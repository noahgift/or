#!/usr/bin/env python

from random import choice
import numpy as np

cities = ["A", "B", "C", "D"]
dt = np.dtype([('city_start', 'S10'), ('city_end', 'S10'), ('distance', int)])
values = [
    ("A","B",1),
    ("A","C",3),
    ("A","D",5),
    ("B","A",1),
    ("B","C",7),
    ("B","D",9),
    ("C","A",13),
    ("C","B",15),
    ("C","D",4),
    ("D","A",6),
    ("D","B",8),
    ("D","C",4),
]
data_set = np.array(values,dtype=dt)

def all_cities(mdarray):
    """Takes a multi-dimensional array in this format and finds unique cities
    
    array([["A", "A"],
    ["A", "B"]])
    
    """
    cities = {}
    city_set = set(data_set['city_end'])
    for city in city_set:
        cities[city] = ""
    return cities
    
def randomize_city_start(all_cities):
    """Returns a randomized city to start trip"""
    
    return choice(cities)

def get_shortest_route(routes):
    """Sort the list by distance and return shortest distance route"""

    route = sorted(routes, key=lambda dist: dist[2]).pop(0)
    return route

def greedy_path():
    """Select the next path to travel based on the shortest, nearest path"""

    itinerary = []
    cities = all_cities(data_set)
    starting_city = randomize_city_start(cities.keys())
    cities_visited = {}
    #we want to iterate through all cities once
    count = 1
    while True:
        possible_routes = []
        distance = [] 
        print "starting city: %s" % starting_city
        for path in data_set:
            if starting_city in path['city_start']:
                #we can't go to cities we have already visited
                if path['city_end'] in cities_visited:
                    continue
                else:
                    print "path: ", path
                    possible_routes.append(path)
        
        if not possible_routes:
            break
        #append this to itinerary
        route = get_shortest_route(possible_routes)
        print "Route(%s): %s " % (count, route)
        count += 1
        itinerary.append(route)
        #add this city to the visited city list
        cities_visited[route[0]] = count
        print "cities_visited: %s " % cities_visited
        #reset the starting_city to the next city
        starting_city = route[1]
        print "itinerary: %s" % itinerary
    
    return itinerary

def get_total_distance(complete_itinerary):
    
    distance = sum(z for z,y,z in complete_itinerary)
    return distance

def main():
    """runs everything"""
    
    print "All Routes: %s" % data_set
    itinerary = greedy_path()
    print "Distance: %s" % get_total_distance(itinerary)

if __name__ == '__main__':
   main()