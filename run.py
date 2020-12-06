#! /usr/bin/env python
from colorama import init
from datetime import datetime
from covid import Covid
import os

def place_value(number):
    return ("{:,}".format(number))

def main():
    init()
    # Capture time
    time_of_now = datetime.now()
    querytime = f"{time_of_now.day} {time_of_now.strftime('%b')} {time_of_now.year} [{time_of_now.hour}:{time_of_now.minute}:{time_of_now.second}]"

    # Load coronavirus data
    covid = Covid(source="worldometers")
    usa_cases = covid.get_status_by_country_name('usa')
    world_cases = {}
    world_cases['confirmed'] = place_value(covid.get_total_confirmed_cases())
    world_cases['deaths'] = place_value(covid.get_total_deaths())
    world_cases['active'] = place_value(covid.get_total_active_cases())
    world_cases['recovered'] = place_value(covid.get_total_recovered())

    # Manage the data for printing to shell
    color_map = {'confirmed': 34, 'deaths': 31, 'active': 33, 'recovered': 32} # Set the Colorama color codes for stats
    stat_list = ['confirmed', 'deaths', 'active', 'recovered']

    # Print data to shell
    os.system('clear')
    print('\033[36m' + "#".center(80, "#"))
    print("     US | GLOBAL COVID STATISTICS     ".center(80, "#"))
    print("#".center(80, "#"))
    print("")
    for i in stat_list:
        print(f'\033[{color_map[i]}m' + f"{i}".upper().center(80, " "))
        print(f"{place_value(usa_cases[i])} | {world_cases[i]}".center(80, " "))
        print("")
    print('\033[39m') # Reset text color
    print(f"Source: Worldometers ({querytime})".rjust(80, " "))


if __name__ == '__main__':
    main()
