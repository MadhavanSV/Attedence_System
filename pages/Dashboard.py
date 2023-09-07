import plotly.express as px
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import io
import matplotlib.pyplot as plt

def to_excel(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

attendance = pickle.load(open("attendance.pkl", "rb"))
mapping = pickle.load(open("teacher_mapping.pkl", "rb"))
attendance_data = pd.read_excel("Sample.xlsx")

unique_date = list(attendance.keys())
unique_date.sort()

dates = str(st.date_input("Enter the date"))
submit = st.button("Submit")

if submit:
    reg_nos = attendance[dates]
    reg_no = []
    name = []
    school = []
    for i in reg_nos:
        reg_no.append(i)
        name.append(mapping[int(i)][0])
        school.append(mapping[int(i)][1])
    
    reg_no = np.array(reg_no)
    name = np.array(name)
    school = np.array(school)
    data = pd.DataFrame()
    data['Name'] = name
    data["Reg No"] = reg_no
    data["School"] = school
    data.sort_values(by = ['School', 'Reg No'], inplace = True)
    data.to_csv("Attendence_Details.csv")
    st.write(data)
    
    unique_schools = list(set(school))
    cnt = []
    for i in unique_schools:
        cnt.append(list(school).count(i))
    
    # st.download_button(label='Download details', data=data, file_name= 'details.xlsx')
    with open("Attendence_Details.csv", "rb") as file:
        btn = st.download_button(
            label="Download",
            data=file,
            file_name="details.csv",
            mime="text/csv"
        )
    # print(unique_schools)
    # print(cnt)
    info = {"Schools" : unique_schools, "Count" : cnt}
    info = pd.DataFrame(info)
    info = info.set_index("Schools")
    st.bar_chart(info)
    
    # fig, ax = plt.subplots()
    # ax.bar(unique_schools, cnt)
    # st.pyplot(fig)