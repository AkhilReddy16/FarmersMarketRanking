#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter=';') #intitailizing reader object and saperating coloumns data.
    
output = {} #dictonary to store reduced values.

for line in reader: #looping the reader object to get each row into line object.
    key = line[0]
    count = line[1]
    rank = line[2]
    if output.get(key) == None: #if key is not present in dict we are adding key and corresponding value to it. 
        output[key] = str(count) + ',' + str(rank) #replacing end of line with empty char
    else:
        oldValArr = output[key].split(',')
        oldCount = oldValArr[0]
        oldRank = oldValArr[1]
        
        newCount = int(oldCount) + int(count)
        newRank = ((int(oldRank)*int(oldCount))+int(rank))/int(newCount) #recaliculating the rank.
        
        output[key] = str(newCount) + ',' + str(int(newRank))
        
for key in output:
    print(key, ' ', output[key]) #providing output in required format.