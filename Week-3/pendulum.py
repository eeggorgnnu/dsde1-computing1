import math

def period(length,gravity):
    try:
        period = (2*math.pi)*(math.sqrt(length/gravity))
        print(math.sqrt(length/gravity))
        print(period)
        return period
        
    except ValueError or TypeError or ZeroDivisionError:
        print ("the numbers input were not suitable for the calculation")

