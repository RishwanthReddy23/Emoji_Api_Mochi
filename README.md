# Emoji_Api_Mochi

### Downolad .py file
##### I have Used Visual Studio Code for Execution of python code.


# Mood of the Tickets Queue

A simple internal utility for the customer service team written with **Python**,**Streamlit**, and **Google Sheets API** that is used for sharing and seeing the emotional mood of the inbound ticket queues day after day.
The home-taken experimentary is the way to create visually understandable and user-friendly data tools - with crystal clear code, and well-thought-out UX - in a few minutes.
---
# Problem Statement

The Operations team is swamped with lots of support tickets during the day, and a "vibe" often reflects on those tickets - as annoying, joyful, puzzling, etc.
This instrument permits the agents to log their vibes with emojis while the process is ongoing and, if they wish, enter an optional note, which will be stored in Google Sheet. It also shows the mood development for the day of the week so that changes and patterns of sentiments can be spotted.
---
# Setting Up Google Sheets
- Set the google sheets by defining permissions
- Download the Google Credinitials .JSON file.
- Authenticate Google API Sheets
- Nothe the google sheets ID From the top of google sheet.
- The app is programmed to look for the credentials.json file (which has your Google API credentials) in the same directory as your main script (Emoji.py) by default. If your credentials.json file is in a location other than the default, you will have If your credentials.json file is saved somewhere different, you have no other way instead of updating the file path in your code to point to that location.

---
#  Mood Logging
- Choose a predefined mood from the dropdown (`😊 😠 😕 🎉`)
- Optionally enter a small note
- The entry is still recorded with a timestamp
- Through the Sheets API, the entries are collected in **Google Sheets**

# Mood Visualization
- The number of occurrences of each mood for **Present day** is represented in a bar chart
- The visual changes in mood trends are depicted by the dynamic updates courtesy of **Plotly**
- A good and simple UI with easily understandable interactions on **Streamlit**

# Output 
- **"streamlit run Emoji.py"** Run this code in output terminal it will automatically redirect to "Streeam lit" Web Dashboard.
