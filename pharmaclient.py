# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:04:59 2021

@author: pradeep
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:27:03 2021

@author: pradeep
"""

import csv
import socket
import pandas as pd
import datetime
import math

c=socket.socket()
c.connect(('localhost',5001))
ch=input("Press a -Adding the Medicine \n Press t for getting the all stock \n Press s for checking the stock \nPress b for billing \n")
         
tp=[]
# FOR ADDING NEW MEDICINE TO THE PHARMACY
if(ch == 'a'):
    df=pd.read_csv("pharmacy.csv")
    
    
    
    print("enter id,medicinename,manufactor,Exp Date,stock,Shelf,price \n")
    for i in range(0,7):
        temp=input()
        tp.append(temp)
    with open("pharmacy.csv", 'a', newline='') as csvfile:
        
        writer = csv.writer(csvfile)
        writer.writerow(tp)
 
#GETTING STOCK OF ALL MEDICINE 
elif(ch =='t'):
    df=pd.read_csv("pharmacy.csv")
    print(df)
    
 # FOR CHECKING STOCK OF A MEDICINE   
elif (ch=='s'):
    with open("pharmacy.csv", 'a', newline='') as csvfile:
        data=csv.reader(csvfile)
        df = pd.read_csv('pharmacy.csv') 
        medname=input("Enter the medicine name \n")
        for i in range(len(df)):
            if df.loc[i,"MEDICINENAME"]==medname:
                stock=df.loc[i,"STOCK"]
                if (stock == 0):
                    print("OUT OF STOCK")
                else:
                    print("In STOCK",stock)
  
    # For BILLING
elif(ch=='b'):
    with open("pharmacy.csv", 'a', newline='') as csvfile:
        data=csv.reader(csvfile)
        df = pd.read_csv('pharmacy.csv') 
        print("Enter 0 if purchase is over \n")
        total=0
        bill={"MEDICINENAME":[],"qty":[],"price":[]}
        b=[]
        while True:
            medname=input("Enter the medicine name \n")
            if medname =='0':
               # bill.append(total) 
                receipt=pd.DataFrame(bill)
                print(receipt)
                break
            
            qty=int(input("Enter quantity \n"))
            for i in range(len(df)):
                if df.loc[i,"MEDICINENAME"]==medname:
                    df.loc[i,"STOCK"]=df.loc[i,"STOCK"]-qty
                    bill.append(df.loc[i,"MEDICINENAME"])
                    bill.append(qty)
                    total=total +df.loc[i,"PRICE"]*qty
                    bill.append(df.loc[i,"PRICE"]*qty)
                    bill.append(";")
             
            
                    
        df.to_csv("pharmacy.csv", mode='w', index=False)
        
        
                

    
c.close()
    