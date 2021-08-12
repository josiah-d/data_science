"""
This file contains helper functions for scripts that make data.

Authors:
    Kin-Yip Chien <kin-yip.chien@galvanize.com>
"""
from pathlib import Path


def make_filepath(file:str, filedir: str = '') -> str:
    """
    Prepend filedir to filepath if filedir is a valid directory.

    Parameters
    ----------
    file : str
        File name.
    filedir : str, default=''
        File directory.

    Returns
    -------
    filepath : str
        File path.
    """
    filepath = file
    if filedir:
        # filedir must end with a forward-slash.
        if filedir[-1] != '/':
            filedir += '/'
        if Path(filedir).is_dir():
            filepath = filedir + file
        else:
            raise ValueError(
                f'{filedir} is not a valid directory.')
    return filepath