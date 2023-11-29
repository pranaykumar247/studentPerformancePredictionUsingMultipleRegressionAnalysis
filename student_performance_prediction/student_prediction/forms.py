# student_prediction/forms.py
from django import forms

#writing score
class ScorePredictionForm1(forms.Form):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ethnicity_choices = [
        ('group A', 'Group A'),
        ('group B', 'Group B'),
        ('group C', 'Group C'),
        ('group D', 'Group D'),
        ('group E', 'Group E'),
    ]

    education_choices = [
        ("associate's degree", "Associate's Degree"),
        ("bachelor's degree", "Bachelor's Degree"),
        ('high school', 'High School'),
        ("master's degree", "Master's Degree"),
        ('some college', 'Some College'),
        ('some high school', 'Some High School'),
    ]

    lunch_choices = [
        ('free/reduced', 'Free/Reduced'),
        ('standard', 'Standard'),
    ]

    test_prep_choices = [
        ('none', 'None'),
        ('completed', 'Completed'),
    ]

    gender = forms.ChoiceField(choices=gender_choices, label='Gender')
    race_ethnicity = forms.ChoiceField(choices=ethnicity_choices, label='Race or Ethnicity')
    parental_level_of_education = forms.ChoiceField(choices=education_choices, label='Parental Level of Education')
    lunch = forms.ChoiceField(choices=lunch_choices, label='Lunch Type')
    test_preparation_course = forms.ChoiceField(choices=test_prep_choices, label='Test Preparation Course')
    math_score = forms.FloatField(label='Math Score',max_value=100,min_value=0)
    reading_score = forms.FloatField(label='Reading Score',max_value=100,min_value=0)
    
#math score
class ScorePredictionForm2(forms.Form):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ethnicity_choices = [
        ('group A', 'Group A'),
        ('group B', 'Group B'),
        ('group C', 'Group C'),
        ('group D', 'Group D'),
        ('group E', 'Group E'),
    ]

    education_choices = [
        ("associate's degree", "Associate's Degree"),
        ("bachelor's degree", "Bachelor's Degree"),
        ('high school', 'High School'),
        ("master's degree", "Master's Degree"),
        ('some college', 'Some College'),
        ('some high school', 'Some High School'),
    ]

    lunch_choices = [
        ('free/reduced', 'Free/Reduced'),
        ('standard', 'Standard'),
    ]

    test_prep_choices = [
        ('none', 'None'),
        ('completed', 'Completed'),
    ]

    gender = forms.ChoiceField(choices=gender_choices, label='Gender')
    race_ethnicity = forms.ChoiceField(choices=ethnicity_choices, label='Race or Ethnicity')
    parental_level_of_education = forms.ChoiceField(choices=education_choices, label='Parental Level of Education')
    lunch = forms.ChoiceField(choices=lunch_choices, label='Lunch Type')
    test_preparation_course = forms.ChoiceField(choices=test_prep_choices, label='Test Preparation Course')
    reading_score = forms.FloatField(label='Reading Score',max_value=100,min_value=0)
    writing_score = forms.FloatField(label='Writing Score',max_value=100,min_value=0)
    
   
    
# Reading Score    
class ScorePredictionForm3(forms.Form):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ethnicity_choices = [
        ('group A', 'Group A'),
        ('group B', 'Group B'),
        ('group C', 'Group C'),
        ('group D', 'Group D'),
        ('group E', 'Group E'),
    ]

    education_choices = [
        ("associate's degree", "Associate's Degree"),
        ("bachelor's degree", "Bachelor's Degree"),
        ('high school', 'High School'),
        ("master's degree", "Master's Degree"),
        ('some college', 'Some College'),
        ('some high school', 'Some High School'),
    ]

    lunch_choices = [
        ('free/reduced', 'Free/Reduced'),
        ('standard', 'Standard'),
    ]

    test_prep_choices = [
        ('none', 'None'),
        ('completed', 'Completed'),
    ]

    gender = forms.ChoiceField(choices=gender_choices, label='Gender')
    race_ethnicity = forms.ChoiceField(choices=ethnicity_choices, label='Race or Ethnicity')
    parental_level_of_education = forms.ChoiceField(choices=education_choices, label='Parental Level of Education')
    lunch = forms.ChoiceField(choices=lunch_choices, label='Lunch Type')
    test_preparation_course = forms.ChoiceField(choices=test_prep_choices, label='Test Preparation Course')
    math_score = forms.FloatField(label='Math Score',max_value=100,min_value=0)
    writing_score = forms.FloatField(label='Writing Score',max_value=100,min_value=0)

    

# Uploading CSV file for performing various tests
from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')

