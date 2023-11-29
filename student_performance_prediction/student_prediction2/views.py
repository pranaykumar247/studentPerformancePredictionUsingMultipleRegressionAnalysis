# student_prediction2/views.py
import pandas as pd
import joblib
from django.shortcuts import render
from .forms import performance_index_form
import pandas as pd
import matplotlib.pyplot as plt
from django.http import HttpResponse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Model Path 
MODEL_PATH1 = os.path.join(BASE_DIR,'ml_models','best_student_performance_model4.pkl')

# Data Path
DATA_PATH = os.path.join(BASE_DIR,'data','updated_preprocessed_dataset2.csv')



# Loading the Model
model1 = joblib.load(MODEL_PATH1)


# Create your views here.
def prediction(request):
    # You can add any necessary logic here, if needed
    return render(request, 'student_prediction2/prediction.html')

def predict_performance_index(request):
    dataset = pd.read_csv(DATA_PATH)
    
    
    if request.method == 'POST':
        form  = performance_index_form(request.POST)
        if form.is_valid():
            
            # Get user input from the form
            input_data = form.cleaned_data
            
            # Create a DataFrame with user input
            user_data = pd.DataFrame([input_data])
            
            # Define a dictionary to map old column names to new names
            column_mapping = {
                'hours_studied': 'Hours Studied',
                'previous_scores': 'Previous Scores',
                'extracurricular_activities': 'Extracurricular Activities',
                'sleep_hours': 'Sleep Hours',
                'sample_question_papers_practiced': 'Sample Question Papers Practiced'
            }

            # Rename the columns in user_data
            user_data.rename(columns=column_mapping, inplace=True)
            
            # Make predictions using model and store it in variable
            predicted_performance = round(model1.predict(user_data)[0],2)
            
            # Append user_data to the dataset
            dataset = pd.concat([dataset, user_data], ignore_index=True)
                
            # Save the updated Dataset
            dataset.to_csv(DATA_PATH,index = False)

            return render(request,'student_prediction2/prediction_result.html',{'predicted_performance':predicted_performance})
    
    else:
        form= performance_index_form()
        
    return render(request,'student_prediction2/user_input_form.html',{'form':form})



def scatter_plot(request):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(DATA_PATH)

    # Extract data columns from the DataFrame
    hours_studied = df['Hours Studied']
    previous_scores = df['Previous Scores']
    
    # Create a scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(hours_studied, previous_scores, c='blue', marker='o', alpha=0.5)
    plt.title('Scatter Plot of Hours Studied vs. Previous Scores')
    plt.xlabel('Hours Studied')
    plt.ylabel('Previous Scores')
    
    image_path = os.path.join(BASE_DIR,'static/images','scatter_plot.png')
    
    # Save the plot as an image file (optional)
    plt.savefig(image_path)

    context = {'scatter_plot_image':image_path}

    
    return render(request,'student_prediction2/prediction_result.html',context)
