import numpy as np
import pandas as pd


def get_counts_dataframe(number_array):
    """Takes an array with possible repeats
    and returns a dataframe with two
    columns: values in the array and counts of
    each value.
    """
    number_array = number_array.round(0)
    vals, counts = np.unique(number_array, return_counts=True)
    results_df = pd.DataFrame({'values': vals, 'counts': counts})
    results_df['values'] = results_df['values'].astype('int')
    return results_df
