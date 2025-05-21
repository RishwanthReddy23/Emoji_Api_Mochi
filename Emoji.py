import streamlit as st  # Streamlit is used for building web UI from Python
import gspread  # Used for Google Sheets API library
from oauth2client.service_account import ServiceAccountCredentials # Authentication for Sheets

import plotly.express as px  #Used for Plotting Graphs
from datetime import datetime  # Used to record time stamps
import pandas as pd


### Settingup Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"] # definining permissions
Sheet_dtls =  ServiceAccountCredentials.from_json_keyfile_name("/Users/bobby/Downloads/mochi-health-460402-1f7f8b52efdc.json", scope) # Reading the service account details
client = gspread.authorize(Sheet_dtls) # Google API sheets API Authentication
sheet = client.open_by_key("1xozTA1r2Ync6vzPRvWLbwroiZtVIPKiVU-H7SlOKZFE").sheet1 # Reading the Google sheet by its ID


### Streamlit User interface
st.title("Ticket Mood-Board") #Adding Title For the Page
Mood = st.selectbox("Select the mood Type:", ["😊 Happy", "😕 Confused", "🎉 Celebratory","😠 Frustrated"]) # Mood selection using emoji buttons.
Additional_Notes = st.text_input("Comments") # In-putting any Additional Note.


### Submission button
if st.button("Submit"):
    Time_Stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Generating the Present time 
    sheet.append_row([Time_Stamp, Mood, Additional_Notes])  # Adding the Logged mood to Google sheets
    st.success("Ticket Mood logged successfully!👍") #Submission Prompt

    # st.subheader("Ticket Mood Summary")
    # x_column = st.selectbox(mood_counts)


### Visualisation
data = sheet.get_all_records() # Getting comple data 


if data: # Visulise the summary if todays data has been logged.
    Mood_df = pd.DataFrame(data) # Converting Json data to Dataframe
    Mood_df['Date'] = pd.to_datetime(Mood_df['Time_Stamp']) # Taking out only date to "date" column from complete time Stamp
    
    Present_date = datetime.now().date() #Filtering only todays date for visualisation
    Todays_data = Mood_df[Mood_df['Date'].dt.date == Present_date]

    if not Todays_data.empty:
        Total_Mood_Counts = Todays_data['Mood'].value_counts().reset_index() #Grouping and counting the Mood counts
        Total_Mood_Counts.columns = ['Mood', 'Count'] 
        
        st.subheader("Summary of Today's Ticket Mood") #Plotting the Graph
        fig = px.bar(Total_Mood_Counts, x='Mood', y='Count', color='Mood') # Selecting column Axis
        st.plotly_chart(fig)
    else:
        st.info("Today there are no Ticket Mood Logs.")
else:
    st.info("Data Un-available !")