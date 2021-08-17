import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

data = pd.read_csv("DepressionSurveyResponses.csv")
print(data.head())

print(data.isnull().sum())

features = data[["Age", "Occupation", "Family member with depression", "Question1", "Question2", "Question3", "Question4", "Question5", "Question6", "Question7", "Question8"]]
target = data['Result']
print(features.head())
print(target.head())

new_features = pd.get_dummies(features)
print(new_features.head())

new_features.drop(["Family member with depression_No", "Question1_No", "Question2_No", "Question3_No", "Question4_No", "Question5_No", "Question6_No", "Question7_No", "Question8_No"], axis=1, inplace=True)
print(new_features.head())

x_train, x_test, y_train, y_test = train_test_split(new_features, target, random_state=15)

model = RandomForestClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
cr = classification_report(y_test, y_pred)
print(cr)

with open("depression_predict.model", "wb") as f:
	pickle.dump(model, f)