import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(x=df.iloc[:, 0], y=df.iloc[:, 1], c = 'c')

    # Add labels and title
    plt.xlabel('Year')  # Label for x-axis using the column name
    plt.ylabel('Sea Level (inches)')  # Label for y-axis using the column name
    plt.title('Rise in Sea Level')

    # Create Second df
    df2 = df[df.iloc[:, 0] >= 2000]
    df2 = df2.reset_index(drop=True)

    # Generate Lines of Best Fit 
    line_1 = linregress(x=df.iloc[:, 0], y=df.iloc[:, 1])
    line_2 = linregress(x=df2.iloc[:, 0], y=df2.iloc[:, 1] )

    #Extend Timelines 
    extended_years = np.arange(df.iloc[0, 0], 2051)
    extended_years_2 = np.arange(2000, 2051)

    #Plot Lines of Best Fit 
    plt.plot(extended_years,line_1.slope * extended_years + line_1.intercept, c = 'b')
    plt.plot(extended_years_2,line_2.slope * extended_years_2 + line_2.intercept, c = 'r')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()