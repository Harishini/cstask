from django.db import models

# Create your models here.
WEEK_CHOICES = (
    ('week1', "Week 1"),
    ('week2', "Week 2"),
    ('week3', "Week 3"),
    ('week4', "Week 4"),
    ('week5', "Week 5"),
    ('week6', "Week 6"),
    ('week7', "Week 7"),
    ('week8', "Week 8"), 
)
class course(models.Model):
    week=models.CharField(max_length=10, choices=WEEK_CHOICES)
    course_name=models.CharField(max_length=100)
    resource_person=models.CharField(max_length=100)

    def __str__(self):
        return self.week

