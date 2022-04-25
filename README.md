# Case Study on healthier lifestyle incentives

## Project Description

An organisation would like to offer their employees an allowance to live a healthier lifestyle, and improve the physical health of their employees.
However, the organisation cannot afford to give this allowance to all employees and have requested the data science team to help identify the employees
that will benefit most from this.

The data science team conducted research and found a dataset on the internet, that they believe can help them predict if someone 
is at risk for heart disease or not, which they believe will be a good indicator of employees that will benefit from this health-allowance .
    
The dataset that they found was collected by asking the following questions to a certain group of people:
    
- `HeartDisease`:	Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI)
- `BMI`:	Body Mass Index (BMI)
- `Smoking`:	Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]
- `AlcoholDrinking`:	Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week
- `Stroke`:	(Ever told) (you had) a stroke?
- `PhysicalHealth`:	Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? (0-30 days)
- `ID`:	Survey question unique identifier
- `MentalHealth`:	Thinking about your mental health, for how many days during the past 30 days was your mental health not good? (0-30 days)
- `DiffWalking`:	Do you have serious difficulty walking or climbing stairs?
- `Income`: What is your monthly income/salary?	
- `Sex`:	Are you male or female?
- `AgeCategory`:	Fourteen-level age category
- `Race`:	Imputed race/ethnicity value
- `Diabetic`:	(Ever told) (you had) diabetes?
- `PhysicalActivity`:	Adults who reported doing physical activity or exercise during the past 30 days other than their regular job
- `GenHealth`:	Would you say that in general your health is...
- `SleepTime`:	On average, how many hours of sleep do you get in a 24-hour period?
- `Asthma`:	(Ever told) (you had) asthma?
- `KidneyDisease`:	Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?
- `SkinCancer`:	(Ever told) (you had) skin cancer?

## Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling
        
## Technologies
* Python
* Pandas, jupyter
* AWS Sagemaker

## Project Structure
1. Importing the required libraries.
2. Importing and Reading the dataset.
3. Exploratory Data Analysis (EDA)
4. Data-Preprocessing
5. Data Visualization
    - Correlation Matrix
    - Pairplot
    - Countplots
6. Data Modeling
    - Separating the data into features and target variable.
    - Splitting the data into training and test sets.
    - Modeling/ Training the data
    - Predicting the data
    - Calculating the prediction scores
    - Getting the model's accuracy
        - Classification Report
        - Confusion Matrix
        - Plotting the confusion matrix

##  Evaluation Metrics

The model will be using various evaluation metrics such as

- Accuracy: which refers to how close a measurement is to the true value and can be calculated using the following formula

![image](https://user-images.githubusercontent.com/30470730/72439883-c586f180-37cd-11ea-94a3-09c09cbd4814.png)


- Precision: which is how consistent results are when measurements are repeated and can be calculated using the following formula

 ![image](https://user-images.githubusercontent.com/30470730/72440009-10a10480-37ce-11ea-8f11-0a3352d0646c.png)

- Recall: which refers to the percentage of total relevant results correctly classified by the model and can be calculated using the formula

 ![image](https://user-images.githubusercontent.com/30470730/72440027-1565b880-37ce-11ea-8bf9-5c5d7a609f85.png)

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](case_study.csv) within this repo.
3.On local machine create a venv then install requirement.txt    
    



