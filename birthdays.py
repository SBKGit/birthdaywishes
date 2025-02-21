import pandas as pd
from datetime import datetime
import time
import webbrowser
import pyautogui

# Path to your Excel file
file_path = "/Users/shireesh.kantharaj/Documents/birthdays.xlsx"

# Read the Excel file
df = pd.read_excel(file_path, engine="openpyxl")

# Ensure column names are clean
df.columns = df.columns.str.strip()

# Convert 'Date of Birth' to datetime format
df["Date of Birth"] = pd.to_datetime(df["Date of Birth"], errors="coerce")

# Get today's date in MM-DD format
today = datetime.today().strftime("%m-%d")

# Open WhatsApp Web (if not already open)
webbrowser.open("https://web.whatsapp.com")
time.sleep(15)  # Give time for WhatsApp Web to load

# Loop through each row in the Excel file
for index, row in df.iterrows():
    dob = row["Date of Birth"]
    
    if pd.notna(dob):  # Check if dob is valid
        dob_str = dob.strftime("%m-%d")  # Convert to MM-DD format

        if today == dob_str:
            name = row["Name"]  # Assuming there's a 'Name' column
            group_name = row["Group Name"]  # Read the group name from the Excel file
            
            if pd.isna(group_name) or group_name.strip() == "":
                print(f"⚠️ No group name found for {name}, skipping...")
                continue  # Skip if no group name is provided

            message = f"🎉 Happy Birthday, {name}..!!! 🎂🎈🎁 Have an amazing day & a Fantastic year ahead..!! 🥳"

            try:
                # Open WhatsApp Group by Searching
                pyautogui.click(200, 200)  # Click on search bar (Adjust coordinates if needed)
                time.sleep(1)
                pyautogui.typewrite(group_name)
                time.sleep(1)
                pyautogui.press("enter")
                time.sleep(3)  # Wait for the group chat to open

                # Type the birthday message
                pyautogui.typewrite(message)
                time.sleep(1)

                # Press Enter to send
                pyautogui.press("enter")

                print(f"✅ Birthday wish sent to {name} in {group_name}!")

                time.sleep(5)  # Wait before sending the next message

            except Exception as e:
                print(f"❌ Failed to send message to {name}: {e}")
