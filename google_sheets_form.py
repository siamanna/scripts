import gspread
from google.oauth2.service_account import Credentials

# Define the scope for the Google API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Path to your service account key JSON file
SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'

# Authenticate and initialize the Google Sheets client
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)

# Open the Google Sheet (replace 'Your Sheet Name' with the actual name of your sheet)
sheet = client.open('Your Sheet Name').sheet1

# Function to process form data
def add_form_data(data):
    """
    Adds a row of form data to the Google Sheet.

    :param data: A list of strings representing form responses.
    """
    sheet.append_row(data)
    print(f"Data added: {data}")

# Example form response data (Replace with your actual form data)
# Each list entry corresponds to a column in the sheet
form_data = [
    "John Doe",   # Name
    "johndoe@example.com",  # Email
    "Positive Feedback",    # Feedback
    "2024-11-24"  # Date (optional or dynamic)
]

# Add the form data to the sheet
add_form_data(form_data)
