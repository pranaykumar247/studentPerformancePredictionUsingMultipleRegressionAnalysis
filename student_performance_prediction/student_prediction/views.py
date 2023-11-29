# student_prediction/views.py
import pandas as pd
import joblib
from django.shortcuts import render
from .forms import ScorePredictionForm1, ScorePredictionForm2, ScorePredictionForm3
import os
from sklearn.preprocessing import LabelEncoder

# Define label encoders for categorical features
gender_encoder = LabelEncoder()
ethnicity_encoder = LabelEncoder()
education_encoder = LabelEncoder()
lunch_encoder = LabelEncoder()
test_prep_encoder = LabelEncoder()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH1 = os.path.join(BASE_DIR, 'ml_models', 'best_student_performance_model1.pkl')
MODEL_PATH2 = os.path.join(BASE_DIR, 'ml_models', 'best_student_performance_model2.pkl')
MODEL_PATH3 = os.path.join(BASE_DIR, 'ml_models', 'best_student_performance_model3.pkl')
DATA_PATH = os.path.join(BASE_DIR, 'data', 'updated_preprocessed_dataset1.csv')

# Load the trained ML model
model1 = joblib.load(MODEL_PATH1)
model2 = joblib.load(MODEL_PATH2)
model3 = joblib.load(MODEL_PATH3)



# Create sets for all possible categories for each feature
possible_genders = set(['male', 'female'])
possible_ethnicities = set(['group A', 'group B', 'group C', 'group D', 'group E'])
possible_educations = set(["associate's degree", "bachelor's degree", 'high school', "master's degree", 'some college', 'some high school'])
possible_lunches = set(['free/reduced', 'standard'])
possible_test_preps = set(['none', 'completed'])

# Fit the label encoders on your training data
gender_encoder.fit(list(possible_genders))
ethnicity_encoder.fit(list(possible_ethnicities))
education_encoder.fit(list(possible_educations))
lunch_encoder.fit(list(possible_lunches))
test_prep_encoder.fit(list(possible_test_preps))


def prediction(request):
    # You can add any necessary logic here, if needed
    return render(request, 'student_prediction/prediction.html')

def prediction_t_test(request):
    # You can add any necessary logic here, if needed
    return render(request, 'student_prediction/prediction_t_test.html')

def prediction_anova(request):
    # You can add any necessary logic here, if needed
    return render(request, 'student_prediction/prediction_anova.html')

# writing score
def writing_score(request):
    # Load the dataset
    dataset = pd.read_csv(DATA_PATH)
    if request.method == 'POST':
        form = ScorePredictionForm1(request.POST)
        if form.is_valid():
            # Get user input from the form
            input_data = form.cleaned_data
            
            # Apply label encoding to categorical features
            input_data['gender'] = gender_encoder.transform([input_data['gender']])[0]
            input_data['race_ethnicity'] = ethnicity_encoder.transform([input_data['race_ethnicity']])[0]
            input_data['parental_level_of_education'] = education_encoder.transform([input_data['parental_level_of_education']])[0]
            input_data['lunch'] = lunch_encoder.transform([input_data['lunch']])[0]
            input_data['test_preparation_course'] = test_prep_encoder.transform([input_data['test_preparation_course']])[0]

            # Create a DataFrame with user input
            user_data = pd.DataFrame([input_data])

            # Predict the missing score using the model
            predicted_score = round(model1.predict(user_data)[0],2)

            # Append user_data to the dataset
            dataset = pd.concat([dataset, user_data], ignore_index=True)

            # Save the updated dataset
            dataset.to_csv(DATA_PATH, index=False)

            return render(request, 'student_prediction/prediction_result.html', {'predicted_score': predicted_score})
    else:
        form = ScorePredictionForm1()

    return render(request, 'student_prediction/writing.html', {'form': form})

