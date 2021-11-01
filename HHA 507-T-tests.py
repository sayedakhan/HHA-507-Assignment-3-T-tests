#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 21:34:39 2021

@author: sayedakhan
"""

import pandas as pd
from numpy.random import seed
from numpy.random import randn
from scipy.stats import shapiro
from matplotlib import pyplot
import scipy.stats as stats
from scipy.stats import ttest_ind
from scipy.stats import spearmanr, pearsonr

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

# generate list of var names 
list(diabetes)

# Question 1) 
# Question 1) 
# Question 1) 
# Question 1) 
# Is there a difference between sex (M:F) and the number of days in hospital?

# gender
# time_in_hospital

# P-value and T-test statistic value 
# P-value and T-test statistic value 
# P-value and T-test statistic value 
# P-value and T-test statistic value 


Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']

ttest_ind(Female['time_in_hospital'], Male['time_in_hospital']) 

#p value is exponential (1.4217299655114968e-21) which means
#there is a significant statistical difference between sex (males and females) and the number of days in hospital


# Question 2) 
# Question 2)
# Question 2)
# Question 2)
# Is there a difference between RACE (Caucasian and African American)and the number of days in hospital?
 
# race
# time_in_hospital


# P-value and T-test statistic value 
# P-value and T-test statistic value 
# P-value and T-test statistic value 
# P-value and T-test statistic value 

Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']

ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital']) 

#p value is a negative exponential (4.178330085585203e-07) which means
#there is a significant statistical difference between RACE (Caucasian and African American) and the number of days in hospital

# Question 3) 
# Question 3)
# Question 3)
# Question 3)
# Is there a difference between RACE (Asian and African American)and the number of lab procedures performed?

# race
# time_in_hospital


# P-value and T-test statistic value 
# P-value and T-test statistic value 
# P-value and T-test statistic value 
# P-value and T-test statistic value 

diabetes['totalCountProcedures'] = diabetes['num_procedures'] + diabetes['num_lab_procedures']

Asian = diabetes[diabetes['race']=='Asian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']

ttest_ind(Asian['totalCountProcedures'], AfricanAmerican['totalCountProcedures']) 

#p value is below 0.05 (0.00015123463923369748) which means
#there is a statistical difference between RACE (Asian and African American) and the number of lab procedures



