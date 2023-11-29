from django import forms

# Performance Index
class performance_index_form(forms.Form):
    hours_studied = forms.IntegerField(label='Hours Studied', min_value=0)
    previous_scores = forms.IntegerField(label='Previous Scores', min_value=0)
    extracurricular_activities = forms.ChoiceField(
        choices=[(1, 'Yes'), (0, 'No')],
        label='Extracurricular Activities (1 for Yes and 0 for No)'
    )
    sleep_hours = forms.IntegerField(label='Sleep Hours', min_value=0)
    sample_question_papers_practiced = forms.IntegerField(
        label='Sample Question Papers Practiced', min_value=0
    )





