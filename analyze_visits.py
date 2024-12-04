import pandas as pd
import numpy as np

# Load and structure the data:
df = pd.read_csv('ms_data.csv')
df.dropna(inplace = True)
df["visit_date"] = pd.to_datetime(df["visit_date"])
df["patient_id"] = df["patient_id"].astype(str)
df["age"] = df["age"].astype(float)
df["education_level"] = df["education_level"].astype("category")
df["walking_speed"] = df["walking_speed"].astype(float)
df.sort_values(by=["patient_id", "visit_date"])

#Add insurance information
with open("insurance.lst", "r") as f:
    next(f) 
    insurance_types = [line.strip() for line in f] 
print(insurance_types)

np.random.seed(11) 
unique_patient_ids = df["patient_id"].unique()
unique_id = df["patient_id"].unique()
df["insurance_type"] = ""
for patient_id in unique_id:
    assigned = np.random.choice(insurance_types)
    df.loc[df["patient_id"] == patient_id, "insurance_type"] = assigned

cost = {"Bronze": 200, "Silver": 150, "Gold": 100, "Platinum": 50}
df["visit_cost"] = 0.0
for insurance_type in cost:
    row = df["insurance_type"] == insurance_type
    variation = np.random.normal(0, 10, size=row.sum())
    df.loc[row, "visit_cost"] = cost[insurance_type] + variation


#Calculate summary statistics
edu_walk = df.groupby("education_level")["walking_speed"].mean()
type_cost = df.groupby("insurance_type")["visit_cost"].mean()
age_walk = df[["age", "walking_speed"]].corr().loc["age", "walking_speed"] 
summary = [
    "## Mean Walking Speed by Education Level\n",
    edu_walk.to_string(),
    "\n## Mean Visit Cost by Insurance Type\n",
    type_cost.to_string(),
    "\n## Effect of Age on Walking Speed\n",
     f"Correlation: {age_walk:.2f}",
]
print(summary)

#with open("README.md", "a") as f: 
#    f.write("\n".join(summary))

# df.to_csv("question2.csv")