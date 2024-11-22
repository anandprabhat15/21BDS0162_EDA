#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install "numpy<2"


# In[5]:


# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'D:/Customer Flight Activity.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Get the dimensions of the dataset
print("\nDataset Dimensions:")
print(data.shape)

# Get summary statistics of the dataset
print("\nSummary Statistics:")
print(data.describe(include='all'))

# Check for missing values
print("\nMissing Values in Dataset:")
print(data.isnull().sum())


# In[6]:


# Check for duplicate rows
print("\nChecking for Duplicate Rows:")
print(data.duplicated().sum())

# Drop duplicates if any
data = data.drop_duplicates()

# Handling missing values (if any exist)
# Replace missing numerical values with median and categorical values with mode
for column in data.columns:
    if data[column].dtype == 'object':  # Categorical columns
        # Use explicit reassignment for categorical columns
        data[column] = data[column].fillna(data[column].mode()[0])
    else:  # Numerical columns
        # Use explicit reassignment for numerical columns
        data[column] = data[column].fillna(data[column].median())

# Verify missing values are handled
print("\nMissing Values After Handling:")
print(data.isnull().sum())


# In[7]:


# Visualize numerical columns
numerical_cols = ['Total Flights', 'Distance', 'Points Accumulated', 'Points Redeemed', 'Dollar Cost Points Redeemed']

for col in numerical_cols:
    plt.figure(figsize=(8, 5))
    sns.histplot(data[col], kde=True, bins=30, color='blue')
    plt.title(f'Distribution of {col}')
    plt.show()

# Visualize categorical columns
categorical_cols = ['Year', 'Month']

for col in categorical_cols:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=data[col], palette='viridis')
    plt.title(f'Count of {col}')
    plt.show()


# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns

# Relationship between Distance and Points Accumulated
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x='Distance', y='Points Accumulated', hue='Year', palette='viridis')
plt.title('Distance vs Points Accumulated')
plt.show()

# Relationship between Total Flights and Points Redeemed
plt.figure(figsize=(8, 5))
sns.boxplot(data=data, x='Year', y='Points Redeemed', palette='Set2')
plt.title('Year vs Points Redeemed')
plt.show()

# Correlation Heatmap with Rotated X-Labels
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.xticks(rotation=45)  # Rotate x-axis labels by 45 degrees
plt.show()


# In[9]:


# Pairplot to visualize relationships among numerical variables
sns.pairplot(data[numerical_cols], diag_kind='kde', corner=True, palette='husl')
plt.show()

# Multivariate analysis with categorical and numerical variables
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='Year', y='Points Accumulated', hue='Month', ci=None, palette='viridis')
plt.title('Yearly Points Accumulated by Month')
plt.show()


# In[ ]:




