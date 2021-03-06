"""
Imports entire gspread library & imports Credentials class which is
part of the service account function from the Google auth library                                                                                                                                                                                                                                                                                                                                                                    of the service account function
"""
import gspread
from google.oauth2.service_account import Credentials

"""
Section sets the constants (note the UPPERCASE) names requires to access
the spreadsheet data 

SCOPE lists the APIs that the program accesses to run
CREDS calls the Credentials class from service account file & 
passes it the creds.json filename
SCOPED_CREDS uses the with_scopes method of the Crtedentials 
class to pass it the SCOPE constant
GSPREAD_CLIENT  uses the gspread_autorize method & is passed the
SCOPED_CREDS variable
SHEET uses the open method and the client object to access the 
specified sheet
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from user
    """
    while True:
        print("Please enter the sales data from the last market\n") #Sets instructional text
        print("The data should consist of six numbers each separated by a comma")
        print("Example: 10,15,20,25,30,35\n") #'/n' creates a new line to separate the text elements

        data_str = (input("Enter data here:\n")) #Saves data input to a named variable
        sales_data = data_str.split(",") #Splits data at commas
        

        if validate_data(sales_data): #calls the function validate_data passes sales_data
            print('Data is valid!\n') #runs only if True received from validate_data
            break #while loop then stopped
    
    return sales_data #returns the entered user data from the function

def validate_data(values):
    """
    Inside the try, converts all string values to integers
    Raises a ValueError if strings cannot be converted to int 
    i.e text entries or if there aren't exactly 6 values
    """
    try:
        [int(value) for value in values] #list comprehension looping through values 
        if len(values) != 6: #if lenth of string is not 6 raise ValueError prints length
            raise ValueError(f'Exactly 6 values are required: you only provided {len(values)}')

    except  ValueError as e: #if another error (not ValueError) set it as var e
        print(f'Invalid data: {e}, please try again\n') #print the error to terminal
        return False #triggers loop to reenter data due to error
    
    return True #exits lopp to reenter data - no error on data entry

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with list data provided.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet('sales') #access sales worksheet
    sales_worksheet.append_row(data) #adds new row to end of sheet with user sales data
    print("Sales worksheet updated successfully!\n")


data = get_sales_data() #var variable to store data returned by user
sales_data = [int(num) for num in data] #list comprehenstion converting num in data var to int
update_sales_worksheet(sales_data) #calls function update_sales and passes in the sales_data
