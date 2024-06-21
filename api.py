import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets" , "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

spreadsheet = client.open('Farm5. Айди квестов')
worksheet = spreadsheet.worksheet('Farm5')

# List all worksheets in the spreadsheet
worksheet_list = spreadsheet.worksheets()
for worksheet in worksheet_list:
    print(worksheet.title)  # Print the title of each worksheet



name_column = worksheet.col_values(1)
print(name_column)