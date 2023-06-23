"""
Script that is responsible for reading out of actors.json and creating the two
other user-friendly formats people may find helpful. If we update actors, then
run this script, the other two files will update automagically.
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-Actor-Names
@Framework https://github.com/DougTheDruid/SoT-ESP-Framework
For community support, please contact me on Discord: dougthedruid
"""
import json
from csv import DictWriter


if __name__ == '__main__':
    # Read in our existing actors.json file
    with open("actors.json", "r") as infile:
        actors = json.load(infile)

    # Create an inverted list version and a list of dictionary for the csv
    csv_list = []
    for key, val in actors.items():
        csv_list.append({
            'Friendly Name': key,
            'Actor Name': val
        })

    # Dump the csv list to a csv file
    with open("actors.csv", "w") as outfile_csv:
        writer = DictWriter(outfile_csv,
                            fieldnames=['Friendly Name', 'Actor Name'],
                            delimiter=',', lineterminator='\n')
        writer.writeheader()
        writer.writerows(csv_list)
