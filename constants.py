# Constant variables, helpers and helper methods
# Created by: Sean Lim
#

import time
import datetime

### Constant variables ###
MAIN_MENU = """\

████████▄     ▄████████ ███▄▄▄▄      ▄█   ▄█▄ ▀█████████▄   ▄█     ▄█   ▄█▄    ▄████████  ▄███████▄
███   ▀███   ███    ███ ███▀▀▀██▄   ███ ▄███▀   ███    ███ ███    ███ ▄███▀   ███    ███ ██▀     ▄██
███    ███   ███    ███ ███   ███   ███▐██▀     ███    ███ ███▌   ███▐██▀     ███    █▀        ▄███▀
███    ███   ███    ███ ███   ███  ▄█████▀     ▄███▄▄▄██▀  ███▌  ▄█████▀     ▄███▄▄▄      ▀█▀▄███▀▄▄
███    ███ ▀███████████ ███   ███ ▀▀█████▄    ▀▀███▀▀▀██▄  ███▌ ▀▀█████▄    ▀▀███▀▀▀       ▄███▀   ▀
███    ███   ███    ███ ███   ███   ███▐██▄     ███    ██▄ ███    ███▐██▄     ███    █▄  ▄███▀
███   ▄███   ███    ███ ███   ███   ███ ▀███▄   ███    ███ ███    ███ ▀███▄   ███    ███ ███▄     ▄█
████████▀    ███    █▀   ▀█   █▀    ███   ▀█▀ ▄█████████▀  █▀     ███   ▀█▀   ██████████  ▀████████▀
                                    ▀                             ▀
======================================================
ADMIN MENU
======================================================
[1] Read bicycle info from file
[2] Display all bicycle info with servicing indication
[3] Display selected bicycle info
[4] Add a bicycle
[5] Perform bicycle maintenance

======================================================
RIDER MENU
======================================================
[6]  Ride a bicycle

Input 0 to exit

------------------------------------------------------
Enter your option: \
"""
DISP_BIKE_INFO_HEAD = """
Bike No. Purchase Date  Batt % Last Maintenance KM Since Last  Service?
-------- -------------  ------ ---------------- -------------  --------"""
DISP_BIKE_RIDE_INFO_HEAD = """
Bike No. Ride duration  Ride distance Battery %
-------- -------------  ------------- ---------"""
MANTAIN_BIKE_HEADER = """
Bike No. Batt % Last Maintenance KM since Last Reason/s
-------- ------ ---------------- ------------- ---------"""
OPTION_MSG = {
              0 : 'EXIT - Bye bye!',
              1 : 'Read bicycle info from file',
              2 : 'Display all bicycle info with servicing indication',
              3 : 'Display selected bicycle info',
              4 : 'Add a bicycle',
              5 : 'Perform bicycle maintenance'
              }
# Error messages
ERROR_no_data = "No data - enter csv file name in option 1 first!"
ERROR_invalid_input = "Please Enter a valid input..."
ERROR_invalid = lambda x: f'Invalid {x}.'

### Helper methods ###
def display_OptionPickedMessage(option, instructions):
    print(f'\nOption {option}: {instructions}')

getDataFrom = lambda fileName:[i for i in open(f'./data/{fileName}',"r")][1:]
dateObjectFrom = lambda dateStr : datetime.date(*map(int,reversed(dateStr.split('/'))))

# Table formatting
FORMAT_ride_history_table = lambda i: f'{i[0]:<9}{i[1]+"sec":<15}{i[2]+"km":<14}{i[3]}'
FORMAT_main_display_table = lambda i: f'{i.bikeNumber:<9}{i.purchaseDate:<15}{i.batteryPercentage:<7}{i.lastMaintenance:<17}{i.kmSinceLast:<15}{i.needsService:<8}'
FORMAT_maintenance_table = lambda i: f'{i.bikeNumber:<9}{i.batteryPercentage:<7}{i.lastMaintenance:<17}{i.kmSinceLast:<14}{i.service_information_string:<9}'