#math score
def math_score(request):
    # Load the dataset
    dataset = pd.read_csv(DATA_PATH)
    if request.method == 'POST':
        form = ScorePredictionForm2(request.POST)
        if form.is_valid():
            # Get user input from the form
            input_data = form.cleaned_data
            
            # Apply label encoding to categorical features
            input_data['gender'] = gender_encoder.transform([input_data['gender']])[0]
            input_data['race_ethnicity'] = ethnicity_encoder.transform([input_data['race_ethnicity']])[0]
            input_data['parental_level_of_education'] = education_encoder.transform([input_data['parental_level_of_education']])[0]
            input_data['lunch'] = lunch_encoder.transform([input_data['lunch']])[0]
            input_data['test_preparation_course'] = test_prep_encoder.transform([input_data['test_preparation_course']])[0]

            # Create a DataFrame with user input
            user_data = pd.DataFrame([input_data])

            # Predict the missing score using the model
            predicted_score = round(model2.predict(user_data)[0],2)

            # Append user_data to the dataset
            dataset = pd.concat([dataset, user_data], ignore_index=True)

            # Save the updated dataset
            dataset.to_csv(DATA_PATH, index=False)

            return render(request, 'student_prediction/prediction_result.html', {'predicted_score': predicted_score})
    else:
        form = ScorePredictionForm2()

    return render(request, 'student_prediction/math.html', {'form': form})


#reading score
def reading_score(request):
    # Load the dataset
    dataset = pd.read_csv(DATA_PATH)
    if request.method == 'POST':
        form = ScorePredictionForm3(request.POST)
        if form.is_valid():
            # Get user input from the form
            input_data = form.cleaned_data
            
            # Apply label encoding to categorical features
            input_data['gender'] = gender_encoder.transform([input_data['gender']])[0]
            input_data['race_ethnicity'] = ethnicity_encoder.transform([input_data['race_ethnicity']])[0]
            input_data['parental_level_of_education'] = education_encoder.transform([input_data['parental_level_of_education']])[0]
            input_data['lunch'] = lunch_encoder.transform([input_data['lunch']])[0]
            input_data['test_preparation_course'] = test_prep_encoder.transform([input_data['test_preparation_course']])[0]

            # Create a DataFrame with user input
            user_data = pd.DataFrame([input_data])

            # Predict the missing score using the model
            predicted_score = round(model3.predict(user_data)[0],2)
            
            # Append user_data to the dataset
            dataset = pd.concat([dataset, user_data], ignore_index=True)

            # Save the updated dataset
            dataset.to_csv(DATA_PATH, index=False)

            return render(request, 'student_prediction/prediction_result.html', {'predicted_score': predicted_score})
    else:
        form = ScorePredictionForm3()

    return render(request, 'student_prediction/reading.html', {'form': form})





# plots




### t-test
from django.shortcuts import render
import pandas as pd
import scipy.stats as stats
import numpy as np

def writing_scores_vs_gender(request):
    # Load the dataset from the 'data' folder
    dataset = pd.read_csv('data/stud.csv')

    # Perform the t-test for writing scores vs. gender
    gender = dataset['gender']
    writing_score = dataset['writing_score']

    t_test_result = stats.ttest_ind(writing_score[gender == 'male'], writing_score[gender == 'female'])
   
    female_mean = np.mean(writing_score[gender == 'female'])
    male_mean = np.mean(writing_score[gender == 'male']) 
    
    # Define null hypothesis (H0) and alternative hypothesis (H1)
    null_hypothesis = "There is no significant difference in the mean writing scores between male and female students."
    alternative_hypothesis = "There is a significant difference in the mean writing scores between male and female students."

    # Determine the result based on the p-value
    alpha = 0.05  # Set your significance level
    p_value = t_test_result.pvalue
    if p_value < alpha:
        hypothesis_result = "Reject H0"
    else:
        hypothesis_result = "Fail to Reject H0"

    context = {
        't_test_result': t_test_result,
        'test_name': "Writing Scores vs. Gender",
        'score': 'Writing',
        'female_mean':female_mean,
        'male_mean':male_mean,
        'null_hypothesis': null_hypothesis,
        'alternative_hypothesis': alternative_hypothesis,
        'hypothesis_result': hypothesis_result,
    }
    return render(request, 'student_prediction/t_test_result.html', context)

