# -*- coding: utf-8 -*-
"""
Case Study
  
Your organisation would like to offer their employees an allowance to live a healthier lifestyle, and improve the physical health of their employees.
However, the organisation cannot afford to give this allowance to all employees and have requested the data science team to help identify the employees
that will benefit most from this.

The data science team conducted research and found a dataset on the internet, that they believe can help them predict if someone 
is at risk for heart disease or not, which they believe will be a good indicator of employees that will benefit from this health-allowance .
    
The dataset that they found was collected by asking the following questions to a certain group of people:
    
HeartDisease:	Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI)
BMI:	Body Mass Index (BMI)
Smoking:	Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]
AlcoholDrinking:	Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week
Stroke:	(Ever told) (you had) a stroke?
PhysicalHealth:	Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? (0-30 days)
ID:	Survey question unique identifier
MentalHealth:	Thinking about your mental health, for how many days during the past 30 days was your mental health not good? (0-30 days)
DiffWalking:	Do you have serious difficulty walking or climbing stairs?
Income: What is your monthly income/salary?	
Sex:	Are you male or female?
AgeCategory:	Fourteen-level age category
Race:	Imputed race/ethnicity value
Diabetic:	(Ever told) (you had) diabetes?
PhysicalActivity:	Adults who reported doing physical activity or exercise during the past 30 days other than their regular job
GenHealth:	Would you say that in general your health is...
SleepTime:	On average, how many hours of sleep do you get in a 24-hour period?
Asthma:	(Ever told) (you had) asthma?
KidneyDisease:	Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?
SkinCancer:	(Ever told) (you had) skin cancer?
   
  
"""


"""

Please follow the following steps as indicated in the code
1. Identify the target column and assign to y (1)
2. Identify columns from the data set that you will use as features for the model, please motivate columns that you REMOVE/LEAVE OUT , if any (3)
3. Using your own discretion, apply 2-5 transformations to the dataset so that it can be used for classifier model
    and motivate each transformation in the comments, see first transformation as example (10)
4. Create a visualisation that will help you determine if there are correlations between the features you created for this model (3)
5. Create test and training data sets (2)
6. Apply any steps (please explain the steps in the comments) you see fit to improve the initial model's output (15)
7. Evaluate the model's performance using accuracy, precision and recall in predicting a case of HeartDisease. (3)
8. Motivate if the model in its current form will be sufficient for its intended purpose or not. (10)
9. Briefly discuss the issue of overfitting and how to mitigate it (2)
10. Suggest alternative solutions to solve the organisation's problem (1)



"""

import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import warnings
warnings.simplefilter("ignore")
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score

#please import any other modules you need to complete this case study

"""
read data from supplied csv into pandas dataframe

"""
data = pd.read_csv('case_study.csv')




"Processing/Transformations: questions 1 - 5"

# 1
y =


# 2
X = 

"""
Column left out:
Motivation:

Column left out:
Motivation:
.
.
.
.
"""



#3
"""
Transformation 1: Convert target column into integers
Motivation: Some motivation for this transformation

"""
y = y.apply(lambda x: 0 if x=='No' else 1)



"""
Transformation 2: 
Motivation: 

"""

"""
Transformation 3: 
Motivation: 

"""

"""
Transformation 4: 
Motivation: 

"""


"""
Transformation 5: 
Motivation: 

"""

"""
Transformation 6: 
Motivation: 

"""

 
"""
Visualisation
"""

#4





#5
X_train, X_test, y_train, y_test =



"""
train model
"""

"""
initial model
"""
clf = DecisionTreeClassifier()
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)


#6
"""
Your improved model
Description of steps taken to improve model:
    XXXX
"""



"""
evaluate model
"""
#7

"""
accuracy:
precision:
recall:
"""

#8
"""
Comments on the performance and usability  of the model:
    
    
    
    
"""   



#9
"""
Overfitting



"""


#10
"""
Alternative solutions



"""
