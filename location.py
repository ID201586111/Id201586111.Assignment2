# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:05:02 2022

@author: dan-8

#This module will contain functions for main model
"""
#imports
import csv
import random

#Set the environment using raster text file
def get_data():
    #Add this data, to 2d list
    environment = []    #Make empty list before any processing done
    f = open('Bomb.txt', newline ='')
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist =[]     #Make new list before each row is processed
        for value in row:
            rowlist.append(value) #Append the values to the rowlist
        environment.append(rowlist)
    f.close()
    return (environment)


#Need to create agent class in order to move
#Make bacreria agents
class Agent():
    def __init__(self, environment, num_of_iterations):
        self.x = 51 #found from running step 1 in mainmodel.py
        self.y = 151#found from running step 1 in mainmodel.py
        self.environment = environment
        self.store = 0
        self.num_of_iterations = num_of_iterations

   
#move agents with wind direction probability
#N= 10% = 0.1
#E= 75% = 0.75
#S= 10% = 0.1
#W= 5% = 0.05


#Move agents: create a random number between 1-0 and use the probability to 
#move North (y+1), East (x+1), South (y-1) and West (x-1)
    def move(self):
        direction = random.random()
        #print(direction)
        if direction <= 0.05:
            self.x += -1
        elif 0.05 < direction <= 0.15:
            self.y += 1
        elif 0.15 < direction <= 0.25:
            self.y += -1
        else:
            self.x += 1
        #print (self.x)
        #print (self.y)
    
#Drop agents: create random number between 1-0 and use probability to drop.
#Above 74m: 20% chance agents moves up, 70% down and 10% stays same height    
    def drop(self, num_of_iterations):
   
        elev_chance = random.random()#possibly change to random0-1
        if self.num_of_iterations > 74:#tried 'when' but could not get to work
            if elev_chance <= 0.2: #20% go up
                self.num_of_iterations += 1
            elif elev_chance >0.2 and elev_chance <= 0.9: #70% go down
                self.num_of_iterations += -1 #no need for an else as iterations would stay same 10%
        if self.num_of_iterations <= 74:
            self.num_of_iterations += -1
        return (num_of_iterations) #returns tuple and number of iterations
    
#To create density each agent would +1 value to the environment where it lands    
    def density (self, environment):
        self.environment[self.y][self.x] += 1

