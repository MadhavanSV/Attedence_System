import pandas as pd
import collections
import pickle

data = pd.read_excel("Sample.xlsx")
name = data['Name'].to_numpy()
reg_no = data['Reg no'].to_numpy()
school = data['School'].to_numpy()

teacher_mapping = collections.defaultdict(list)
attendance = collections.defaultdict(list)
for i in range(len(name)):
    teacher_mapping[reg_no[i]].append(name[i])
    teacher_mapping[reg_no[i]].append(school[i])

pickle.dump(teacher_mapping, open("teacher_mapping.pkl", "wb"))
pickle.dump(attendance, open("attendance.pkl", "wb"))
