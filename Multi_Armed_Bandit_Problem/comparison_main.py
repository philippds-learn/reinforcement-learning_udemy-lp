import numpy as np
import matplotlib.pyplot as plt
from epsilons_session import run_experiment_eps as run_experiment_eps
from optimistic_initial_values_session import run_experiment_oiv as run_experiment_oiv
from ucb1_session import run_experiment_ucb1 as run_experiment_ucb1
from decaying_epsilon_session import run_experiment_decaying_epsilon as run_experiment_decaying_epsilon
from bayesian_session import run_experiment_bayesian as run_experiment_bayesian

if __name__ == '__main__':
    c_1 = run_experiment_eps(1.0, 2.0, 3.0, 0.1, 100000)
    oiv = run_experiment_oiv(1.0, 2.0, 3.0, 100000)
    ucb1 = run_experiment_ucb1(1.0, 2.0, 3.0, 100000)
    epc_decay = run_experiment_decaying_epsilon(1.0, 2.0, 3.0, 100000)
    bayesian = run_experiment_bayesian(1.0, 2.0, 3.0, 100000)
    
    # log scale plot
    plt.plot(c_1, label = 'eps = 0.1')
    plt.plot(oiv, label = 'optimistic')
    plt.plot(ucb1, label = 'ubc1')
    plt.plot(epc_decay, label = 'decaying_epsilon')
    plt.plot(bayesian, label = 'bayesian')
    
    plt.legend()
    plt.xscale('log')
    plt.show()
    