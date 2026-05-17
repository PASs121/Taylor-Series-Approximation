from math import cos, pi, sin
from decimal import Decimal, getcontext

from matplotlib import pyplot as plt


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
    """Fuction implementing Taylor series approximation of sine.

    :param x: Value in radians for which sine is to be calculated.
    :type x: float | Decimal

    :param terms: Number of terms in the Talyor series, defaults to 50. Higher value results in higher accuracy.
    :type terms: int, optional

    :return: Calculated sine of x (approx.)
    :rtype: Decimal
    """
    

    if isinstance(x, float):
        x = Decimal(str(x))

    sum = Decimal(0)

    for i in range(0, terms):
        n = Decimal(i)
        sum += ((-1)**(i)) * (x**(2*n+1)) / Decimal(factorial(2*i+1))

    return sum


def cosine(x: float | Decimal, terms: int = 50) -> Decimal:
    """Fuction implementing Taylor series approximation of cosine.

    :param x: Value in radians for which cosine is to be calculated.
    :type x: float | Decimal

    :param terms: Number of terms in the Taylor series, defaults to 50. Higher value results in higher accuracy.
    :type terms: int, optional

    :return: Calculated cosine of x (approx.)
    :rtype: Decimal
    """

    if isinstance(x, float):
        x = Decimal(str(x))

    sum = Decimal(0)

    for i in range(0, terms):
        n = Decimal(i)
        sum += ((-1)**(i)) * (x**(2*n)) / Decimal(factorial(2*i))
    return sum


# -------- PLOT SECTION --------

# Lists for the x and y values of the curves
x_values = []
taylor_sin_values = []
taylor_cos_values = []
math_sin_values = []
math_cos_values = []
delta_sin_values = []
delta_cos_values = []


# Generate points from -12π to 12π
step = 0.05
x = -12 * pi

while x <= 12 * pi:

    x_values.append(x)

    # Taylor series sine
    taylor_y = float(sine(x))
    taylor_sin_values.append(taylor_y)

    # Built-in math.sin()
    math_y = sin(x)
    math_sin_values.append(math_y)

    # Difference between Taylor series and math sine functions
    delta_sin_values.append(abs(taylor_y - math_y))

    # Taylor series cosine
    taylor_y = float(cosine(x))
    taylor_cos_values.append(taylor_y)

    # Built-in math.cos()
    math_y = cos(x)
    math_cos_values.append(math_y)

    # Difference between Taylor series and math cosine functions
    delta_cos_values.append(abs(taylor_y - math_y))

    x += step


# Create the plots for the Taylor series and math functions

plt.figure(figsize=(10, 5))

# Taylor series curve
plt.plot(
    x_values,
    taylor_sin_values,
    label="Taylor Series sin(x)",
    color="blue",
    linewidth=2
)

# math.sin curve
plt.plot(
    x_values,
    math_sin_values,
    label="math.sin(x)",
    color="red",
    linestyle="dashed",
    linewidth=2
)

# Difference between Taylor series and math sine curves
plt.plot(
    x_values,
    delta_sin_values,
    label="Difference in sin(x)",
    color="magenta",
    linestyle="solid",
    linewidth=1
)

plt.title("Comparison of Taylor Series and math sine functions")
plt.xlabel("Value of x (radians)")
plt.ylabel("Value of sin(x)")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.grid(True)
plt.legend()

plt.figure(figsize=(10, 5))

# Taylor series cosine curve
plt.plot(
    x_values,
    taylor_cos_values,
    label="Taylor Series cos(x)",
    color="cyan",
    linewidth=2
)

# math.cos curve
plt.plot(
    x_values,
    math_cos_values,
    label="math.cos(x)",
    color="green",
    linestyle="dashed",
    linewidth=2
)

# Difference between Taylor series and math cosine curves
plt.plot(
    x_values,
    delta_cos_values,
    label="Difference in cos(x)",
    color="orange",
    linestyle="solid",
    linewidth=1
)

plt.title("Comparison of Taylor Series and math cosine functions")
plt.xlabel("Value of x (radians)")
plt.ylabel("Value of cos(x)")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.grid(True)
plt.legend()

plt.show()