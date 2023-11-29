from django.urls import path
from . import views

app_name = 'student_prediction2'

urlpatterns = [
    path('predictions2/',views.prediction,name = 'prediction'),
    path('predict_performance_index/', views.predict_performance_index, name='predict_performance_index'),
    path('scatter_plot/', views.scatter_plot, name='scatter_plot'),
]
