This code automates to send the birthday wishes, code checks the current date and if it matches the dates in the spreadsheet it sends out wishes in the whatsapp group 😂

Create a excel spreadsheet with Columns Name / Date of birth / Phone number or Group name

Use this script and modifiy the birthday wish as appropriate and rename the spreadsheet as required

Depending on your env setup run the script (Ex for Mac users **python birthday.py**

Set up a cron job that runs as per your specific time and code is below

1️⃣ Open the cron editor:
crontab -e

2️⃣ Add this line to run the script daily at 12 AM UK time (or 5:30 AM IST):
30 5 * * * /usr/bin/python3 /Users/shireesh.kantharaj/Documents/birthdays.py
(Replace /usr/bin/python3 with your actual Python path, check with which python3)

3️⃣ Save & Exit.

4️⃣ Verify if cron is running:
crontab -l

5️⃣ Check logs if it runs correctly:
grep CRON /var/log/syslog
