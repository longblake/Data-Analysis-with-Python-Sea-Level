import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(x=df.iloc[:, 0], y=df.iloc[:, 1])

    # Add labels and title
    plt.xlabel('Year')  # Label for x-axis using the column name
    plt.ylabel('Sea Level (inches)')  # Label for y-axis using the column name
    plt.title('Rise in Sea Level')
    
    #Year,CSIRO Adjusted Sea Level,Lower Error Bound,Upper Error Bound,NOAA Adjusted Sea Level


    # Create first line of best fit
    line_1 = linregress(x=df.iloc[:, 0], y=df.iloc[:, 1])
    plt.plot(df.iloc[:, 0],line_1.slope * df.iloc[:,0] + line_1.intercept)

    # Create second line of best fit
    #linregress(x, y=None, alternative='two-sided')

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()