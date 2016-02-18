#!/usr/bin/env python
"""
    :module: color range
    :platform: omni
    :synopsis: This module returns color range values that camn be used to color objects
    :plans: none
"""
__author__ = "Andres Weber"
__edited_by__ = "michael Nieves"
__email__ = "michaelanieves@gmail.com"
__version__ = 1.0

class ColorRange(object):
    def __init__(self, rgb):
        self.r, self.g, self.b = rgb
    
    def get_range(self, num, min = 0.00, max =.4):
        max = [max]*3 if (isinstance(max, float) or isinstance(max, int)) else max
        min = [min]*3 if (isinstance(min, float) or isinstance(min, int)) else min
        vals = []
        
        for component, max_component, min_component in zip([self.r, self.g, self.b], max, min):
            component_list = []
            cur_val = component if not min_component > component else min_component
            min_component = cur_val
            
            incr = (max_component - min_component) / (float(num)-1)
            
            for n in range(0, num):
                component_list.append(cur_val)
                cur_val += incr
            vals.append(component_list)
            
        colors = []
        for r,g,b in zip(vals[0], vals[1], vals[2]):
            colors.append([r,g,b])
        
        return colors