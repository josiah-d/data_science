import numpy as np
import scipy.stats as scs

# visitors, registrations, purchases
lp1 = np.array([998832.,331912.,18255.])
lp2 = np.array([1012285.,349643.,18531.])
lp3 = np.array([995750.,320432.,18585.])

# Knowing when (and for how long) the data were 
# taken and how the visitors got to the website is also important 
# information for a thorough analysis.

# With this solution the following assumputions hold:
# We want to assume that individuals are independent of one another.
# We also want to assume that registers can only happen from visitors.  
# As well as, a purchase can only occur from an individual that is registered

def z_score_for_prop(lpA, lpB, visreg = True):
    '''Calculate the z score for two proportions where the
    null hypothesis is that the two proportions are equal,
    ie. p1 - p2 = 0. '''
    if visreg == True: #calc whether the difference in the 
        # registration to visitor proportion is significant
        total_prop = (lpA[1] + lpB[1]) / (lpA[0] + lpB[0])
        upper = ((lpA[1]/lpA[0]) - (lpB[1]/lpB[0])) + np.abs(scs.norm.ppf(.05/6))*((total_prop) * (1-total_prop)*(1 / lpA[0] + 1 / lpB[0]))**0.5
        lower = ((lpA[1]/lpA[0]) - (lpB[1]/lpB[0])) - np.abs(scs.norm.ppf(.05/6))*((total_prop) * (1-total_prop)*(1 / lpA[0] + 1 / lpB[0]))**0.5
    else: # calc whether the difference in the 
        # purchase to reg proportion is significant
        total_prop = (lpA[2] + lpB[2]) / (lpA[1] + lpB[1])
        upper = ((lpA[2]/lpA[1]) - (lpB[2]/lpB[1])) + np.abs(scs.norm.ppf(.05/6))*((total_prop) * (1-total_prop)*(1 / lpA[1] + 1 / lpB[2]))**0.5 
        lower = ((lpA[2]/lpA[1]) - (lpB[2]/lpB[1])) - np.abs(scs.norm.ppf(.05/6))*((total_prop) * (1-total_prop)*(1 / lpA[1] + 1 / lpB[2]))**0.5 
    return lower, upper

# We are performing 3 choose 2 tests: 3 tests, but for vis to reg and reg to pay is 3*2 = 6
# total tests.  The z-value above is for the bonferroni correction of the 
# number of tests we are computing values for.  That is .05/15 as our Type I Error rate.

z_score_for_prop(lp1, lp2, visreg = False) #Not Different
z_score_for_prop(lp3, lp2, visreg = False) #3 is higher than 2
z_score_for_prop(lp1, lp3, visreg = False) #Not Different

z_score_for_prop(lp1, lp2) #2 is higher than 1
z_score_for_prop(lp3, lp2) #2 is higher than 3
z_score_for_prop(lp1, lp3) #1 is higher than 3

# Based on these results, we would suggest page 2 for moving from vist to register
# We would also suggest either 3 or 1 form moving from register to pay.  There
# is no statistical difference between 3 and 1 in terms of moving from registered
# to paying.  We see that 3 is significantly higher than 2, but 1 is not.  
# More visitors may allow us to truly differentiate between 1 and 3.  At this 
# point is suggestive that 3 might be higher, but this is not statistically 
# significant at this point. We might also use a bayesian method using a uniform prior
# and computing the posterior based on the resulting beta distribution.
