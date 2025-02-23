# Bryce Beeskow
# Assignment 4
# 11/24/2024
# CSC115
# I certify, that this computer program submitted by me is all of my own work. Signed: Bryce Beeskow

# Function for reading users name (first and last) prints out their name
def read_name():
     firstname = input(('Enter your first name: '))     
     lastname = input('Enter your last name: ') 
     print(f'Name: {firstname} {lastname} \n')
     
     
# Function for reading gross pay of the user prints out the gross pay and returns it for calculations
def read_gross_pay():
     gross_pay = float(input('Enter your monthly gross pay: '))
     #formatting pattern  
     formatter = '{:.2f}'     
     print(f'Gross pay: $ {formatter.format(gross_pay)}\n')
     return gross_pay
     
     
# Function for reading number of dependents of the user prints dependents and returns it for calculations
def read_dependents():
     dependents = int(input('Enter number of dependents: '))
     print(f'Number of dependents: {dependents}\n')
     return dependents

# Function for computing tax rate depending on how many dependents
def compute_tax_rate(dependents):
     #if dependents is less than 2 (1 or 0) taxrate is 20% and the tax to calculate netpay is .20     
     if dependents < 2:
          taxrate = '20%'
          rate = 0.20
          print(f'Tax rate: {taxrate}\n')
          
     #else if dependents is 2 or 3 then tax rate is 15% and the tax to calculate netpay is .15
     elif dependents == 2 or dependents == 3:
          taxrate = '15%'
          rate = 0.15
          print(f'Tax rate: {taxrate}\n')
    #else dependents is 4 or more then tax rate is 10% and the tax to calculate netpay is .10
     else:
          taxrate = '10%'
          rate = 0.10    
          print(f'Tax rate: {taxrate}\n')
     return rate

# Function for cumputing the net pay of the user
def compute_net_pay(gross_pay, rate):
     netpay = gross_pay - (gross_pay * rate)
     #formatting pattern  
     formatter = '{:.2f}'
     print(f'Net Pay: ${formatter.format(netpay)}\n')
    
    
# main Function for the output
def main():  
     read_name()
     compute_net_pay(read_gross_pay(), compute_tax_rate(read_dependents()))
     
     
# prints out everything in the main function     
main()