import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

scopes = ["https://www.googleapis.com/auth/spreadsheets" , "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

spreadsheet = client.open('Farm5. Айди квестов')
worksheet = spreadsheet.worksheet('Farm5')


# Fetch all the values from the worksheet
all_values = worksheet.get_all_values()

# Use the second row as the headers
headers = all_values[1]

# Use the remaining rows as the data
data = all_values[2:]

# Convert the data to a DataFrame
records_df = pd.DataFrame(data, columns=headers)

# Display the DataFrame
print(records_df)

# Save the DataFrame to an Excel file
records_df.to_excel('quest_data.xlsx', index=False)