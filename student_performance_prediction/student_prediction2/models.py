from django.db import models

class Student2(models.Model):
    hours_studied = models.IntegerField()
    previous_scores = models.IntegerField()
    extracurricular_activities = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    sleep_hours = models.IntegerField()
    sample_question_papers_practiced = models.IntegerField()
    performance_index = models.FloatField()

    def __str__(self):
        return f'Student2 {self.pk}'
