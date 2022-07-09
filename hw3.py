# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 19:59:08 2022

@author: GAlamoudi
"""
#making an array from csv file
import numpy as np
import csv
import pandas as pd
import os.path

try_again = 1

while try_again == 1:
    csv_file = input("what is the name of your file ? ")+".csv"
    if os.path.exists(csv_file) == True:
        with open(csv_file, mode ='r') as file_name:
            csv_array = list(csv.reader(file_name))
            break
    else:
        try_again = int(input("### FILE DOESNT EXIST ###\n\npress 1 to try again : "))
    
    
#masking method
def masking(csv_array):
    a1 = []
    a2 = []
    a3 = []
    for i in csv_array:
        for j in i:
            for char in j:
                masked = chr(ord(char)+1)
                a1.extend(masked)
            a2.extend([''.join(a1)])
            a1 =[]
        a3.append(a2)
        a2 = []
    dataframe = pd.DataFrame(a3) 
    return dataframe.to_csv(r"{}\{}.csv".format((input("What is the path of your new file? : ")),(input("what is the name of the file? : "))))

#unmasking method
def un_masking(csv_array):
    a1 = []
    a2 = []
    a4 = []
    for i in csv_array:
        for j in i:
            for char in j:
                un_masked = chr(ord(char)-1)
                a1.extend(un_masked)
            a2.extend([''.join(a1)])
            a1 =[]
        a4.append(a2)
        a2 = []
    dataframe = pd.DataFrame(a4) 
    return dataframe.to_csv(r"{}\{}.csv".format((input("What is the path of your new file? : ")),(input("what is the name of the file? : "))))


cond = 3
while cond != 0 :    
    try:
        print("## choose a number ##\n1 to mask your data\n2 to unmask your data\n0 to exist")
        while cond != 0:
            cond = int(input()) 
            try:
                if cond == 1:
                    masking(csv_array)
                    break
                elif cond ==2:
                    un_masking(csv_array)
                    break
                elif cond == 0:
                    break
            except:
                print("SOMTHING WENT WRONG!!!")
    except:
        print("\n### please write a number ###")
