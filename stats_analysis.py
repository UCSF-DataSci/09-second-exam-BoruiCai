import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import f_oneway, ttest_ind
import seaborn as sns
# Analyze walking speed:
df = pd.read_csv('question2.csv')

multi_reg = smf.mixedlm("walking_speed ~ C(education_level) + age", 
                        data=df, 
                        groups=df["patient_id"]).fit()

print("\nKey Statistics:")
print(f"Fixed Effects:\n{multi_reg.fe_params}")
print(f"Random Effects Variance:\n{multi_reg.cov_re}")
print(f"Confidence Intervals:\n{multi_reg.conf_int()}")

# Analyze costs
## boxplot
ana = (df.groupby("insurance_type")["visit_cost"].describe())
print(ana)
plt.figure(figsize=(10, 6))
sns.boxplot(x="visit_cost", y="insurance_type", data = df)
plt.title("Visit Costs by Insurance Type")
plt.show()

##effect size
grand_mean = df["visit_cost"].mean()
group_means = df.groupby("insurance_type")["visit_cost"].mean()
group_sizes = df.groupby("insurance_type")["visit_cost"].size()
sst = ((df["visit_cost"] - grand_mean) ** 2).sum()
ssb = sum(group_sizes[ins] * (group_means[ins] - grand_mean) ** 2 for ins in group_means.index)
eta2 = ssb / sst
print(f"\nEffect Size: {eta2:.4f}")

# Advanced analysis
### Interaction effect
model = smf.ols("walking_speed ~ C(education_level) * age", data=df).fit()
print("\nRegression Analysis with Interaction Effects")
print(model.summary())
print(f"Confidence Intervals:\n{model.conf_int()}")
