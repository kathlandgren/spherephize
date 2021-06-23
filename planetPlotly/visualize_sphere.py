# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:51:58 2021

@author: ek672

This is the planet-plotly module
"""
import pandas as pd
import numpy as np
import plotly.graph_objects as go

class Sphere:
    
    #init method
    def __init__(self, num_lat,num_lon,temp_type):
        self.num_lat=num_lat
        self.num_lon=num_lon
        self.temp_type=temp_type
        
    def make_lat(self):
        #creates an array of latitudes (phi)
        phi=np.linspace(0,np.pi,self.num_lat)
        return phi
        
    def make_lon(self):
        #creates an array of longitudes (theta)
        theta=np.linspace(0,2*np.pi,self.num_lon)
        return theta
        
    def make_temp(self,custom_data="None",mean_temp=1000):
        #creates the temperature field
        
        if self.temp_type=="uniform":
            #creates uniform temperature field
            data=mean_temp*np.ones((self.num_lon,self.num_lat))

        elif self.temp_type=="zonal":
            #creates zonal temperature field
            lat=self.make_lat()
            data=np.sin(lat)*mean_temp*np.ones((self.num_lon,self.num_lat))
            
        
        elif self.temp_type=="custom":
            #uses an array
            data=custom_data
            
        return data
    
    
def plot_sphere(planet,theta,phi):
    """
    This function creates the interacti
    """
    x = np.outer(np.cos(theta),np.sin(phi))
    y = np.outer(np.sin(theta),np.sin(phi))
    z = np.outer(np.ones(129),np.cos(phi))

    temp=planet.make_temp()

    x = np.outer(np.cos(theta),np.sin(phi))
    y = np.outer(np.sin(theta),np.sin(phi))
    z = np.outer(np.ones(planet.num_lon),np.cos(phi))
    
    #call plotly
    fig= go.Figure(go.Surface(x=x, y=y, z=z,surfacecolor=temp,cmax=1200,cmin=700,colorscale='jet'))
    
    fig.update_layout(scene = dict(
                        xaxis = dict(
                             showbackground=False,visible=False),
                        yaxis = dict(
                             showbackground=False,visible=False),
                        zaxis = dict(
                             showbackground=False,visible=False)))
                      
    fig.show()