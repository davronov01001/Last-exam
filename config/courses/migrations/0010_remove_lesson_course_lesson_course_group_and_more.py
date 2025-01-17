# Generated by Django 5.0.7 on 2024-10-13 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_comment_content_alter_comment_lesson_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='courses.coursegroup'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='lesson',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.lesson'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.student'),
        ),
    ]
