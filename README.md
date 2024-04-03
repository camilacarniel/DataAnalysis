 A collection of data science exercises designed to enhance understanding and proficiency in data analysis, and statistical modeling

Installation:

Before running the code, it is necessary to have the following libraries installed:
scipy
numpy
matplotlib
scikit-learn

# 01. Olympic Analysis 
The first file, entitled "Olympic Analysis", code analyzes Brazilian athletes using Olympic data. It calculates statistics such as mean, median, variance, and standard deviation of age for both male and female athletes.

The code also creates visualizations including a histogram to show the age distribution, a box plot to compare age distributions by sex, and a line plot with linear regression lines to analyze the trend of mean age over the years for male and female athletes. Additionally, it generates a bar plot to compare the total number of athletes and the number of medal-winning athletes by sex. The color palette for the plots is customized, with yellow, green and blue, the colors of the brazilian flag! 

# 02. Normal Distribution

Description:
The second file, entitled "Normal Distribution" contains the functions necessary to assist in the development of calculating values in the ZScore and determining the percentage of these values on a Gaussian curve.

Functions:
get_zscore():: This function returns the Z-score value based on a variable provided by the user.
get_percentage(zscore): This function returns the percentage based on a variable provided by the user, and calculates whether it is above or below the provided value.
plot_graph(): Generates a graph with the variable and/or the percentage, indicating them on the Gaussian curve.

# 03. Linear Regression

Description:
The third file, entitled "Linear Refression" asks the user for the number of data pairs (x, y) they want to input as well as the x and y values for each data pair. Linear regression is performed using LinearRegression from the scikit-learn library and the graph is plotted using matplotlib. You can, additionally see the equation of the regression line and the correlation between data.

