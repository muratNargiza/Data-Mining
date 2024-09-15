import pandas as pd
#1.1
df = pd.DataFrame({
    'Height': [160, 170, 180],
    'Weight': [60, 70, 80]
})

df['BMI'] = df['Weight'] / (df['Height'] / 100) ** 2
print(df)


# #1.2
# from sklearn.preprocessing import PolynomialFeatures

# df = pd.DataFrame({
#     'Feature1':[1, 2, 3],
#     'Feature2':[1, 2, 3]
# })

# poly = PolynomialFeatures(degree=2, include_bias = False)
# new_features = poly.fit_transform(df)
# print(new_features)

# -----------------------------------------------------------------------------

# #2
# df = pd.DataFrame({
#     'Date': ['2023-01-01', '2023-05-15', '2024-07-20']
# })

# df['Date'] = pd.to_datetime(df['Date'])

# df['Day_of_Week'] = df['Date'].dt.day_name()
# df['Week_of_Year'] = df['Date'].dt.isocalendar().week
# df['Is_Weekend'] = df['Date'].dt.dayofweek >= 5

# print(df)

# -----------------------------------------------------------------------------

#3
df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%H:%M').dt.time
df['End_Time'] = pd.to_datetime(df['End_Time'], format='%H:%M').dt.time

# Compute the duration between start and end times
df['Duration'] = pd.to_datetime(df['End_Time'].astype(str), format='%H:%M') - pd.to_datetime(df['Start_Time'].astype(str), format='%H:%M')
df['Duration'] = df['Duration'].dt.total_seconds() / 3600  # Convert duration to hours

# Classify times of day
def time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 24:
        return 'Evening'
    else:
        return 'Night'

df['Start_Time_Period'] = df['Start_Time'].apply(lambda x: time_of_day(x.hour))
df['End_Time_Period'] = df['End_Time'].apply(lambda x: time_of_day(x.hour))

print(df)