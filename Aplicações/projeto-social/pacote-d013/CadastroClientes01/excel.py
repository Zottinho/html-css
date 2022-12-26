#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib  joga no terminal pra ele instalar
        
    #=================    ===============================================
        # ADICIONAR EDITAR INFORMAÇÕES
        #https://developers.google.com/sheets/api/guides/values#python
  
        
 # =    ===========================================================================
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#tipo de autorização das planilhas mudar de .readonly no final
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ICCky1a05xIrwUZqzhv-1lHx2FXJo5Wm45dDmoQiyY8'
SAMPLE_RANGE_NAME = 'Página1!A1:Z1000'


def main():
   #creds é de credenciais.
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
#------------------ login -----------------------
    try:
        service = build('sheets', 'v4', credentials=creds)

        # LER INFORMAÇÕES DO GOOGLE SHEETS
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                     range=SAMPLE_RANGE_NAME).execute()
        
        valores = result['values']
        print(valores)
        
    
 #----------------------------------------------------------       
  
        valores_adicionar = [
            ["tamo",'23122','3123213223'],
            ['=sajdjkçççççççççççççççççççs'],
        ]
        
        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                       range="A3", valueInputOption="USER_ENTERED", 
                                       body={'values': valores_adicionar}).execute()
        
       
    except HttpError as err:
            print(err)
      
if __name__ == '__main__':
        main()    