#!/usr/bin/env python
# coding: utf-8

# # Data analysis: Velib

# Author: O. Roustant, INSA Toulouse. January 2021.
# 
# We consider the ‘Vélib’ data set, related to the bike sharing system of Paris. The data are loading profiles of the bike stations over one week, collected every hour, from the period Monday 2nd Sept. - Sunday 7th Sept., 2014. The loading profile of a station, or simply loading, is defined as the ratio of number of available bikes divided by the number of bike docks. A loading of 1 means that the station is fully loaded, i.e. all bikes are available. A loading of 0 means that the station is empty, all bikes have been rent.
# 
# From the viewpoint of data analysis, the individuals are the stations. The variables are the 168 time steps (hours in the week). The aim is to detect clusters in the data, corresponding to common customer usages. This clustering should then be used to predict the loading profile.
# 

# In[1]:


import pandas as pd
path=''  # si les données sont déjà dans le répertoire courant
loading = pd.read_csv(path+'velibLoading.csv', sep = " ")
loading.head()


# In[2]:


velibAdds = pd.read_csv(path+'velibAdds.csv', sep = " ")
velibAdds.head()


# In[3]:


# Plot the loading of the first station
get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import * 
import numpy as np

p = loading.columns.size
Time = np.linspace(1, p, p)
plot(Time, loading.transpose()[1], linewidth = 2, color = 'blue')
xlabel('Time'); ylabel('Laoding'); title(velibAdds.names[1])
vlines(x = np.linspace(1, p, 8), ymin = 0, ymax = 1, colors = "black", linestyle = "dotted")
show()


# # Descriptive statistics.
# 
# Some ideas : 
# 
# 1. Draw a matrix of plots of size 4*4, corresponding to the first 16 stations. (Do not forget the vertical lines corresponding to days).
# 2. Draw the boxplot of the variables, sorted in time order. 
# What can you say about the distribution of the variables? 
# Position, dispersion, symmetry?
# 3. Investigate the temporal correlation of the variables. 
# For instance, for a given station, plot the loading at t+h versus loading at time t.
# Visualize the correlation matrix by an image plot. Interpret the result.
# 4. Plot the stations coordinates on a 2D map (latitude versus longitude). Use a different color for stations which are located on a hill.
# 5. Redo questions 1-3 for the subset of stations which are located on a hill. Same questions for those who are not. Comment?
