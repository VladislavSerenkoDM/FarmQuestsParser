import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

scopes = ["https://www.googleapis.com/auth/spreadsheets" , "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

spreadsheet = client.open('Farm5. Айди квестов')
worksheet = spreadsheet.worksheet('Farm5')


# Get all the records of the data
records_data = worksheet.get_all_records()

# Convert the json to dataframe
records_df = pd.DataFrame.from_dict(records_data)

# Display the dataframe
print(records_df)

# Save the dataframe to an Excel file
records_df.to_excel('quest_data.xlsx', index=False)