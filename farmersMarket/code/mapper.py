#!/usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter=';') #intitailizing reader object and saperating coloumns data.



for line in reader:
    #looping the reader object to get each row into line object.
    try:
        key = line[3]+','+line[5] #taking city and state values as key.
        rank = 0
        for i in range(9, 45): #looping through the product coloum and if product is available then adding 1 to rank 
            if str(line[i]) == 'True':
                rank += 1
        for i in range(45,47):
            if str(line[i]) == 'True':#for having online presence we are giving extra credit.
                rank += 2
    except:
        continue
    
    print(key,';',1,';',rank) #output wiil key ; <market count for the key> ; rank


