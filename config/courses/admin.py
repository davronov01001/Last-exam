from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Days)
class DayView(admin.ModelAdmin):
    list_display = ('id', 'week_day')
    list_editable = ('week_day',)

@admin.register(Category)
class CategoryView(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)

@admin.register(Course)
class CourseView(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_editable = ('name', 'category')

@admin.register(CourseGroup)
class CourseGroupView(admin.ModelAdmin):
    list_display = ('id', 'course', 'name', 'starts', 'ends', 'time', 'status')
    list_editable = ('course', 'name', 'starts', 'ends', 'time', 'status')

@admin.register(Lesson)
class LessonView(admin.ModelAdmin):
    list_display = ('id', 'course_group', 'start_lesson', 'topic')
    list_editable = ('course_group', 'topic')

@admin.register(LessonVideo)
class LessonVideoView(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'name', 'video')
    list_editable = ('lesson', 'name', 'video')

@admin.register(Teacher)
class TeacherView(admin.ModelAdmin):
    list_display = ('id', 'user','group', 'experience', 'sphere_of_teaching', 'is_working', 'birth_date', 'phone_number', 'gender', 'profile_image')
    list_editable = ('user','group', 'experience', 'sphere_of_teaching', 'is_working', 'birth_date', 'phone_number', 'gender', 'profile_image')

@admin.register(Student)
class StudentView(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'is_studying', 'birth_date', 'phone_number', 'profile_image', 'gender', 'view_image')
    list_editable = ('user', 'group', 'user','is_studying', 'birth_date', 'phone_number', 'profile_image', 'gender')
    def view_image(self, obj):
        if obj.profile_image:
            return mark_safe(f'<img src="{obj.profile_image.url}" style="height: 100px;"/>')
        return "(No image)"
    
    view_image.short_description = "Profile Image"

@admin.register(Reaction)
class ReactionView(admin.ModelAdmin):
    list_display = ('id', 'user', 'lesson', 'reaction_type')
    list_editable = ('user', 'lesson', 'reaction_type')
