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

# Exclude non-float64 columns
numerical_columns = data.columns.difference(['date', 'order_id'])

# Compute cap & floor at 1% and 99% respectively
quantiles = data[numerical_columns].quantile([0.01, 0.99])

# Create solution dataframe
solution = data.copy(deep=True)

# Replace outliers 
for col in numerical_columns:
    upper_bound = quantiles.loc[0.99, col]
    lower_bound = quantiles.loc[0.01, col]
    solution[col] = data[col].clip(lower=lower_bound, 
                                   upper=upper_bound)



# Write submission
solution.to_csv("submission.csv", index=False)

