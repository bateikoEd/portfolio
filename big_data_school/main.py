from time import time
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report, \
                            roc_auc_score , accuracy_score, precision_score, auc, recall_score
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.ensemble import VotingClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from xgboost import XGBClassifier
import pickle

test_set_percent = 0.1

def get_score_for_model(n_splits=10):
    seed = 13

    results = []
    names = []
    scoring = 'roc_auc'

    for name, model in models:
        strat = StratifiedKFold(n_splits=n_splits, random_state=seed, shuffle=True)

        cv_results = cross_val_score(model, X_train, y_train, cv=strat, scoring=scoring, n_jobs=-1)

        results.append(cv_results)
        names.append(name)

        print(f"{name}: {cv_results.mean()} ({cv_results.std()})")

    return np.array(results)

# def append_res_to_boxplot(results, df):
#     i = 0
#     while i < len(results[0]):
#         line = []
#         for num, ml in zip(results, mod_list):
#             line.append([num[i],ml])
#
#         i = i+1
#         df = df.append(pd.DataFrame(line, columns=['Score', 'ML']),ignore_index=True)
#     return df

test_set_percent = 0.1
# test_features_30 = pd.read_csv('prepared_data/test_best_features_30.csv')
df_balanced = pd.read_csv('prepared_data/train_best_features_30_balanced.csv')

y = df_balanced['target']
X = df_balanced.drop(['target'], axis = 1)

# Spliting set
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_set_percent)

time_steart = time()
models = []
models.append(('LR', LogisticRegression()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('DecTree', DecisionTreeClassifier()))
models.append(('RF', RandomForestClassifier()))
models.append(('XGB', XGBClassifier()))
models.append(('GaussianNB', GaussianNB()))
models.append(('ada', AdaBoostClassifier()))
models.append(('SVC', SVC()))

results = get_score_for_model()
# ada_best = ada_best.fit(X_train, y_train)
# randomForest_best = randomForest_best.fit(X_train, y_train)
time_end = time()

print(f'time:\t{time_end - time_steart}')