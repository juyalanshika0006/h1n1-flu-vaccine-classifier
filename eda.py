#Step:2 Exploratory Data Analysis 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#Load the Data
train_features=pd.read_csv("training_set_features.csv")
train_labels=pd.read_csv("training_set_labels.csv")

#Merge features and labels into one dataframe for easy plotting 
train=train_features.merge(train_labels, on='respondent_id')

print("Merged shape:", train.shape)
print("Columns:", train.columns.tolist()[:10], "...")

#Vaccination Rate by Doctor Recommendation

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# H1N1
sns.barplot(data=train, x='doctor_recc_h1n1', y='h1n1_vaccine', ax=axes[0])
axes[0].set_title('H1N1 Vaccination Rate by Doctor Recommendation')
axes[0].set_ylabel('Vaccination Rate')
axes[0].set_xlabel('Doctor Recommended H1N1 Vaccine')

# Seasonal
sns.barplot(data=train, x='doctor_recc_seasonal', y='seasonal_vaccine', ax=axes[1])
axes[1].set_title('Seasonal Vaccination Rate by Doctor Recommendation')
axes[1].set_ylabel('Vaccination Rate')
axes[1].set_xlabel('Doctor Recommended Seasonal Vaccine')

plt.tight_layout()
plt.show()

#Vaccination Rate by Age Group

plt.figure(figsize=(8, 5))
sns.barplot(data=train, x='h1n1_concern', y='h1n1_vaccine', palette='Blues')
plt.title('H1N1 Vaccination Rate by Concern Level')
plt.xlabel('H1N1 Concern (0=Not at all, 3=Very concerned)')
plt.ylabel('Vaccination Rate')
plt.show()


plt.figure(figsize=(10, 5))
sns.barplot(data=train, x='age_group', y='h1n1_vaccine', palette='viridis')
plt.title('H1N1 Vaccination Rate by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Vaccination Rate')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Correlation Between the Two Targets

# Cross-tabulate the two targets
crosstab = pd.crosstab(train['h1n1_vaccine'], train['seasonal_vaccine'], normalize='all')
print("Joint distribution of vaccines:")
print(crosstab)

# Visualize
plt.figure(figsize=(6, 5))
sns.heatmap(crosstab, annot=True, cmap='Blues', fmt='.3f')
plt.title('Joint Distribution: H1N1 vs Seasonal Vaccine')
plt.ylabel('H1N1 Vaccine')
plt.xlabel('Seasonal Vaccine')
plt.show()