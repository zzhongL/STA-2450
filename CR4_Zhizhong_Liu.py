#Assignment: Code Reading 4
#Student Name: Zhizhong Liu


"""
This code processes a dataset to summarize and visualize the distribution of variables.

This code reads a dataset from "http://www.jpstats.org/data/fev.csv" and extracts all categorical variables.
It calculates the unique values, counts, percentages for each categorical variable.

This code includes functions:
    summary(significant_digits=2): Prints a summary of the categorical variables w/ counts and percentages.
    pie_cart(): Displays pie charts
    bar_chart(): Displays bar charts
"""

import pandas as pd
import matplotlib.pyplot as plt

dat = pd.read_csv("http://www.jpstats.org/data/fev.csv")

data_qual = dat.select_dtypes(exclude="number")
values = []
counts = []
percents = []

for var in data_qual.columns:
    current_var = data_qual[var]
    values.append(current_var.unique().tolist())
    counts.append(current_var.value_counts().tolist())
    percents.append((current_var.value_counts() / len(current_var) * 100).tolist())


def summary(significant_digits=2):
    """
    Prints a summary of the categorical variables in the dataset.

    Args:
        significant_digits (int, optional)

    This function iterates through all the categorical variables in `data_qual` and it prints the variable name,
    unique values, counts of each value, and corresponding percentages.
    """
    for i in range(len(counts)):
        print(f"Variable: {data_qual.columns[i]}")
        for j in range(len(values)):
            display_str = str(values[i][j])
            display_str += " " + str(counts[i][j]) + " "
            display_str += str(round(percents[i][j], significant_digits)) + "%"
            print(f"\t{display_str}")


def pie_cart():
    """
    Generates pie charts for each categorical variable

    This function creates a pie chart for each categorical variable in `data_qual`
    using unique values and respective counts.
    ALso sets the title of pie chart to variable name.
    """
    for i in range(len(values)):
        plt.pie(counts[i], labels=values[i])
        plt.title(data_qual.columns[i])
        plt.show()


def bar_chart():
    """
    Generates bar charts for each categorical variable

    This function creates a bar chart for each categorical variable in `data_qual`
    using unique values and respective counts.
    ALso sets the title of bar chart to variable name.
    """
    for i in range(len(values)):
        plt.bar(values[i], counts[i])
        plt.title(data_qual.columns[i])
        plt.show()


summary()
pie_cart()
bar_chart()

#This code summarizes the statistics of all categorical variables in the dataset
# and visualizes the distribution of each variable value
# in the form of pie charts and bar charts.