from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
	objects = models.Manager()
	published = PublishedManager()

	STATUS_CHOICES = {
	('draft','Draft'),
	('published','Published'),
	}

	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120)
	author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
	body = models.TextField(default='')
	likes = models.ManyToManyField(User, related_name='like',blank=True)
	created = models.DateTimeField(auto_now_add=True) #auto_now_add is used at the time of creation
	updated = models.DateTimeField(auto_now=True) #auto_now is used while updating the created thing
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	restrict_comment = models.BooleanField(default=False)

	class Meta:
		ordering = ['-id']


	def __str__(self):
		return self.title

	def total_likes(self):
		return self.likes.count()

	def get_absolute_url(self):
		url = reverse("post_detail", kwargs={"id":self.id, "slug":self.slug})
		return url


@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
	slug = slugify(kwargs['instance'].title)
	kwargs['instance'].slug = slug


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dob = models.DateTimeField(null=True, blank=True)
	photo = models.ImageField(default='default.png', blank=True)

	def __str__(self):
		return "Profile Of User {}".format(self.user.username)


class Images(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/',blank=True, null=True)

	def __str__(self):
		return self.post.title + " Image"

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	reply = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)
	content = models.TextField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return '{}-{}'.format(self.post.title, str(self.user.username))

