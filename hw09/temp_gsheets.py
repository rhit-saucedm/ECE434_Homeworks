#!/usr/bin/env python3
# Based pm: https://github.com/googleworkspace/python-samples/tree/master/sheets/quickstart
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account
from w1thermsensor import W1ThermSensor
import time, sys
import os

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '10gASXOXZXoJ3USf1qOvrCkPMxhUUArt3R1MxpD4F96M'
SAMPLE_RANGE_NAME = 'A2'

temp = {}
w1_path="/sys/class/hwmon"
if (not os.path.exists(w1_path)):
    print("MAX31820 has not config yet.")

f1=open(w1_path+"/hwmon0/temp1_input", "r")
f2=open(w1_path+"/hwmon1/temp1_input", "r")
f3=open(w1_path+"/hwmon2/temp1_input", "r")

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    global service
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)

if __name__ == '__main__':
    main()
    try:
        while(True):
            try:
                for index, sensor in enumerate(W1ThermSensor.get_available_sensors(), start=0):
                    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature())) 
                    temp[index] = sensor.get_temperature()
                
                # Call the Sheets API
                sheet = service.spreadsheets()
                values = [[time.time()/60/60/24+ 25569 - 4/24, temp[0], temp[1], temp[2]]]
                body = {'values': values}
                result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, valueInputOption='USER_ENTERED', body=body).execute()
                time.sleep(1)
            except:

                print("error")
                time.sleep(0.1)

    except KeyboardInterrupt:
        f1.close()
        f2.close()
        f3.close()
# [END sheets_quickstart]