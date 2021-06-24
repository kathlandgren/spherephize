# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 18:37:18 2021

@author: ek672
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import math



def import_csv(path):
    """
    Reads the .csv file as a pandas data frame and returns the values

    Parameters
    ----------
    path : string
        Path to the .csv data to be imported.

    Returns
    -------
    array
        numpy array of the data read

    """
    df=pd.read_csv(path)
    return df.values

def make_theta(longitudes):
    """
    Converts the imported longitudes to the necessary format for plotly

    Parameters
    ----------
    longitudes : array
        An array of longitudes.

    Returns
    -------
    theta : array
        An array of longitudes realy to be imported.

    """
    if longitudes[0]==0 & longitudes[-1]==2*np.pi:
        theta=longitudes
    else:
        theta = longitudes + np.pi
        theta= np.append(theta,2*np.pi)
        theta = np.insert(theta,0,0)
        
    return theta

def fill_in_data(temp_data):
    """
    Fills in the data gap to make sure the sphere is plotted continuously.

    Parameters
    ----------
    temp_data : array
        Temperature field data

    Returns
    -------
    input_temp : array
        Temperature filled with the gap filled in.

    """
    to_append = (temp_data[:,0] + temp_data[:,-1])*0.5
    to_append = to_append.reshape((len(to_append),1))
    temp = np.append(temp_data,to_append,axis=1).T
    return temp