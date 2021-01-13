import streamlit as st
import pandas as pd 
# from db_fxns import * 
import streamlit.components.v1 as stc



# Data Viz Pkgs
import plotly.express as px 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">ToDo App (CRUD)</h1>
    <p style="color:white;text-align:center;">Built with Streamlit</p>
    </div>
    """


def main():
	stc.html(HTML_BANNER)


	menu = ["Create","Read","Update","Delete","About"]
	choice = st.sidebar.selectbox("Menu",menu)
	

	if choice == "Create":
		st.subheader("Add Item")
		col1,col2 = st.beta_columns(2)
		
		with col1:
			task = st.text_area("Task To Do")

		with col2:
			task_status = st.selectbox("Status",["ToDo","Doing","Done"])
			task_due_date = st.date_input("Due Date")

		if st.button("Add Task"):
			add_data(task,task_status,task_due_date)
			st.success("Added ::{} ::To Task".format(task))


	elif choice == "Read":
		st.subheader("View Items")


	elif choice == "Update":
		st.subheader("Update")


	elif choice == "Delete":
		st.subheader("Delete")
		

	else:
		st.subheader("About ToDo List App")



if __name__ == '__main__':
	main()

