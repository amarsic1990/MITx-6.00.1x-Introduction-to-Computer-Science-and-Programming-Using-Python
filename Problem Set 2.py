# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:55:10 2017

@author: marsic
"""

balance = 4842
annualInterestRate =0.2
monthlyPaymentRate = 0.04

for i in range(1,13):
    print('Month: '+ str(i))
    p = round(balance * monthlyPaymentRate, 2)
    print('Minimum monthly payment: ' + str(p))
    balance = round(balance-p, 2)
    balance = round(balance +(0.2/12*balance), 2)
    print('Remaining balance: ' + str(balance))
    