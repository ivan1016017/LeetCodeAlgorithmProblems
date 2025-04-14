import pandas as pd

# Read the dataset
data = pd.read_csv("data.csv")

# Check the dtypes
data.dtypes
'''
>>> data.dtypes
order_id     object
date         object
revenue     float64
dtype: object
'''

# Compute cap & floor at 1% and 99% for revenue
quantiles = data['revenue'].quantile([0.01, 0.99])
lower_bound = quantiles.loc[0.01]
upper_bound = quantiles.loc[0.99]

# Get the minimum and maximum values of revenue
min_value = data['revenue'].min()
max_value = data['revenue'].max()

# Replace outliers in revenue
solution = data.copy(deep=True)
solution['revenue'] = solution['revenue'].apply(
    lambda x: min_value if x < lower_bound else max_value if x > upper_bound else x
)

# Write submission
solution.to_csv("submission.csv", index=False)