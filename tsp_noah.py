#!/usr/bin/env python

from random import choice
from numpy import array

cities = ["A", "B", "C", "D"]
dtype = [('city_start', 'S10'), ('city_end', 'S10'), ('distance', int)]
values = [
    ["A", "A", 0],
    ["A","B",1],
    ["A","C",10],
    ["A","D",1],
    ["B","A",1],
    ["B","B",0],
    ["B","C",1],
    ["B","D",10],
    ["C","A",10],
    ["C","B",1],
    ["C","C",0],
    ["C","D",1],
    ["D","A",1],
    ["D","B",10],
    ["D","C",1],
    ["D","D",0]
]
param = array(values,dtype=dtype)

def all_cities(mdarray):
    """Takes a multi-dimensional array in this format and finds unique cities
    
    array([["A", "A"],
    ["A", "B"]])
    
    """
    
    city = []
    farray = mdarray.flatten()
    for item in set(farray):
        try:
            eval(item)
        except NameError:
            city.append(item)
    return city
    
def randomize_city_start(all_cities):
    """Returns a randomized city to start trip"""
    
    return choice(cities)

def greedy_path(cities):
    """Select the next path to travel based on the shortest, nearest path"""

    route = []
    while True:
        try:
            city = cities.pop(0)
            route.append(city)
        except IndexError:
            break
    return route

def main():
    """runs everything"""
    unique_cities = all_cities(param)
    print unique_cities
    starting_city = randomize_city_start(unique_cities)
    #print "starting city: %s" % starting_city
    print greedy_path(starting_city)

if __name__ == '__main__':
   main()