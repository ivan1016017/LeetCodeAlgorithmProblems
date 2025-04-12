import pandas as pd
import xgboost as xgb
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.metrics import f1_score, make_scorer

# Load the dataset
train_data = pd.read_csv("train.csv")

# remove ids
train_data = train_data.drop(columns=['ID'])

# identify imbalanced dataset
train_data["Target"].value_counts()
'''
>>> train_data["Target"].value_counts()
Target
0    6420
1     316
Name: count, dtype: int64
'''


# Separate features and target
X = train_data.drop(columns=["Target"])
y = train_data["Target"]

# Initialize XGBoost model
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss")

# Define the hyperparameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.6, 0.8],
    'colsample_bytree': [0.6, 0.8]
}


# Define F1 scorer
f1_scorer = make_scorer(f1_score, pos_label=1)

# Perform 5-fold stratified cross-validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1234)
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    scoring=f1_scorer,
    cv=skf,
    verbose=1,
    n_jobs=-1
)


# Fit the grid search
grid_search.fit(X, y)

# Print the best parameters and the best F1 score
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best F1 score: {grid_search.best_score_}")

# Train the best model on the full training set
best_model = grid_search.best_estimator_
best_model.fit(X, y)