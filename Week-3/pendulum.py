import math

def period(length,gravity):
    try:
        period = (2*math.pi)*(math.sqrt(length/gravity))
        print(math.sqrt(length/gravity))
        print(period)
        return period
        
    except ValueError:
        raise ValueError
        print ("the numbers input were not suitable for the calculation")

    except TypeError:
        raise TypeError
        print ("Pls use numbers")
        
    except ZeroDivisionError:
        raise ZeroDivisionError
        print ("you cant devide by zero!!!")

period("hi",3)
