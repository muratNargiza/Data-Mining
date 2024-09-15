#1
# from sklearn.preprocessing import StandardScaler
# import pandas as pd

# data = pd.DataFrame({
#     'price': [1000, 1500, 2000, 2500, 3000]
# })

# scaler = StandardScaler()

# data[['price']] = scaler.fit_transform(data[['price']])
# print(data)

# -----------------------------------------------------------------------------

#2
import pandas as pd

data = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'C'],
    'Value': [1, 2, 3, 4]
})

encoded_data = pd.get_dummies(data, columns=['Category'])
print(encoded_data)

# -----------------------------------------------------------------------------
#3

import pandas as pd

# Sample data
data = pd.DataFrame({
    'Temperature': [32, 45, 50, 65, 70, 85, 90]
})

# Define quantiles for binning
data['Temp_Group'] = pd.qcut(data['Temperature'], q=4, labels=['Very Cold', 'Cold', 'Warm', 'Hot'])
print(data)

