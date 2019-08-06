import csv
import json
csvfile = open('pub.csv', 'r')
jsonfile = open('pub.json', 'w')
fieldnames = ('Paper','Authors', 'Year', 'Study Area', 'Business Model', 'Method', 'Theme')
reader = csv.DictReader(csvfile, fieldnames)
out = json.dumps([row for row in reader])
jsonfile.write(out)