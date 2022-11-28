"""
Monte Carlo Lab


"""

#imports
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


#################
#   functions   #
#################

# returns a random integer from 1 to N (context: picks a random bin)
def get_random_num(N):
    return random.randint(1,N)

# do monte carlo simulations
def monte_carlo():
    N = 1000

    num_balls = list(range(1, N))
    num_empty_bins = []
    # run the simulation N times
    for curr_N in range(len(num_balls)):
        bins = [0] * N
        # individual simulation
        for curr_b in range(curr_N):
            bins[get_random_num(curr_N)-1] += 1                 # adds a ball to a random bin
        num_empty_bins.append(curr_N - np.count_nonzero(bins))  # appends the number of empty bins
    
    # perform scipy linear regression
    linear_regression(num_empty_bins, num_balls)

    # plot results
    plt.xlabel("Number of Balls")
    plt.ylabel("Number of Empty Bins")
    plt.plot(num_balls, num_empty_bins)
    plt.show()

# do linear regression
def linear_regression(num_empty_bins, num_balls):
    # set variables
    y = num_empty_bins
    X = num_balls

    # perform regression
    slope, intercept, rvalue, pvalue, stderr = stats.linregress(X,y)

    # print results
    print("SciPy Linear Regression Solution")
    print("slope     :", slope)
    print("intercept :", intercept)
    print("rvalue    :", rvalue)

    # write results
    results.write("SciPy Linear Regression Solution\n")
    results.write(f"slope     :  %f\n" %slope)
    results.write(f"intercept :  %f\n" %intercept)
    results.write(f"rvalue    :  %f\n" %rvalue)

#################
# end functions #
#################

# open txt file (to write table to)
results = open("results.txt", "w")



# run simulations
monte_carlo()