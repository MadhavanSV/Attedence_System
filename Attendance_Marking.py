import streamlit as st
import pickle
import datetime

mapping = pickle.load(open("teacher_mapping.pkl", "rb"))
attendance = pickle.load(open("attendance.pkl", "rb"))

st.title("Attendence Marking")
reg_no = st.text_input("Enter the reg no")
submit = st.button("Submit")

if submit:
    date = str(datetime.date.today())
    if reg_no not in attendance[date]:
        attendance[date].append(reg_no)
        pickle.dump(attendance, open("attendance.pkl", "wb"))
        st.success(f"Attendance for {mapping[int(reg_no)][0]} from {mapping[int(reg_no)][1]} school  marked successfully")
    else:
        st.error('Attendance already marked', icon="🚨")
