from decimal import Decimal, getcontext

from matplotlib import pyplot as plt


# This file contains functions to calculate factorial of a number, and functions implementing Taylor series approximation of sine, cosine and exponential.


getcontext().prec = 50

def factorial(n: int) -> int:
    """Function to calculate factorial of a number.

    :param n: Input number
    :type n: int

    :raises ValueError: When n is -ve as factorial of -ve numbers is not defined.

    :return: Calculated factorial value
    :rtype: int
    """

    fact=1
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")   
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
            fact *= i
        
    return fact


def sine(x: float | Decimal, terms: int = 50) -> Decimal:
    """Function implementing Taylor series approximation of sine.

    :param x: Value in radians for which sine is to be calculated.
    :type x: float | Decimal

    :param terms: Number of terms in the Taylor series, defaults to 50. Higher value results in higher accuracy.
    :type terms: int, optional

    :return: Calculated sine of x (approx.)
    :rtype: Decimal
    """
    

    if not isinstance(x, Decimal):
        x = Decimal(str(x))

    result = Decimal(0)

    for i in range(0, terms):
        n = Decimal(i)
        result += ((-1)**(i)) * (x**(2*n+1)) / Decimal(factorial(2*i+1))

    return result


def cosine(x: float | Decimal, terms: int = 50) -> Decimal:
    """Function implementing Taylor series approximation of cosine.

    :param x: Value in radians for which cosine is to be calculated.
    :type x: float | Decimal

    :param terms: Number of terms in the Taylor series, defaults to 50. Higher value results in higher accuracy.
    :type terms: int, optional

    :return: Calculated cosine of x (approx.)
    :rtype: Decimal
    """

    if not isinstance(x, Decimal):
        x = Decimal(str(x))

    result = Decimal(0)

    for i in range(0, terms):
        n = Decimal(i)
        result += ((-1)**(i)) * (x**(2*n)) / Decimal(factorial(2*i))

    return result


def exponential(x: float | Decimal, terms: int = 50) -> Decimal:
    """Function implementing Taylor series approximation of exponential.

    :param x: 
        Value for which exponential is to be calculated.
    :type x: 
        float | Decimal

    :param terms: 
        Number of terms in Taylor series, defaults to 50. Higher value results in higher accuracy.
    :type terms: 
        int, optional

    
    :return: Calculated exponential of x (e^x).
    :rtype: Decimal
    """

    if not isinstance(x, Decimal):
        x = Decimal(str(x))
    
    result = Decimal(0)

    for i in range(0, terms):
        result += ((x**Decimal(i)) / Decimal(factorial(i)))
    
    return result 

if __name__ == "__main__":
    print("This is the module for the mathematical functions in the sin_cos program. \nRun main.py to start the application.")