#!/usr/bin/env python3

import sys
import json

# Read file name from command line
input_file = sys.argv[1]

# name of file to be manipulated
fh = open(input_file)

# variable for whole json structure
raw_data = json.loads(fh.read())

# Assigns date_of value and traverses jason structure
for date_of in raw_data:

# Assigns location value and traverses jason structure
    for location in raw_data[date_of]:

# Assigns serverName and status values and traverses jason structure
        for location_data in raw_data[date_of][location]:
            serverName = location_data['serverName']
            status = location_data['status']
            users = location_data['users']

# Assigns name, computerName and idNumber values
            for record in users:
                name = record['name']
                computerName = record['computerName']
                idNumber = record['idNumber']

# Assembles log_line from above variables
                log_line = json.dumps({'Date': date_of, 'Location': location, 'Server': serverName, 'Status': status, 'Name': name, 'Computer': computerName, 'Id': idNumber})

# Creates the output file and appends each line to it
                file_name_format = "{}-{}.json"
                file_name = file_name_format.format(location, date_of)
                with open(file_name, 'a+') as myfile:
                    myfile.write('%s \n' % log_line)
