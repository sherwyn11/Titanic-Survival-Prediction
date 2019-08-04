# Titanic Survival Prediction (Classification) (Model chosen - Logistic Regression)

import numpy as np
import pandas as pd

df = pd.read_csv("titanic.csv")
df.dropna()
df = df.drop(
    [
        "zero",
        "zero.1",
        "zero.2",
        "zero.3",
        "zero.4",
        "zero.5",
        "zero.6",
        "zero.7",
        "zero.8",
        "zero.9",
        "zero.10",
        "zero.11",
        "zero.1",
        "zero.1",
        "zero.1",
        "zero.1",
        "zero.1",
        "zero.1",
        "zero.12",
        "zero.13",
        "zero.14",
        "zero.15",
        "zero.16",
        "zero.17",
        "zero.18",
    ],
    axis=1,
)

from sklearn.preprocessing import LabelEncoder

X = df.iloc[:, 1:-1]
y = df.iloc[:, -1].values

X = X.apply(LabelEncoder().fit_transform)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0, solver="lbfgs",max_iter=1000, multi_class="ovr")
clf.fit(X_train, y_train)

def survival(data):
    data = pd.DataFrame(np.array(data).reshape(1,7))
    data = data.apply(LabelEncoder().fit_transform)
    lg_pred = clf.predict_proba(data)[:,1]
    return(round(lg_pred[0]*100, 3))