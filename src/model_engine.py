import pymc as pm
import numpy as np
import arviz as az
import matplotlib.pyplot as plt


class BrentOilBayesianModel:
    def __init__(self, data):
        self.data = np.array(data)
        self.n_data = len(self.data)
        self.model = None
        self.trace = None

    def build_model(self):
        """Builds the Bayesian Change Point Model (Instruction 1b)"""
        idx = np.arange(self.n_data)

        with pm.Model() as self.model:
            # i. Define Switch Point (tau)
            tau = pm.DiscreteUniform("tau", lower=0, upper=self.n_data - 1)

            # ii. Define "Before" and "After" Parameters (mu1, mu2)
            mu_1 = pm.Normal("mu_1", mu=self.data.mean(),
                             sigma=self.data.std())
            mu_2 = pm.Normal("mu_2", mu=self.data.mean(),
                             sigma=self.data.std())
            sigma = pm.HalfNormal("sigma", sigma=self.data.std())

            # iii. Use Switch Function
            mu = pm.math.switch(tau > idx, mu_1, mu_2)

            # iv. Define Likelihood
            obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=self.data)

    def run_sampler(self, draws=2000, tune=1000):
        """Runs the MCMC simulation (Instruction 1b-v)"""
        with self.model:
            self.trace = pm.sample(
                draws=draws, tune=tune, target_accept=0.9, return_inferencedata=True)
        return self.trace

    def interpret_outputs(self):
        """Check convergence and plot results (Instruction 1c)"""
        # i. Check for Convergence (r_hat)
        print(az.summary(self.trace, var_names=["mu_1", "mu_2", "tau"]))
        az.plot_trace(self.trace)
        plt.show()

        # ii. Identify Change Point (Posterior of tau)
        az.plot_posterior(self.trace, var_names=["tau"])
        plt.title("Posterior Distribution of Change Point (Tau)")
        plt.show()
