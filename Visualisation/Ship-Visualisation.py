#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Collin Reinking
#collin.reinking@berkeley.edu

import folium
import pandas as pd
import re
import os
import branca.colormap as cm
import re
import numpy as np
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from matplotlib import colors
#from scipy import stats


# In[6]:


data=pd.read_csv("/Users/zwt2000/Desktop/Ship_Visualisation/2018_Conainer_visData.csv")[["imo","lat_x","long_x","hour"]]
data = data[data["hour"]<169][data["long_x"]!= -99999.0][data["lat_x"]!= -99999.0]
data


# In[7]:


grouped_data_positions = data[["imo","lat_x","long_x"]]
grouped_data_positions



# In[ ]:


#create a map
this_map = folium.Map(prefer_canvas=True)

def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    folium.CircleMarker(location=[point.lat_x, point.long_x],
                        radius=0.5,
                        weight=2).add_to(this_map)

#use df.apply(,axis=1) to "iterate" through every row in your dataframe
grouped_data_positions.apply(plotDot, axis = 1)


#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())

#Save the map to an HTML file

this_map
this_map.save(os.path.join("/Users/zwt2000/Downloads/","location2.html"))


# In[ ]:




