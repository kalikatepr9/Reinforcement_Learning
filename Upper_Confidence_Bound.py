# Reinforcement learning 
                        
 # Upper Confidence Bound

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
#10000 users, 10 version of ad.
#1 = user clicks an add
#0 = user did'nt
'''
# Implementing Random Selection
#randomly showing ad to a user
import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward
'''

# Implementing UCB
import math           
N = 10000     #10000 rows/users/rounds
d = 10      #10 columns/ versions of advertisement
ads_selected = []
numbers_of_selections = [0] * d    #Ni(n) #initialise
sums_of_rewards = [0] * d          #Ri(n)
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]        #step 1
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i]) #step 2
            upper_bound = average_reward + delta_i                                #step 3
        else:
            upper_bound = 1e400        
            
        if upper_bound > max_upper_bound:      
            max_upper_bound = upper_bound
            ad = i
            
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward

# Visualising the results
plt.hist(ads_selected)       
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()  

#UCB helps to decide which next advertisement to show to user based on the previous data