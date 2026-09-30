# 💉 Flu Shot Learning: Predict H1N1 and Seasonal Vaccines

A machine learning project based on the **DrivenData Flu Shot Learning competition**, focused on predicting whether survey respondents received the **H1N1 flu vaccine** and the **seasonal flu vaccine**.

🔗 **Competition:** [DrivenData — Flu Shot Learning](https://www.drivendata.org/competitions/66/flu-shot-learning/)

---

## 🎯 Problem Statement

The goal of this project is to use responses from the **National 2009 H1N1 Flu Survey** to predict vaccination behavior.

For each respondent, the model predicts two binary outcomes:

* 💉 **H1N1 vaccine** — whether the respondent received the H1N1 flu vaccine
* 💉 **Seasonal vaccine** — whether the respondent received the seasonal flu vaccine

This is a **multi-label binary classification problem**, where each respondent has two target variables.

---

## 📏 Evaluation Metric

The competition evaluates predictions using the **Mean ROC AUC** across the two target variables:

* `h1n1_vaccine`
* `seasonal_vaccine`

The final score is calculated as:

**Mean AUC = (H1N1 AUC + Seasonal AUC) / 2**

ROC AUC measures how effectively a model distinguishes between the positive and negative classes across different classification thresholds.

---

## 📊 Dataset

The dataset is derived from the **National 2009 H1N1 Flu Survey**.

### Dataset dimensions

| Dataset           |   Rows | Columns |
| ----------------- | -----: | ------: |
| Training Features | 26,707 |      36 |
| Training Labels   | 26,707 |       3 |
| Test Features     | 26,708 |      36 |

The training labels contain:

* `respondent_id`
* `h1n1_vaccine`
* `seasonal_vaccine`

The feature dataset contains approximately **35 survey-based features**, covering areas such as:

* Demographics
* Health behaviors
* Medical history
* Doctor recommendations
* Vaccine concerns
* Vaccine effectiveness opinions
* Employment information
* Health insurance
* Household characteristics

> **Note:** Competition data files are not included in this repository. They can be downloaded from the official competition page.

🔗 [Download the competition dataset](https://www.drivendata.org/competitions/66/flu-shot-learning/)

---

# 🧪 Project Workflow

## 1️⃣ Data Loading & Inspection

The first stage focuses on understanding the structure and quality of the dataset.

### Tasks performed

* Loaded training features, training labels, and test features
* Checked dataset dimensions
* Verified respondent ID alignment
* Inspected data types
* Examined missing values
* Investigated target distributions
* Identified highly incomplete features

### Important observations

Three features contain approximately **50% missing values**:

* `employment_occupation`
* `employment_industry`
* `health_insurance`

The target variables are also imbalanced:

* `h1n1_vaccine` → approximately **21% vaccinated**
* `seasonal_vaccine` → approximately **47% vaccinated**

Understanding these characteristics is important before building the machine learning pipeline.

---

## 2️⃣ Exploratory Data Analysis

The EDA stage investigates relationships between survey responses and vaccination behavior.

### Planned analysis

Visualizations and statistical analysis will be used to investigate vaccination rates according to:

* Doctor recommendations
* Vaccine concern levels
* Vaccine effectiveness opinions
* Age groups
* Health behaviors
* Previous vaccination behavior
* Demographic characteristics

The relationship between the two target variables will also be examined to determine whether receiving one vaccine is associated with receiving the other.

---

## 3️⃣ Data Preprocessing

The preprocessing pipeline will prepare the categorical survey data for machine learning.

### Planned preprocessing steps

1. Identify columns with excessive missing values
2. Handle missing values in the remaining features
3. Encode categorical variables using **One-Hot Encoding**
4. Preserve numerical features where applicable
5. Build preprocessing using a **scikit-learn Pipeline**
6. Ensure preprocessing is fitted only on the training data to avoid data leakage

Using a pipeline allows preprocessing and model training to be handled consistently during validation and prediction.

---

## 4️⃣ Machine Learning Models

Several classification approaches will be explored.

### Baseline Model

**Logistic Regression**

A logistic regression model will provide an interpretable baseline for comparison.

The multi-target nature of the problem will be handled using:

`MultiOutputClassifier`

### Additional Models

The project will also investigate:

* Random Forest
* Gradient Boosting
* Other suitable tree-based models

Hyperparameter optimization will be performed using:

`GridSearchCV`

Model performance will be compared using ROC AUC.

---

## 5️⃣ Model Evaluation

Models will be evaluated separately for both prediction targets.

| Model               | H1N1 AUC | Seasonal AUC | Mean AUC |
| ------------------- | -------: | -----------: | -------: |
| Logistic Regression |        — |            — |        — |
| Random Forest       |        — |            — |        — |
| Gradient Boosting   |        — |            — |        — |

The final table will be updated as models are trained and evaluated.

---

## 6️⃣ Prediction & Submission

The final model will generate **probability predictions** rather than simple class labels.

The submission will contain predicted probabilities for:

* `h1n1_vaccine`
* `seasonal_vaccine`

These predictions can then be formatted according to the DrivenData competition requirements and submitted to the leaderboard.

---

# 📁 Repository Structure

```text
flu-shot-learning-h1n1/
│
├── exploration.py
│   └── Step 1: Load and inspect the dataset
│
├── eda.py
│   └── Step 2: Exploratory data analysis
│
├── preprocessing.py
│   └── Step 3: Data preprocessing and feature engineering
│
├── modeling.py
│   └── Step 4: Model training and evaluation
│
├── submission.py
│   └── Step 5: Generate competition predictions
│
├── .gitignore
│
└── README.md
```

---

# 🛠️ Technologies & Libraries

This project uses **Python** and common data science / machine learning libraries.

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn

### Visualization

* Matplotlib
* Seaborn

### Key Machine Learning Concepts

* Binary classification
* Multi-label classification
* Missing-value handling
* One-hot encoding
* Feature preprocessing
* Train/validation splitting
* ROC AUC
* Logistic Regression
* Random Forest
* Gradient Boosting
* Hyperparameter tuning
* Machine learning pipelines

---

# ⚙️ Setup

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd flu-shot-learning-h1n1
```

## 2. Install dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## 3. Download the competition dataset

Download the required CSV files from the official DrivenData competition page.

Place them inside the project directory according to the file paths expected by the scripts.

## 4. Run the data inspection script

```bash
python exploration.py
```

---

# 📈 Results

Model performance will be evaluated using ROC AUC.

The results table will be updated as different models are trained and compared.

| Model               | H1N1 ROC AUC | Seasonal ROC AUC | Mean ROC AUC |
| ------------------- | -----------: | ---------------: | -----------: |
| Logistic Regression |          TBD |              TBD |          TBD |
| Random Forest       |          TBD |              TBD |          TBD |
| Gradient Boosting   |          TBD |              TBD |          TBD |

> **Note:** Results will be added after completing model training and validation.

---

# 🔍 Key Learning Outcomes

Through this project, I am practicing:

* Working with real-world survey data
* Identifying and handling missing data
* Exploratory data analysis
* Categorical feature encoding
* Building reproducible preprocessing pipelines
* Multi-target classification
* Model comparison
* ROC AUC evaluation
* Hyperparameter tuning
* Generating probability-based predictions
* Preparing machine learning solutions for a real-world competition

---

# 🚀 Future Improvements

Possible future extensions include:

* Advanced feature engineering
* Improved missing-value strategies
* Additional classification algorithms
* Cross-validation
* Hyperparameter optimization
* Class-imbalance analysis
* Feature importance analysis
* Model interpretability using SHAP
* Experiment tracking
* DrivenData leaderboard submission

---

# 🔗 References

* [DrivenData — Flu Shot Learning Competition](https://www.drivendata.org/competitions/66/flu-shot-learning/)
* [DrivenData Benchmark Notebook](https://www.drivendata.org/competitions/66/flu-shot-learning/page/211/)
* National 2009 H1N1 Flu Survey dataset provided through the competition

---

# 📝 License

This project is intended for **educational and portfolio purposes**.

The dataset is provided by **DrivenData** and originates from the **CDC's National 2009 H1N1 Flu Survey**. Please refer to the competition's official terms and data-use requirements for dataset-specific licensing and usage information.
