import pandas
import scipy.stats
import numpy




class CI_simulation():
    def __init__(self):
        """Initializes the simulation"""
        self.dat = None
        self.mu = None
        self.lower_limit = []
        self.upper_limit = []
        self.coverage = None

    def gen_data(self, distribution, n):
        """
        Generate simulated data from the given distibution
        Parameters
        ----------
        distribution : String
            the name of the distribution to simulate from
            Can be one of the following:
                "norm"
                "uniform"
                "expon"
                "t" - t will have 10 df
        n : int > 1
            Size of the sample to simulate

        Returns
        -------
        a series of the simulated data
        the mean of the distribution

        """

        if distribution == "norm":
            self.dat = pandas.Series(scipy.stats.norm.rvs(size=n))
            self.mu = scipy.stats.norm.mean()

        if distribution == "uniform":
            self.dat = pandas.Series(scipy.stats.uniform.rvs(size=n))
            self.mu = scipy.stats.uniform.mean()

        if distribution == "expon":
            self.dat = pandas.Series(scipy.stats.expon.rvs(size=n))
            self.mu = scipy.stats.expon.mean()

        if distribution == "t":
            self.dat = pandas.Series(scipy.stats.t.rvs(size=n, df=10))
            self.mu = scipy.stats.t.mean(df=10)

    def cal_conf_int(self, conf_level):
        """
        Calculates the specified level confidence interval for the given data
        Parameters
        ----------
        data : a pandas series
            The data used to make the confidence interval
        conf_level : float between 0 and 1 exclusive
            The confidence level of the interval for each iteration.

        Returns
        -------
        lower limit: float
            the lower limit of the interval
        upper limit: float
            the upper limit of the interval
        """

        n = len(self.dat)

        alpha = 1 - conf_level
        t_cv = scipy.stats.t.ppf(1 - alpha / 2, n - 1)

        xbar = self.dat.mean()
        std_dev = self.dat.std()
        ll = xbar - t_cv * (std_dev / numpy.sqrt(n))
        ul = xbar + t_cv * (std_dev / numpy.sqrt(n))

        return ll, ul

    def conf_int_sim(self, distribution, n, conf_level, num_sims):
        """
        Simulates data from distribution and computes the confidence interval.
        This is done num_sims times. The coverage of the interval is returned

        Parameters
        ----------
        distribution : String
            the name of the distribution to simulate from
            Can be one of the following:
                "norm"
                "uniform"
                "expon"
                "t" - t will have 10 df
        n : int > 1
            Size of the sample to simulate
        conf_level : float between 0 and 1 exclusive
            The confidence level of the interval for each iteration.
        num_sims : int > 0
            The number of iterations.

        Returns
        -------
        A float representing the proportion of times the interval contained the
        true mean.

        """

        for i in range(num_sims):
            self.gen_data(distribution, n)
            ll, ul = self.cal_conf_int(conf_level)
            self.lower_limit.append(ll)
            self.upper_limit.append(ul)

        coverage_list = [self.mu > x and self.mu < y for x, y in zip(self.lower_limit, self.upper_limit)]
        self.coverage = numpy.mean(coverage_list)

        return self.coverage


sim = CI_simulation()
sim.conf_int_sim("norm", 20, .95, 1000)
sim.coverage


import plotinine

widths_data = sim.widths
widths_data = pandas.DataFrame(widths_data)
p =
(
    plotnine.ggplot(data = data) +
    plotinine.geom_histogram(plotnine.aes(x = "widths"),)
    bins = 50, color = "red", fill = "blue"
)

p.show()