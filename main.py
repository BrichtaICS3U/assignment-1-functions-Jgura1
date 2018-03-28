# Assignment 1
# ICS3U
# Jesse Guram
# March 28, 2018

if CtoF:
    enter F
else:
    enter C


def CtoF(C):
    """convert from celcius to fahrenheit"""
    F = (1.8)*C+32

    return F
temperature = int(input('Enter your temperature in Celsius: '))
print(int(round(CtoF(temperature))))



def FtoC(F):
    """convert from fahrenheit to celcius"""
    C = (0.55556)*(F-32)

    return C
temperature = int(input('Enter your temperature in Fahrenheit:'))
print(int(round(FtoC(temperature))))

