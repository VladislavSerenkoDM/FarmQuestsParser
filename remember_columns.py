import gspread
from google.oauth2.service_account import Credentials
from openpyxl import Workbook

scopes = ["https://www.googleapis.com/auth/spreadsheets" , "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

spreadsheet = client.open('Farm5. Айди квестов')
worksheet = spreadsheet.worksheet('Farm5')


# Define the Master column number (1-based index)
master_column_number = 2

# Get the current state of the Master column
master_column_data = worksheet.col_values(master_column_number)

# Debug print
print(f"Initial Master Column Data: {master_column_data}")

# Save the initial state to an Excel file
wb = Workbook()
ws = wb.active
ws.title = "InitialState"
for idx, value in enumerate(master_column_data, start=1):
    ws.cell(row=idx, column=1, value=value)

wb.save("master_column_initial_state.xlsx")