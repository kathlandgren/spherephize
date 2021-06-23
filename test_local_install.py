# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:21:54 2021

@author: ek672
"""

import planetPlotly.visualize_sphere as p


#testPlanet=p.visualize_sphere.Sphere(10,20,"uniform")

test=p.Sphere(10,20,"uniform")

phi=test.make_lat()

theta=test.make_lon()

p.plot_sphere(test,theta,phi)



