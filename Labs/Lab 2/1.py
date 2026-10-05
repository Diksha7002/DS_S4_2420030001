#A)Handling Missing Values
#1.Mean/Median/Mode Imputation
import pandas as pd
import numpy as np
#Sample dataset
df=pd.DataFrame({ 'Age':[25,30,np.nan,40,35],
                 'Department':['HR','Finance','Finance',np.nan,'IT']})
#Display Original Dataset
print("Original Dataset (with Missing Values):")
print(df)
#Mean for numeric
df['Age']=df['Age'].fillna(df['Age'].mean())
#Mode for categorical
df['Department']=df['Department'].fillna(df['Department'].mode()[0])
print(df)

print("\n\n")

#2.Forward/Backward Fill
import pandas as pd
import numpy as np
df=pd.DataFrame({ 'Age':[25,30,np.nan,40,35],
                    'Department':['HR','Finance','Finance',np.nan,'IT']})
#Display Original Dataset
print("Original Dataset (with Missing Values):")
print(df)
#Forward Fill
df_ffill=df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)
#Backward Fill
df_bfill=df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)

print("\n\n")

#3.Deletion(drop rows/columns)
import pandas as pd
import numpy as np
df=pd.DataFrame({ 'Age':[25,30,np.nan,40,35],
                    'Department':['HR','Finance','Finance',np.nan,'IT']})
#Display Original Dataset
print("Original Dataset (with Missing Values):")
print(df)
#Drop rows with missing values
df_drop_rows=df.dropna()
print("After Dropping rows:\n",df_drop_rows)
#Drop columns with missing values
df_drop_columns=df.dropna(axis=1)
print("After Dropping columns:\n",df_drop_columns)

print("\n\n")

#4a.Removing Duplicates
import pandas as pd
#Sample dataset with duplicates
df=pd .DataFrame({
    'ID':[1,2,2,3,4,4],
    'Name':['Alice','Bob','Bob','Charlie','David','David'],
    'Age':[25,30,30,35,40,40]
})
print("Original Data:\n",df)
#Remove exact duplicates 
df_exact=df.drop_duplicates()
print("\nAfter Exact Match Removal:\n",df_exact)

print("\n\n")

#4b.Removing Duplicates (Subset-Based Removal)
import pandas as pd
#Sample dataset with duplicates
df=pd .DataFrame({
    'ID':[1,2,2,3,4,4,5],
    'Name':['Alice','Bob','Bob','Charlie','David','David','David'],
    'Age':[25,30,30,35,40,40,40]
})
print("Original Data:\n",df)
#Remove duplicates based only on 'ID'
df_subset_id=df.drop_duplicates(subset='ID')
print("\nAfter Subset-Based Removal (ID):\n",df_subset_id)
#Remove duplicates based only on 'Name'
df_subset_name=df.drop_duplicates(subset='Name')
print("\nAfter Subset-Based Removal (Name):\n",df_subset_name)

print("\n\n")

#4c.Removing Duplicates (Correcting Inconsistent Formats)
#4.c.a Date Standardization(ISO 8601 Format)
import pandas as pd
#Sample dataset with inconsistent date formats
df=pd.DataFrame({
    'Date':['2025-01-05','05/01/2025','Jan 5,2025','2025.01.05'],
})
print("Original Data:\n",df)
#Convert all dates to standard ISO format (YYYY-MM-DD)
df['Date']=pd.to_datetime(df['Date'],errors='coerce').dt.strftime('%Y-%m-%d')
print(df)

print("\n\n")

#4c.Removing Duplicates (Correcting Inconsistent Formats)
#4c.b Case Normalization(Lowercase/Uppercase)
#sample dataset with inconsistent case formats
import pandas as pd
df=pd.DataFrame({
    'Name':['Alice','BOB','charlie','DAVID']
})
print("Original Data:\n",df)
#convert all names to lowercase
df['Name_lower']=df['Name'].str.lower()
#Convert all names to uppercase
df['Name_upper']=df['Name'].str.upper()
print("\n",df)

