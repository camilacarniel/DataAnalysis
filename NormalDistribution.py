#Normal distribution

import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

# Parameterize the input depending on the data
def get_zscore():
    var = float(input("Enter the variable to be evaluated: "))
    return st.norm.cdf(var) # Value of the specific number in ZScore

# Return the percentage value
def get_percentage(zscore):
    direction = float(input("Enter 1 for values greater (1) or less (0) than your variable: "))
    mean = float(input("Enter the distribution mean: "))
    std_deviation = float(input("Enter the distribution standard deviation: "))
    z = (zscore - mean) / std_deviation
    return (1 - st.norm.cdf(z)) if direction == 1 else st.norm.cdf(z)

# Plot the graph
def plot_graph():
    # Ask the user if they want to know the position of a number in ZScore

    while True:
        user_choice = input("Do you want to know the position of a number in ZScore? Enter 'yes' to continue or any other key to exit: ")
        if user_choice.lower() != 'yes':
            print("Exiting the program.")
            break

        zscore = get_zscore()
        # Ask the user if they want to know the percentage of values above or below the number in ZScore
        plot_percentage = input("Do you want to know the percentage of values above or below the number in ZScore? Enter 'yes' for the first option or 'no' for the second: ")

        # Gaussian curve
        x = np.linspace(-5, 5, 1000)  
        y = st.norm.pdf(x, 0, 1) 
        plt.plot(x, y, 'r-', label='Gaussian Curve')

        # Adding the ZScore value to the curve
        plt.plot(zscore, st.norm.pdf(zscore, 0, 1), 'bo', label='Value in ZScore')

        if plot_percentage.lower() == 'yes':
            percentage = get_percentage(zscore)
            plt.axvline(x=percentage, color='g', linestyle='--', label='Percentage')

        plt.xlabel('Values')
        plt.ylabel('Probability Density')
        plt.title('Gaussian Curve with Value in ZScore and Percentage')
        plt.legend()
        plt.grid(True)
        plt.show()

# Putting the functions into practice
plot_graph()
