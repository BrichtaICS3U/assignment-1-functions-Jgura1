# Assignment 1
# ICS3U
# Jesse Guram
# March 28, 2018

def CtoF(C):
    """convert from celcius to fahrenheit"""
    F = (1.8)*C+32

    return F

def FtoC(F):
    """convert from fahrenheit to celcius"""
    C = (0.55556)*(F-32)

    return C

print('enter 1 for Celcius or 2 Fahrenheit:')
x = int(input())

if x == 1:
    temperature1 = int(input('Enter your temperature in Celsius: '))
    print(int(round(CtoF(temperature1))))
   
elif x == 2:
    temperature2 = int(input('Enter your temperature in Fahrenheit:'))
    print(int(round(FtoC(temperature2))))
    

else:
    print('neither')