def reading_scores_vs_gender(request):
    # Load the dataset from the 'data' folder
    dataset = pd.read_csv('data/stud.csv')

    # Perform the t-test for reading scores vs. gender
    gender = dataset['gender']
    reading_score = dataset['reading_score']

    t_test_result = stats.ttest_ind(reading_score[gender == 'male'], reading_score[gender == 'female'])
    
    female_mean = np.mean(reading_score[gender == 'female'])
    male_mean = np.mean(reading_score[gender == 'male']) 

    # Define null hypothesis (H0) and alternative hypothesis (H1)
    null_hypothesis = "There is no significant difference in the mean reading scores between male and female students."
    alternative_hypothesis = "There is a significant difference in the mean reading scores between male and female students."

    # Determine the result based on the p-value
    alpha = 0.05  # Set your significance level
    p_value = t_test_result.pvalue
    if p_value < alpha:
        hypothesis_result = "Reject H0"
    else:
        hypothesis_result = "Fail to Reject H0"

    context = {
        't_test_result': t_test_result,
        'test_name': "Reading Scores vs. Gender",
        'score': 'Reading',
        'female_mean':female_mean,
        'male_mean':male_mean,
        'null_hypothesis': null_hypothesis,
        'alternative_hypothesis': alternative_hypothesis,
        'hypothesis_result': hypothesis_result,
    }
    return render(request, 'student_prediction/t_test_result.html', context)


def math_scores_vs_gender(request):
    # Load the dataset from the 'data' folder
    dataset = pd.read_csv('data/stud.csv')

    # Extract data for male and female students
    math_score_male = dataset[dataset['gender'] == 'male']['math_score']
    math_score_female = dataset[dataset['gender'] == 'female']['math_score']

    # Perform an independent two-sample t-test
    t_test_result = stats.ttest_ind(math_score_male, math_score_female, equal_var=False)
    
    female_mean = np.mean(math_score_female)
    male_mean = np.mean(math_score_male) 

    # Define null hypothesis (H0) and alternative hypothesis (H1)
    null_hypothesis = "There is no significant difference in the mean math scores between male and female students."
    alternative_hypothesis = "There is a significant difference in the mean math scores between male and female students."

    # Determine the result based on the p-value
    alpha = 0.05  # Set your significance level
    p_value = t_test_result.pvalue
    if p_value < alpha:
        hypothesis_result = "Reject H0"
    else:
        hypothesis_result = "Fail to Reject H0"

    context = {
        't_test_result': t_test_result,
        'test_name': "Math Scores vs. Gender",
        'score': 'Math',
        'female_mean':female_mean,
        'male_mean':male_mean,
        'null_hypothesis': null_hypothesis,
        'alternative_hypothesis': alternative_hypothesis,
        'hypothesis_result': hypothesis_result,
    }
    return render(request, 'student_prediction/t_test_result.html', context)




### ONE Way ANOVA TEST 
from scipy.stats import f_oneway
import pandas as pd
# from scipy import stats


