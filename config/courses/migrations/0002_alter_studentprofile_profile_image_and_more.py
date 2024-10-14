# Generated by Django 5.0.7 on 2024-10-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='students/profile_photo/'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='teachers/profile/'),
        ),
    ]
