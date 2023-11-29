from django.urls import path
from . import views

app_name = 'student_prediction'

urlpatterns = [
    path('predictions/',views.prediction,name = 'prediction'),
    path('prediction_t_test/',views.prediction_t_test,name = 'prediction_t_test'),
    path('prediction_anova/',views.prediction_anova,name = 'prediction_anova'),
    path('writing_scores_vs_gender/', views.writing_scores_vs_gender, name='writing_scores_vs_gender'),
    path('reading_scores_vs_gender/', views.reading_scores_vs_gender, name='reading_scores_vs_gender'),
    path('math_scores_vs_gender/', views.math_scores_vs_gender, name='math_scores_vs_gender'),
    path('math_scores_vs_parental_education/', views.math_scores_vs_parental_education, name='math_scores_vs_parental_education'),
    path('reading_scores_vs_parental_education/', views.reading_scores_vs_parental_education, name='reading_scores_vs_parental_education'),
    path('writing_scores_vs_parental_education/', views.writing_scores_vs_parental_education, name='writing_scores_vs_parental_education'),
    path('predict_writing/', views.writing_score, name='writing_score'),
    path('predict_math/', views.math_score, name='math_score'),
    path('predict_reading/', views.reading_score, name='reading_score'),
]
