# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:55:10 2017

@author: marsic
"""
############################ Problem 1: Paying The Minimum
#balance = 4842
#annualInterestRate =0.2
#monthlyPaymentRate = 0.04
pSum = 0

for i in range(1,13):
    #print('Month: '+ str(i))
    p = round(balance * monthlyPaymentRate, 2)
    pSum = round(pSum+p,2)
    #print('Minimum monthly payment: ' + str(p))
    balance = round(balance-p, 2)
    balance = round(balance +(annualInterestRate/12*balance), 2)
    #print('Remaining balance: ' + str(balance))
#print('Total paid: ' + str(pSum))  
print('Remaining balance: ' + str(balance))


################################# Problem 2: Paying Debt Off In A Year
balance = 3329
annualInterestRate = 0.2
p = 10
while True:
    newBalance = balance
    for i in range(12):        
        newBalance -= p
        newBalance = newBalance + annualInterestRate / 12 * newBalance
    if newBalance <= 0: break
    p += 10
print('Lowest Payment: ' + str(p))

############### Problem 3: Using Bisection Search to Make the Program Faster
balance = 320000
annualInterestRate = 0.2
lb = round(balance / 12,2)
ub = round(balance * annualInterestRate, 2)

while True:
    newBalance = balance
    p = round((lb+ub)/2.0,2)
    for i in range(12):
        newBalance -= p       
        newBalance = round(newBalance + annualInterestRate / 12 * newBalance, 2)
    if abs(newBalance) < 0.1:
        break
    elif newBalance > 0:
        lb = p
    else:
        ub = p
print('Lowest Payment: ' + str(p))    
        
        
    