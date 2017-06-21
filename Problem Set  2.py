# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:34:49 2017

@author: marsic
"""

### Problem 1 - Paying Debt off in a Year

#balance = 484
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

for i in range(12):
    balance -= balance * monthlyPaymentRate
    balance += balance * (annualInterestRate/12)
print('Remaing balance:', round(balance, 2))



### Problem 2 - Paying Debt Off in a Year
balance = 3926
annualInterestRate = 0.2
newBalance = balance
payment = 0

while abs(newBalance) >= 0.01:
    newBalance = balance
    payment += 10
    for i in range(12):
        newBalance -= payment
        newBalance += newBalance*(annualInterestRate/12)       
print('Lowest payment:', payment)


### Problem 3 - Using Bisection Search to Make the Program Faster
#balance = 320000
#annualInterestRate = 0.2
lowerBound = 0
upperBound = (balance * (1 + annualInterestRate/12)**12)/12
newBalance = balance

while abs(newBalance) > 0.1:
    newBalance = balance
    payment = (lowerBound+upperBound)/2
    for i in range(12):
        newBalance -= payment
        newBalance += newBalance * (annualInterestRate/12)
    if newBalance > 0:
        lowerBound = payment
    else:
        upperBound = payment
print('Lowest payment:', round(payment, 2))