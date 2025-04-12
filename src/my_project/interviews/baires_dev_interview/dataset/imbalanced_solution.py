import pandas as pd
import xgboost as xgb
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.metrics import f1_score, make_scorer
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

# Set the seed
seed = 1234

# Load the dataset
train_data = pd.read_csv("train.csv")

# Remove IDs
train_data = train_data.drop(columns=['ID'])

# Identify imbalanced dataset
train_data["Target"].value_counts()
'''
>>> train_data["Target"].value_counts()
Target
0    6420
1     316
Name: count, dtype: int64
'''

# Impute missing values with the mean
imputer = SimpleImputer(strategy='mean')
train_data.iloc[:, :] = imputer.fit_transform(train_data)

# Separate features and target
X = train_data.drop(columns=["Target"])
y = train_data["Target"]

# Define the XGBoost model
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss")

# Define the hyperparameter grid
param_grid = {
    'model__subsample': [0.6, 0.8],
    'model__colsample_bytree': [0.6, 0.8],
    'model__n_estimators': [50, 100, 200],
    'model__max_depth': [3, 5, 7],
    'model__learning_rate': [0.01, 0.1, 0.2]    
}

# Define F1 scorer
f1_scorer = make_scorer(f1_score, pos_label=1)

# Create a pipeline with SMOTE and the XGBoost model
pipeline = Pipeline([
    ('smote', SMOTE(random_state=seed)),
    ('model', model)
])

# Perform 5-fold stratified cross-validation with grid search
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    scoring=f1_scorer,
    cv=skf,
    verbose=1,
    n_jobs=-1
)

# Fit the grid search
grid_search.fit(X, y)

# Print the best parameters and the best F1 score
print("Best parameters: {}".format(grid_search.best_params_))
print("Best F1 score: {}".format(grid_search.best_score_))

score = 100*grid_search.best_score_
'''
This is the solution you are lookin at since test.csv does not have 
Target column
'''
print('Solution: {}'.format(score))

# Train the best model on the full training set
best_model = grid_search.best_estimator_
best_model.fit(X, y)

# Load the test dataset
test_data = pd.read_csv("test.csv")

# Remove the 'ID' column
test_ids = test_data['ID']  # Save the IDs for the output file
test_data = test_data.drop(columns=['ID'])

# Predict using the trained model
predictions = best_model.predict(test_data)

# Create a DataFrame for the predictions
output = pd.DataFrame({
    'ID': test_ids,
    'Target': predictions
})

# Save the predictions to a CSV file
output.to_csv("predictions.csv", index=False)

print("Predictions saved to predictions.csv")

