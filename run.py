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
    print("Please enter the sales data from the last market.") #Sets instructional text
    print("The data should consist of six numbers each separated by a comma")
    print("Example: 10,15,20,25,30,35\n") #'/n' creates a new line to separate the text elements

    data_str = int(input("Enter data here:")) #Saves data input to a named variable
    print(f'The data entered is {data_str}') #Prints the variable back to terminal

get_sales_data() #Calls function