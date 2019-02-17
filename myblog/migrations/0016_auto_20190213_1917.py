# Generated by Django 2.1.1 on 2019-02-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0015_auto_20190213_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
