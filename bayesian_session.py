import numpy as np
import matplotlib.pyplot as plt

class BayesianBandit:
    def __init__(self, m):
        self.m = m
        # parameter for mu - prior is N(0,1)
        self.m0 = 0
        self.lambda0 = 1
        self.sum_x = 0
        self.tau = 1
    
    def pull(self):
        return np.random.randn() + self.m
    
    def sample(self):
        return np.random.randn() / np.sqrt(self.lambda0) + self.m0
    
    def update(self, x):
        # assume tau is 1
        self.lambda0 += 1
        self.sum_x += x
        self.m0 = self.tau * self.sum_x / self.lambda0

def run_experiment_bayesian(m1, m2, m3, N):
    bandits = [BayesianBandit(m1), BayesianBandit(m2), BayesianBandit(m3)]

    data = np.empty(N)
  
    for i in range(N):
        # optimistic initial values
        j = np.argmax([b.sample() for b in bandits])
        x = bandits[j].pull()
        bandits[j].update(x)

        # for the plot
        data[i] = x
    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

    # plot moving average ctr
    plt.plot(cumulative_average)
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    plt.xscale('log')
    plt.show()

    return cumulative_average