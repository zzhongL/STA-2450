import scipy.stats as stats
import numpy as np
import pandas as pd

np.set_printoptions(legacy='1.25')
data = pd.read_csv("http://www.jpstats.org/data/handspanheight.csv")
"""
def conf_int_sim(n, conf_level, num_sims):
    # Reading in the data
    data = pd.read_csv("http://www.jpstats.org/data/handspanheight.csv")
    # Setting confidence level
    alpha = 1 - conf_level
    # Finding t-critical value
    t_cv = stats.t.ppf(1 - alpha / 2, n - 1)
    # Creating empty lists for lower and upper bounds
    lower = []
    upper = []

    for i in range(num_sims):
        # Taking a random sample of size n from the dataset
        sample = data['handspan'].sample(n)
        xbar = sample.mean()  # Sample mean
        s = sample.std(ddof=1)  # Sample standard deviation
        lower.append(xbar - t_cv * s / np.sqrt(n))  # Lower limit of confidence interval
        upper.append(xbar + t_cv * s / np.sqrt(n))  # Upper limit of confidence interval

    # Finding the population mean (mu)
    mu = data['handspan'].mean()
    # Checking if the true mean falls into each interval
    coverage_list = [(mu > x) and (mu < y) for x, y in zip(lower, upper)]
    # Proportion of intervals containing the true mean
    return np.mean(coverage_list)


# Testing the conf_int_sim function
result = conf_int_sim(n=20, conf_level=0.95, num_sims=100)
print("Coverage proportion:", result)

"""
# Function to generate simulated data
def gen_data(distribution, n):
    """
    Generate simulated data from the given distribution.

    Parameters
    ----------
    distribution : str
        The name of the distribution to simulate from ("normal", "uniform", "exponential", "t").
    n : int
        Size of the sample to simulate.

    Returns
    -------
    tuple
        A tuple of the simulated data array and the theoretical mean of the distribution.
    """
    if distribution == "normal":
        data = stats.norm.rvs(size=n)
        mu = stats.norm.mean()
    elif distribution == "uniform":
        data = stats.uniform.rvs(size=n)
        mu = stats.uniform.mean()
    elif distribution == "exponential":
        data = stats.expon.rvs(size=n)
        mu = stats.expon.mean()
    elif distribution == "t":
        data = stats.t.rvs(size=n, df=10)
        mu = stats.t.mean(df=10)
    else:
        raise ValueError("Invalid distribution name. Choose from 'normal', 'uniform', 'exponential', 't'.")
    return data, mu

simulated_data, true_mean = gen_data("exponential", 20)
print("Simulated data:", simulated_data)
print("Theoretical mean:", true_mean)


#First funciton will just clacualte the lower and and upper limits of a confidence interval
def cal_conf_int(data,conf_level):
    alpha = 1 - conf_level
    n = len(data)
    # Finding t-critical value
    t_cv = stats.t.ppf(1 - alpha / 2, n - 1)
    # Taking a random sample of size n from the dataset
    sample = data
    xbar = sample.mean()  # Sample mean
    s = sample.std () # Sample standard deviation
    ll = xbar - t_cv * s / np.sqrt(n)
    ul = xbar + t_cv * s / np.sqrt(n)
    return ll,ul


def conf_int_sim(distribution, n, conf_level, num_sims):
    coverage_list = []
    for i in range(num_sims):
        data, mu = gen_data(distribution, n)
        ll, ul = cal_conf_int(data, conf_level)
        coverage_list.append((mu > ll) and (mu < ul))
    coverage = np.mean(coverage_list)
    return coverage

conf_int_sim("normal",20,0.95,100)
ll,ul = cal_conf_int(data,95)