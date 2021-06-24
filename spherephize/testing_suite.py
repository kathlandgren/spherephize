# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:33:34 2021

@author: ek672
"""

import visualize_sphere as vs


def test_sphere_class():
    """
    This tests the constructor methon of the sphere class

    Returns
    -------
    None.

    """
    planet=vs.Sphere(10,20,"zonal")
    
    assert planet.num_lat==10, "Wrong latitudes"
    assert planet.num_lon==20, "Wrong latitudes"
    assert planet.temp_type=="zonal", "Wrong temperature type"
    
    pass
    
def test_
