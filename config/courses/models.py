from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User, Group


class Days(models.Model):
    """Days when Lessons are scheduled"""
    week_day = models.CharField(max_length=15)

    def __str__(self):
        return self.week_day


STATUS_CHOICES = [
    ('not_started', "Not Started Yet"),
    ('continuing', "Continuing"),
    ('ended', "Ended"),
    ('freezed', "Freezed"),
]


class Category(models.Model):
    """Type of courses"""
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    """Available Courses"""
    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class CourseGroup(models.Model):
    """Organized groups for Courses"""
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=5, help_text="Group name: (example: FN1)")
    starts = models.DateField()
    ends = models.DateField()
    time = models.TimeField()
    days = models.ManyToManyField(Days)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Lesson"""
    course_group = models.ForeignKey(CourseGroup, on_delete=models.SET_NULL, null=True, related_name='lessons')
    start_lesson = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255, help_text="Topic of the lesson: ")

    def __str__(self):
        return self.topic


class LessonVideo(models.Model):
    """Video of the lesson"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='videos')
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to="lesson/videos/", validators=[FileExtensionValidator(['mp4', 'avi'])])

    def __str__(self):
        return self.name


GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]


class Teacher(models.Model):
    """Teachers"""
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(Course, related_name='teachers')
    experience = models.IntegerField(default=1)
    sphere_of_teaching = models.CharField(max_length=100)
    is_working = models.BooleanField(default=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    courses = models.ManyToManyField(Course, related_name='teacher_profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    profile_image = models.ImageField(upload_to='teachers/profile/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.courses}"


class Student(models.Model):
    """Students"""
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(Course, related_name='students')
    is_studying = models.BooleanField(default=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to='students/profile_photo/', blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    courses = models.ManyToManyField(CourseGroup, related_name='profiles')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


REACTION_CHOICES = [
    ('like', 'Like'),
    ('dislike', 'Dislike'),
]


class Reaction(models.Model):
    """Reactions of Students to Lessons"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='reactions')
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} {self.lesson.topic} {self.reaction_type}"


class Comment(models.Model):
    """Comments to Lesson"""
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, null=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
