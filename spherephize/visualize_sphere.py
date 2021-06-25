# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:51:58 2021

@author: Kath Landgren

This module contains the Sphere class and the visualization code
"""
import numpy as np
import plotly.graph_objects as go

class Sphere:
    """
    Class Sphere 
    
    Parameters
    ----------
    num_lat : int
        Positive integer, number of latitudes.
    num_lon : int
        Positive integer, number of longitudes.
    temp_type : string
        A string: "uniform", "zonal", or "custom".

    """
    
    #init method
    def __init__(self, num_lat,num_lon,temp_type):
        """Constructor method
        """
        
        
        np.seterr(divide='ignore', invalid='ignore') 
        self.num_lat=num_lat
        self.num_lon=num_lon
        self.temp_type=temp_type
        
        assert type(temp_type)==str, "Temperature type must be a string specifying accepted temperature types"
        
    def make_lat(self):
        """
        Creates an array of latitudes based on the number of latitudes

        Returns
        -------
        phi : array
            Array of latitudes from 0 to pi.

        """
        #creates an array of latitudes (phi)
        phi=np.linspace(0,np.pi,self.num_lat)
        self.phi=phi
        return phi
        
    def make_lon(self):
        """
        Creates an array of longitudes based on the number of longitudes

        Returns
        -------
        theta : array
            Array of longitudes from 0 to 2pi.

        """
        #creates an array of longitudes (theta)
        theta=np.linspace(0,2*np.pi,self.num_lon)
        self.theta=theta
        return theta
        
    def make_temp(self,custom_data="None",mean_temp=1000):
        """
        Creates the temperature field based on temperature type

        Parameters
        ----------
        custom_data : array, optional
            Custom temperature data. The default is "None".
        mean_temp : float, optional
            Mean temperature for the zonal and uniform temperature fields. 
            The default is 1000.

        Returns
        -------
        data : array 
            temperature field data

        """
        
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

        self.temp=data
        return data

    def get_temp(self):
        """
        Gets the temperature from the object of :class: 'Sphere'

        Returns
        -------
        temp : array
            temperature field assigned to the object.

        """
        temp=self.temp
        return temp

    
def make_hoverdata(x,y,z,input_temp):
    """
    Makes the data that appear when hovering over a point on a sphere,
    namely latitude, longitude, and the temperature value

    Parameters
    ----------
    x : array
        array of x coordinates for the sphere.
    y : array
        array of y coordinates for the sphere.
    z : array
        array of z coordinates for the sphere.
    input_temp : array
        temperature field

    Returns
    -------
    hoverdata : array
        Stack of latitude, longitude, and temperature field arrays

    """
    
    trunc_temp= input_temp.round(decimals=0)
    
    lats=np.arcsin(z)*180/np.pi
    lats=lats.round(decimals=1)
    
    lons=2*np.arctan(np.divide(y,(x**2+y**2)))*180/np.pi
    lons=lons.round(decimals=1)
    
    hoverdata=np.stack((lats.T, lons.T, trunc_temp.T), axis =-1)
    return hoverdata

def plot_sphere(planet,theta,phi,temp,cmin=700,cmax=1200,cscale='jet',save=False,name="None"):
    """
    This function creates the interactive visualization plot    

    Parameters
    ----------
    planet : object of class Sphere
        the planet
    theta : array
        longitudes.
    phi : array
        latitudes.
    temp : array
        temperature field data
    cmin : float, optional
        Lower bound on the colorbar, K. The default is 700.
    cmax : float, optional
        Upper bound on the colorbar, K. The default is 1200.
    cscale : string
        colormap to use
    save : bool, optional
        If true, save output as html. The default is False.
    name : string, optional
        Name of (or path to) html file

    Returns
    -------
    fig : figure
        

    """

    x = np.outer(np.cos(theta),np.sin(phi))
    y = np.outer(np.sin(theta),np.sin(phi))
    z = np.outer(np.ones(planet.num_lon),np.cos(phi))
    
    
    hoverdata=make_hoverdata(x,y,z,temp)
    #call plotly
    fig= go.Figure(go.Surface(x=x, y=y, z=z,surfacecolor=temp,cmax=cmax,cmin=cmin,colorscale=cscale,customdata=hoverdata,    hovertemplate ="lat: %{customdata[0]}"+\
                             "<br>lon: %{customdata[1]}"+\
                             "<br>temp:%{customdata[2]} K<extra></extra>", \
                             contours = {
         "x": {"show": True, "start": -1, "end": 1, "size": 1, "color":"black"},
        "y": {"show": True, "start": -1, "end": 1, "size": 1, "color":"black"},
        "z": {"show": True, "start": -1, "end": 1, "size": 1, "color":"black"}
    }))

    
    fig.update_layout(scene = dict(
                        xaxis = dict(
                             showbackground=False,visible=False),
                        yaxis = dict(
                             showbackground=False,visible=False),
                        zaxis = dict(
                             showbackground=False,visible=False)))
                      

    if save==1:
        fig.write_html(name+".html")
        
    return fig