#Problem Definition
# Define the problem:
# Predict whether a passenger survived the Titanic disaster based on features.
objective = "Classification: Survived (Yes/No)"
success_criteria = "Accuracy > 80%"
constraints = "Limited features, missing values, imbalanced classes"
print("Objective:", objective)
print("Success Criteria:", success_criteria)
print("Constraints:", constraints)

#Data Collection, Data Cleaning & Preprocessing
#Data Collection
import pandas as pd                 # Load dataset (Titanic dataset from seaborn or CSV)
import seaborn as sns
df = sns.load_dataset("titanic")
print("Data shape:", df.shape)
print(df.head())
# Handle missing values
df['age']=df['age'].fillna(df['age'].median())
df['embarked']=df['embarked'].fillna(df['embarked'].mode()[0])
# Drop duplicates
df.drop_duplicates(inplace=True)
# Encode categorical variables
df = pd.get_dummies(df, columns=['sex','class','embarked'], drop_first=True)
# Feature engineering: family size
df['family_size'] = df['sibsp'] + df['parch']
print(df.head())

#Exploratory Data Analysis (EDA)
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of age
sns.histplot(df['age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Correlation matrix
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

#Data Modeling
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Define features and target
X = df.drop(columns=['survived'])
y = df['survived']

# Convert remaining categorical columns into numerical columns
X = pd.get_dummies(X, drop_first=True)

# Handle missing values
X = X.fillna(X.median(numeric_only=True))

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model trained successfully!")

#Model Evaluation
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
