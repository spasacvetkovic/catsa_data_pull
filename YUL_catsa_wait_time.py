"""
Script Comment


"""
# Python Libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
import time
import os
# ----------------------------- Airport 3
# Local Variables - YUL
v_airline_code = "YUL"
v_airline_name = "Montreal-Trudeau International Airport"
v_bound = "Departure"
quote_page = 'https://www.catsa-acsta.gc.ca/en/airport/montreal-trudeau-international-airport'

timestr = time.strftime("%Y%m%d_%H%M%S")
# print (timestr)
# print('yyz_wait_time_' + timestr +'.csv')
v_file = v_airline_code + '_catsa_wait_time_' + timestr + '.csv'
v_ola_path = 'OLA'
v_file_name = os.path.join(v_ola_path,v_file)

# Processing
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")
# print(soup.find("table", attrs={"class": "views-table"}).find("th").text)

# Writing to File
with open(v_file_name, 'w', newline='') as f1:
    columnTitleRow = "Airport Code, Airport Name, Terminal, Bound, Flight Sector,Check Point, Wait Time\n"
    f1.write(columnTitleRow)
    for tr in soup.find_all('tr')[1:]: # Zapaz: Samo jedan prazan red !!!
        tds = tr.find_all('td')
        row = v_airline_code + "," + v_airline_name + "," + " " + "," + v_bound + "," + " " + "," + tds[0].text.strip() + "," + tds[1].text.strip() + "\n"
        f1.write(row)
