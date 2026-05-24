from matplotlib import pyplot as plt
from decimal import Decimal
from numpy import arange
from math import cos, pi, sin, exp
from lib import sine, cosine, exponential

# This file contains the Plotter class for plotting line graphs using Matplotlib for comparison of Taylor series and math functions.

class Plotter():
    """Class object for plotting line graphs using Matplotlib for comparison.
    """

    def __init__(self):
        plt.style.use("dark_background")

    def plot_sine(self, terms: int, plot_range: float = 2):
        """Plots a line graph using Taylor sine function and math sine function for comparison.
        
        :param terms: 
            Number of terms to use in the Taylor series.
        :type terms: 
            int

        :param plot_range: 
            Range of x values to plot, defaults to 2.
        :type plot_range: 
            float, optional
        """

        x_values = arange(-plot_range * pi, plot_range * pi, 0.1)
        taylor_values = [sine(x, terms) for x in x_values]
        math_values = [sin(x) for x in x_values]
        

        plt.figure(figsize=(10, 5))

        plt.plot(
            x_values, 
            taylor_values, 
            label=f"Taylor Series (n={terms})", 
            color="#4FC3F7"
            )
        
        plt.plot(
            x_values, 
            math_values, 
            label="math.sin(x)", 
            color="#FF7043", 
            linestyle="dashed"
            )

        plt.title("Comparison of Taylor Series and math sine functions")
        plt.xlabel("Value of x (radians)")
        plt.ylabel("Value of sin(x)")

        plt.axhline(0, color='#888888', linewidth=0.5)
        plt.axvline(0, color='#888888', linewidth=0.5)

        plt.grid(visible=True,color="#444444")
        plt.legend()
        plt.show()



    def plot_cosine(self, terms: int, plot_range: float = 2):
        """Plots a line graph using Taylor cosine function and math cosine function for comparison.

        :param terms: 
            Number of terms to use in the Taylor series.
        :type terms: 
            int

        :param plot_range: 
            Range of x values to plot, defaults to 2.
        :type plot_range: 
            float, optional
        """

        x_values = arange(-plot_range * pi, plot_range * pi, 0.1)
        taylor_values = [cosine(x, terms) for x in x_values]
        math_values = [cos(x) for x in x_values]

        plt.figure(figsize=(10, 5))

        plt.plot(
            x_values, 
            taylor_values, 
            label=f"Taylor Series (n={terms})", 
            color="#81C784"
            )
        
        plt.plot(
            x_values, 
            math_values, 
            label="math.cos(x)", 
            color="#BA68C8", 
            linestyle="dashed"
            )

        plt.title("Comparison of Taylor Series and math cosine functions")
        plt.xlabel("Value of x (radians)")
        plt.ylabel("Value of cos(x)")

        plt.axhline(0, color='#888888', linewidth=0.5)
        plt.axvline(0, color='#888888', linewidth=0.5)

        plt.grid(visible=True,color="#444444")
        plt.legend()
        plt.show()



    def plot_exponential(self, terms: int, plot_range: float = 2):
        """Plots a line graph using Taylor exponential function and math exponential function for comparison.

        :param terms: 
            Number of terms to use in the Taylor series.
        :type terms: 
            int

        :param plot_range: 
            Range of x values to plot, defaults to 2.
        :type plot_range: 
            float, optional
        """

        x_values = arange(-(plot_range/2), plot_range, 0.1)
        taylor_values = [exponential(x, terms) for x in x_values]
        math_values = [exp(x) for x in x_values]
        
        plt.figure(figsize=(10, 5))

        plt.plot(
            x_values, 
            taylor_values, 
            label=f"Taylor Series (n={terms})", 
            color="#EC407A"
            )
        
        plt.plot(
            x_values, 
            math_values, 
            label="math.exp(x)", 
            color="#26C6DA", 
            linestyle="dashed"
            )

        plt.title("Comparison of Taylor Series and math exponential functions")
        plt.xlabel("Value of x")
        plt.ylabel("Value of exp(x)")

        plt.axhline(0, color='#888888', linewidth=0.5)
        plt.axvline(0, color='#888888', linewidth=0.5)

        plt.grid(visible=True,color="#444444")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    print("This is the module for plotting functions in the sin_cos program. \nRun main.py to start the application.")