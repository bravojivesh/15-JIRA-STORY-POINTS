import csv
import pandas

with open ("test.csv") as data:
    content= csv.reader(data)
    for column in content:
        x=column[9]
        print (x)


