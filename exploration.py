# Step 1: Load and inspect the H1N1 competition data
# Dataset: DrivenData Flu Shot Learning

import pandas as pd

#Load the three csv files
train_features=pd.read_csv("training_set_features.csv")
train_labels=pd.read_csv("training_set_labels.csv")
test_features=pd.read_csv("test_set_features.csv")

#Determine the shape of the dataframes

print("Training Features Shape:", train_features.shape)
print("Training Labels Shape:", train_labels.shape)
print("Test Features Shape:", test_features.shape)

#Determine the first few rows of the dataframes

print("Training Features:")
print(train_features.head())
print("Training Labels:")
print(train_labels.head())
print("Test Features:")
print(test_features.head())

#Determine the data types and missing values in the dataframes

print("--- Data Types in Training Features ---")
print(train_features.dtypes.value_counts())

print("\n--- Missing Values per Column (Training) ---")
missing_train = train_features.isnull().sum().sort_values(ascending=False)
missing_percent = (missing_train / len(train_features)) * 100
print(pd.DataFrame({'Missing Count': missing_train, 'Missing %': missing_percent}).head(15))

print("--- Target Means:")
print(train_labels[['h1n1_vaccine', 'seasonal_vaccine']].mean())

print("\n--- H1N1 Vaccine Counts ---")
print(train_labels['h1n1_vaccine'].value_counts())

print("\n--- Seasonal Vaccine Counts ---")
print(train_labels['seasonal_vaccine'].value_counts())