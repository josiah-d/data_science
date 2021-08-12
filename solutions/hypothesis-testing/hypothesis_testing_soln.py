import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from z_test import z_test

from itertools import combinations
import scipy.stats as stats


def plot_subgroup_hist(df, df_signed_in, df_not_signed_in):
    '''
    Displays information of 2 sub groups of a data set 
    '''
    
    fig, axs = plt.subplots(2, 3, figsize=(12, 5))
    for col_name, ax in zip(df_signed_in.columns, axs.flatten()):
        bins = np.linspace(df[col_name].min(), df[col_name].max(), 20)
        height, binz = np.histogram(df_signed_in[col_name], bins=bins, density=True)
        bp1 = ax.bar(bins[:-1], height, .5*(bins[1]-bins[0]),
                     alpha=0.5, label="Signed In", color='g')
        height, binz = np.histogram(df_not_signed_in[col_name], bins=bins, density=True)
        bp2 = ax.bar(bins[:-1]+.5*(bins[1]-bins[0]), height,
                     .5*(bins[1]-bins[0]), color='b', alpha=.5)
        ax.set_title(col_name)
        ax.legend((bp1[0], bp2[0]), ("Signed In", "Not Signed In"), loc='best')

    plt.tight_layout()

    return fig, ax


def age_group_pairs(df_signed_in, alpha=.05):
    results = pd.DataFrame()
    combos = combinations(pd.unique(df_signed_in['age_groups']), 2)
    for age_group_1, age_group_2 in combos:
        age_group_1_ctr = df_signed_in[df_signed_in.age_groups == age_group_1]['CTR']
        age_group_2_ctr = df_signed_in[df_signed_in.age_groups == age_group_2]['CTR']
        p_value = stats.ttest_ind(age_group_1_ctr, age_group_2_ctr, equal_var=True)[1]
        age_group_1_ctr_mean = age_group_1_ctr.mean()
        age_group_2_ctr_mean = age_group_2_ctr.mean()
        diff = age_group_1_ctr_mean-age_group_2_ctr_mean
        absolute_diff = abs(age_group_1_ctr_mean-age_group_2_ctr_mean)
        results = results.append({
                'first_age_group':age_group_1, 'second_age_group':age_group_2, 
                'first_group_mean':age_group_1_ctr_mean, 'second_group_mean':age_group_2_ctr_mean,
                'mean_diff':diff, 'absolute_mean_diff':absolute_diff, 'p_value':p_value},
                ignore_index=True)

    results = results[['first_age_group', 'second_age_group', 
                    'first_group_mean', 'second_group_mean', 
                    'mean_diff', 'absolute_mean_diff', 'p_value']]

    return results

def find_mismatch(ab_cell, landing_page_cell):
    """Checks if A/B test treatment/control encoding is accurate
    Parameters
    ----------
    ab_cell: str
        Treatment/Control encoding
    landing_page_cell: str
        Page version
    Returns
    -------
    int: indicator of match (1) or mismatch (0)
    """

    if ab_cell == 'treatment' and landing_page_cell == 'new_page':
        return 0
    elif ab_cell == 'control' and landing_page_cell == 'old_page':
        return 0
    else:
        return 1

def calc_conversion_rate(data, page_type):
    """Counts proportion of tatal visits resulting in a conversion
    Parameters
    ----------
    data: Pandas DataFrame
        A/B testing storage DataFrame with columns 'converted' (1=yes, 0=no)
        and 'landing_page' with values "new_page" or "old_page"
    page_type: str ("new" or "old")
        corresponding to the "new_page"/"old_page"
    Returns
    -------
    float: proportion of total visits converted for input page_type
    """

    total_vis = data[data['landing_page'] == page_type + '_page']
    converted = total_vis[total_vis['converted'] == 1].shape[0]
    return float(converted) / total_vis.shape[0], total_vis.shape[0]


def plot_pval(data):
    """plots p-value based on hourly testing of running A/B test
    Parameters
    ----------
    data: Pandas DataFrame
        A/B testing storage DataFrame with columns 'hour' converted' and 'landing_page'
    Returns
    -------
    None: A plot is produced buy no axis object is returned
    """

    pval_lst = []
    datetime = data.ts.astype('datetime64[s]')
    hour = datetime.apply(lambda x: x.hour)
    data['hour'] = hour
    # Run the test as the data accumulates hourly
    for hr in hour.unique():
        hr_data = data[data['hour'] <= hr]
        # data for old landing page
        old = hr_data[hr_data['landing_page'] == 'old_page']['converted']
        old_nrow = old.shape[0]
        old_conversion = old.mean()
        # data for new landing page
        new = hr_data[hr_data['landing_page'] == 'new_page']['converted']
        new_nrow = new.shape[0]
        new_conversion = new.mean()
        # Run the z-test
        p_val = z_test(old_conversion, new_conversion,
                       old_nrow, new_nrow, effect_size=0.001,
                       alpha=.05)
        pval_lst.append(p_val[1])

    # Make the plot
    plt.plot(pval_lst, marker='o')
    plt.ylabel('p-value', fontweight='bold', fontsize=14)
    plt.xlabel('Hour in the day', fontweight='bold', fontsize=14)
    plt.axhline(0.05, linestyle='--', color='r')

