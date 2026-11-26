from django.db import models

from accounts.models import User

# Create your models here.

class Course(models.Model):

    LANGUAGE_CHOICES = [
    ('python', 'Python'),
    ('java', 'Java'),
    ('javascript', 'JavaScript'),
    ('c', 'C'),
    ('cpp', 'C++'),
    ('csharp', 'C#'),
    ('php', 'PHP'),
    ('ruby', 'Ruby'),
    ('go', 'Go'),
    ('kotlin', 'Kotlin'),
    ('swift', 'Swift'),
    ('typescript', 'TypeScript'),
    ('sql', 'SQL'),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField

    langauge = models.CharField(max_length=200,choices=LANGUAGE_CHOICES,default="python")

    duration = models.CharField(max_length=200)

    fee = models.PositiveIntegerField()

    cover_picture = models.ImageField(upload_to="cover_pics",null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    trainer = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    