 A collection of data science exercises designed to enhance understanding and proficiency in data analysis, and statistical modeling

Installation:

Before running the code, it is necessary to have the following libraries installed:
scipy
numpy
matplotlib
scikit-learn

# 01. Normal Distribution

Description:
The first file, entitled "Normal Distribution" contains the functions necessary to assist in the development of calculating values in the ZScore and determining the percentage of these values on a Gaussian curve.

Functions:
get_zscore():: This function returns the Z-score value based on a variable provided by the user.
get_percentage(zscore): This function returns the percentage based on a variable provided by the user, and calculates whether it is above or below the provided value.
plot_graph(): Generates a graph with the variable and/or the percentage, indicating them on the Gaussian curve.

# 02. Linear Regression

Description:
The second file, entitled "Linear Refression" asks the user for the number of data pairs (x, y) they want to input as well as the x and y values for each data pair. Linear regression is performed using LinearRegression from the scikit-learn library and the graph is plotted using matplotlib. You can, additionally see the equation of the regression line and the correlation between data.

