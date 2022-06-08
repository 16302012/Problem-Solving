# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:12:08 2022

@author: User
"""

def city_country(city, country, population=0):

    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string