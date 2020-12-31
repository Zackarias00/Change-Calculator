#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:48:31 2020

@author: zackarias00
"""
import random

# SIMPLE FUNCTION TO FIND THE CHANGE

def find_change(total,payment):
    return payment - total

paying = True

while paying:

    total = 0.0
    payment = 0.0
    change = 0.0
    decision = False
    do_we_let_it_slide = [True,False]

# INPUT TOTAL

    while True:
        try:
            total = float(input('\nWhat is the total? \n$ '))
        except:
            print("\nIt has to be a number!")
        else:
            break

# INPUT CUSTOMER PAYMENT    

    while True:
        if total <= 0:
            break
        try:
            payment = float(input('\nWhat did the customer pay with? \n$ '))
        except:
            print("\nIt has to be a number!")
        else:

            # RANDOM DECISION TO LET THE CUSTOMER OFF WITHOUT PAYING THE ENTIRE BILL

            if payment - total >= -0.50 and payment - total <= 0:
                decision = random.choice(do_we_let_it_slide)
            if decision == True:
                print("\nI'll cover you on the rest")
                paying = False
                break

            # IF THE CUSTOMER OWES MORE MONEY

            while payment < total and decision == False:
                print("\nYou still owe me money!")
                payment = payment + float(input("\nGive me some more money! \n$ "))
            else:
                break
        
    change = round(find_change(total,payment),2)
    
    if total <= 0:
        print("\nThat's stupid!")
        paying = False
        break
    elif change < 0:
        break
    elif change == 0:
        print("\nI don't owe you anything!")
        paying = False
    else:
        print(f"\nThis is how much I owe you! \n${change} \nTake it and get out!")
        paying = False