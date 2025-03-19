import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Observed Data", color="blue")


    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_full = np.arange(df["Year"].min(), 2051)
    sea_level_pred_full = slope * years_full + intercept
    plt.plot(years_full, sea_level_pred_full, label="Best Fit All Years", color="red")


    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = np.arange(2000, 2051)
    sea_level_pred_recent = slope2 * years_recent + intercept2
    plt.plot(years_recent, sea_level_pred_recent, label="Best Fit (2000+)", color="green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()