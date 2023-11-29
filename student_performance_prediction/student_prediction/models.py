# student_prediction/models.py
from django.db import models

class UserEnteredData(models.Model):
    # Define fields as needed
    gender = models.CharField(max_length=10)
    race_ethnicity = models.CharField(max_length=20)
    parental_level_of_education = models.CharField(max_length=50)
    lunch = models.CharField(max_length=20)
    test_preparation_course = models.CharField(max_length=20)
    math_score = models.IntegerField()
    reading_score = models.IntegerField()
    writing_score = models.IntegerField()

# models.py

from django.db import models

class ScoreData(models.Model):
    gender = models.CharField(max_length=10)
    writing_score = models.IntegerField()
    reading_score = models.IntegerField()
    math_score = models.IntegerField()
