Summary for Question 1
15464
patient_id,visit_date,age,education_level,walking_speed
P0001,2020-01-29,35.64,High School,4.0
P0001,2020-04-14,35.85,High School,4.01
P0001,2020-07-25,36.13,High School,4.14
P0001,2020-10-11,36.34,High School,4.03
P0001,2021-01-10,36.59,High School,4.11
P0001,2021-04-12,36.84,High School,3.29
P0001,2021-07-11,37.09,High School,4.0
P0001,2021-10-16,37.35,High School,3.66
P0001,2022-01-28,37.64,High School,3.69
## Mean Walking Speed by Education Level

education_level
Bachelors       4.040544
Graduate        4.485526
High School     3.252443
Some College    3.656462

## Mean Visit Cost by Insurance Type

insurance_type
Bronze      200.096845
Gold        100.110730
Platinum     49.905000
Silver      149.839975

## Effect of Age on Walking Speed

Correlation: -0.69## Step 1: Walking Speed Analysis
Fixed Effects:
Intercept                             5.623463
C(education_level)[T.Graduate]        0.398105
C(education_level)[T.High School]    -0.809417
C(education_level)[T.Some College]   -0.413514
age                                  -0.030265

Random Effects Variance:
          Group
Group  0.001824

Confidence Intervals:
                                           0         1
Intercept                           5.602343  5.644582
C(education_level)[T.Graduate]      0.381236  0.414974
C(education_level)[T.High School]  -0.825780 -0.793055
C(education_level)[T.Some College] -0.430144 -0.396884
age                                -0.030605 -0.029926
Group Var                           0.002240  0.029770

## Step 2: Cost Analysis
                 count        mean        std         min         25%         50%         75%         max
insurance_type                                                                                           
Bronze          3800.0  200.096845  10.116974  165.127237  193.304028  200.179625  206.931297  233.587981
Gold            3985.0  100.110730   9.848678   66.742084   93.631367  100.026471  106.751302  134.524268
Platinum        3823.0   49.905000   9.928111   16.079500   43.320408   50.013032   56.507437   86.923715
Silver          3856.0  149.839975   9.973272  116.011359  143.079681  149.691183  156.637540  189.608701

Effect Size (Eta-Squared): 0.9689

## Step 3: Advanced Analysis
### Interaction Effects on Walking Speed
                            OLS Regression Results                            
==============================================================================
Dep. Variable:          walking_speed   R-squared:                       0.811
Model:                            OLS   Adj. R-squared:                  0.811
Method:                 Least Squares   F-statistic:                     9452.
Date:                Wed, 04 Dec 2024   Prob (F-statistic):               0.00
Time:                        16:55:44   Log-Likelihood:                -5224.9
No. Observations:               15464   AIC:                         1.047e+04
Df Residuals:                   15456   BIC:                         1.053e+04
Df Model:                           7                                         
Covariance Type:            nonrobust                                         
==========================================================================================================
                                             coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------------------------
Intercept                                  5.6141      0.016    349.768      0.000       5.583       5.646
C(education_level)[T.Graduate]             0.3946      0.023     16.950      0.000       0.349       0.440
C(education_level)[T.High School]         -0.7951      0.023    -34.443      0.000      -0.840      -0.750
C(education_level)[T.Some College]        -0.4015      0.024    -16.950      0.000      -0.448      -0.355
age                                       -0.0301      0.000   -103.724      0.000      -0.031      -0.030
C(education_level)[T.Graduate]:age      7.489e-05      0.000      0.176      0.861      -0.001       0.001
C(education_level)[T.High School]:age     -0.0003      0.000     -0.655      0.512      -0.001       0.001
C(education_level)[T.Some College]:age    -0.0002      0.000     -0.538      0.591      -0.001       0.001
==============================================================================
Omnibus:                        2.248   Durbin-Watson:                   1.876
Prob(Omnibus):                  0.325   Jarque-Bera (JB):                2.207
Skew:                           0.007   Prob(JB):                        0.332
Kurtosis:                       2.943   Cond. No.                         772.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Confidence Intervals:
                                               0         1
Intercept                               5.582594  5.645517
C(education_level)[T.Graduate]          0.348951  0.440209
C(education_level)[T.High School]      -0.840399 -0.749898
C(education_level)[T.Some College]     -0.447883 -0.355031
age                                    -0.030654 -0.029517
C(education_level)[T.Graduate]:age     -0.000761  0.000911
C(education_level)[T.High School]:age  -0.001099  0.000548
C(education_level)[T.Some College]:age -0.001082  0.000616

