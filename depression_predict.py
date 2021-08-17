import pickle

with open("depression_predict.model", "rb") as f:
	model = pickle.load(f)

age = int(input("Enter your age: "))
o1 = int(input("Buisiness (0 for no and 1 for yes): "))
o2 = int(input("Working (0 for no and 1 for yes): "))
o3 = int(input("Student (0 for no and 1 for yes): "))
o4 = int(input("Unemployed (0 for no and 1 for yes): "))
o5 = int(input("Housewife (0 for no and 1 for yes): "))
fm = int(input("Any family member with depression? (0 for no and 1 for yes): "))
q1 = int(input("1) Do you have little pleasure or interest in doing things? (0 for no and 1 for yes): "))
q2 = int(input("2) Do you feel hopeless or down? (0 for no and 1 for yes): "))
q3 = int(input("3) Do you have trouble sleeping, either sleeping too much or not at all? (0 for no and 1 for yes): "))
q4 = int(input("4) Do you feel tired or have little energy? (0 for no and 1 for yes): "))
q5 = int(input("5) Do you overeat or have a poor appetite? (0 for no and 1 for yes): "))
q6 = int(input("6) Do you feel like a failure or you've let people down? (0 for no and 1 for yes): "))
q7 = int(input("7) Do you have trouble concentrating? (0 for no and 1 for yes): "))
q8 = int(input("8) Do you have any harmful thoughts towards yourself? (0 for no and 1 for yes): "))

d = [[age, o1, o2, o3, o4, o5, fm, q1, q2, q3, q4, q5, q6, q7, q8]]
res = model.predict(d)
print(res)