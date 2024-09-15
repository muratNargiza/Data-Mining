import pandas as pd
# -----------------------------------------------------------------------------
#1
import pandas as pd

data = {
    'Name': ['Nargiza', 'Madi', 'Aruzhan', 'Nargiza', 'Nargiza', 'Ers'],
    'Age': [28, 34, 28, 30, 24, 34]
}

df = pd.DataFrame(data)

print("Duplicate Rows:")
print(df[df.duplicated()])

df_cleaned = df.drop_duplicates()
print("Cleaned DataFrame:")
print(df_cleaned)

# -----------------------------------------------------------------------------

#2
import pandas as pd
from scipy import stats

data = {
    'Score': [50, 55, 60, 200, 65, 70, 75, 80, 85]
}

df = pd.DataFrame(data)

z_scores = stats.zscore(df['Score'])
abs_z_scores = abs(z_scores)
filtered_entries = (abs_z_scores < 3)
df_no_outliers = df[filtered_entries]

print("DataFrame without outliers:")
print(df_no_outliers)

# -----------------------------------------------------------------------------

#3
data = {
    'Product': ['apple', 'Banana', 'APPLE', 'bANANA', 'Orange'],
    'Category': ['Fruit', 'fruit', 'Fruit', 'Vegetable', 'fruit']
}

df = pd.DataFrame(data)

df['Product'] = df['Product'].str.lower().str.title()
df['Category'] = df['Category'].str.title()

print("Standardized DataFrame:")
print(df)
