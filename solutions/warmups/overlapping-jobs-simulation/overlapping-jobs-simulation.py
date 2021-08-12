import numpy as np
# There are five hours in this interval and each job lasts one hour, or 20% of the total interval.
# Let's use np.random.random to generate a number between 0 and 1, representing the position in the interval that the jobs start.
# If the difference between start times is <= 20% of the interval then there's an overlap. 
process_1 = np.random.random(size=10**7)
process_2 = np.random.random(size=10**7)
overlap_percentage = np.mean(np.abs(process_1 - process_2) <= 0.20)
annual_cost = overlap_percentage * 365 * 1000
print(annual_cost)