def math_scores_vs_parental_education(request):
    
    # Load the dataset from the datasets
    dataset = pd.read_csv('data/stud.csv')
    
    # Extract the relevant data
    math_score = dataset['math_score']
    parental_education = dataset['parental_level_of_education']
    
    # Define the parental education groups
    associate_degree_scores = math_score[parental_education == "associate's degree"]
    bachelor_degree_scores = math_score[parental_education == "bachelor's degree"]
    some_college_scores = math_score[parental_education == "some college"]
    high_school_scores = math_score[parental_education == "high school"]
    some_high_school_scores = math_score[parental_education == "some high school"]
    masters_degree_scores = math_score[parental_education == "master's degree"]
    
    # Perform the one-way ANOVA test
    one_way_anova = stats.f_oneway(
        associate_degree_scores,
        bachelor_degree_scores,
        some_college_scores,
        high_school_scores,
        some_high_school_scores,
        masters_degree_scores
    )
    
    # Define the hypotheses
    # Null Hypothesis (H0): All parental education groups have the same population mean math score.
    # Alternative Hypothesis (H1): At least one parental education group has a different population mean math score.
    
    # Get the p-value from the ANOVA result
    p_value = one_way_anova.pvalue
    
    # Determine whether to accept or reject H0 based on the p-value
    if p_value < 0.05:  # You can choose your significance level (0.05 is common)
        hypothesis_result = "Reject H0"
    else:
        hypothesis_result = "Fail to Reject H0"
    
    context = {
        'anova_result': one_way_anova,
        'test_name': "Math Scores vs Parental Education",
        'null_hypothesis': "All parental education groups have the same population mean math score.",
        'alternative_hypothesis': "At least one parental education group has a different population mean math score.",
        'hypothesis_result': hypothesis_result  # Display the result based on the p-value
    }
    
    return render(request, 'student_prediction/anova_result.html', context)

    

def reading_scores_vs_parental_education(request):
    #Load the dataset from the datasets
    dataset = pd.read_csv('data/stud.csv')
    
    # Perform the one way anova for math scores vs parental education
    reading_score = dataset['reading_score']
    parental_education = dataset['parental_level_of_education']
    
    one_way_anova = stats.f_oneway(reading_score[parental_education == "associate's degree"], reading_score[parental_education == "bachelor's degree"], reading_score[parental_education == "some college"], reading_score[parental_education =="high school"], reading_score[parental_education=="some high school"], reading_score[parental_education=="master's degree"])
    
    p_value = one_way_anova.pvalue
    
    # Determine whether to accept or reject H0 based on the p-value
    if p_value < 0.05:  # You can choose your significance level (0.05 is common)
        hypothesis_result = "Reject H0 and Accept H1"
    else:
        hypothesis_result = "Fail to Reject H0"
    
    context = {
        'anova_result': one_way_anova,
        'test_name': "Reading Scores vs Parental Education",
        'null_hypothesis': "All parental education groups have the same population mean math score.",
        'alternative_hypothesis': "At least one parental education group has a different population mean reading score.",
        'hypothesis_result': hypothesis_result  # Display the result based on the p-value
    }
    
    return render(request, 'student_prediction/anova_result.html', context)

def writing_scores_vs_parental_education(request):
    #Load the dataset from the datasets
    dataset = pd.read_csv('data/stud.csv')
    
    # Perform the one way anova for math scores vs parental education
    writing_score = dataset['writing_score']
    parental_education = dataset['parental_level_of_education']
    
    one_way_anova = stats.f_oneway(writing_score[parental_education == "associate's degree"], writing_score[parental_education == "bachelor's degree"], writing_score[parental_education == "some college"], writing_score[parental_education =="high school"], writing_score[parental_education=="some high school"], writing_score[parental_education=="master's degree"])
    
    p_value = one_way_anova.pvalue
    
    # Determine whether to accept or reject H0 based on the p-value
    if p_value < 0.05:  # You can choose your significance level (0.05 is common)
        hypothesis_result = "Reject H0"
    else:
        hypothesis_result = "Fail to Reject H0"
    
    context = {
        'anova_result': one_way_anova,
        'test_name': "Writing Scores vs Parental Education",
        'null_hypothesis': "All parental education groups have the same population mean math score.",
        'alternative_hypothesis': "At least one parental education group has a different population mean writing score.",
        'hypothesis_result': hypothesis_result  # Display the result based on the p-value
    }
    
    return render(request, 'student_prediction/anova_result.html', context)