# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:55:42 2022

@author: dan-8

This project will produce a density map showing bacteria fallout from a 
biological weapon. It will bring in a map of the area as a text file (bomb.txt)
which contains the point at which the bomb has been let off and plot where 
the bacteria particles will land.
 
The project will create 5000 particles from the bomb position and using known 
probabilities of wind direction, and the rate at which they will fall from 
the sky; plot where each particle will land and create a density map of the 
area, which will be exported as a text file.


Step 1: Pull in the data file and find the bomb location.

Step 2: Calculate where 5000 bacteria will end up.

Step 3: Draw a density map of where all the bacteria end up as an 
image and displays it on the screen.

Step 4: Save the density map to a file as text.

"""
#imports
import matplotlib.pyplot as plt
import time
import csv
import itertools

#import module
import location

#start the timer
start = time.process_time()


#test 
#a = "hello world"
#print(a)
'''
First step import bomb location raster and display
'''

#set environment from location.py using a 300x300 grid (image is 300x300)
environment = location.get_data()

#Get Bomb Location- x/y
#create empty list for coords
bomb=[]

#set x and y to point in grid where location is '255'
y = []
x = []

for i in range(len(environment[:])):
    for j in environment[i]:
        if j ==255:
            y.append(i)
x = [index for (index, item) in enumerate(environment[y[0]]) if item == 255]

#doesn't take '0' row and column into account so +1 to x/y value will fix this.
x_coord = [i + 1 for i in x]
y_coord = [i + 1 for i in y]

#print(x_coord, y_coord) x = 51, y =151 input these values into agent

#put into empty bomb list, as coordinates
bomb = [(x, y) for x in x_coord for y in y_coord]
print ('Bomb at Coordinates:', bomb)

'''
Step 2: Make the bacteria agents and move them with wind:
5% chance that in any given second, particle will blow west
10% chance of blowing north or south
75% chance of blowing east.
1 iteration = 1 second, particle move at 1 pixel (1 meter) a second.

NOTE to work out how particles fall:
Building is 75m at 1 pixel per second = 75 iterations of the module.
However if the particle is at/above the height of the building- 20% chance each
second it will rise by a metre in turbulance, a 10% chance it will stay at 
the same level, and an 70% chance it will fall. 
Below the height of the building there is no turbulance, and the particles 
will drop by a metre a second. 
'''

#Make bacteria agents try get it to work with 10 then make 5000 at end.
num_of_agents = 5000
num_of_iterations = 75
agents =[]
for i in range(num_of_agents):
    agents.append(bomb)
#print ('agents are:', agents) #Makes a list of agents in seperate lists

#make into 1 list with multiple coords for bacreria 
coords = list(itertools.chain.from_iterable(agents))
#print (coords)
#print (coords[0])#test print the first set of coords


'''
So now have the bacteria agents time to move them.
'''
#Note: plt was moved to this positon as I was stuggling to get the new
#Environment to draw on grid (original position in step 3)
plt.xlim(0, 300)
plt.ylim(0,300)
plt.xlabel('Easting')
plt.ylabel('Northing')
plt.title('Bacteria Bomb Fallout')#found labels using matplotlib.org- tutorials

#Move Bacteria Agents
bacteria =[]
for i in range (num_of_agents):
    bacteria.append(location.Agent(environment, num_of_iterations))
for i in range (num_of_iterations):
    for i in range (num_of_agents):
        if num_of_iterations > 0: #this will stop the agents at 'floor'
            bacteria[i].move()#Moves N, E, S, W
            bacteria[i].drop(num_of_iterations)#Drops agents from 75m
for i in range (num_of_agents):
#    print (bacteria[i].x, bacteria[i].y)
    bacteria[i].density(environment)#Step 3 please read below
    
'''   
Note: when stuggling to show the new environment to check if the 'move'
process had worked, I run a print on 'environemt' and copied the result into
a text file and manualy checked if cells had been changed.
'''
#print(environment)

'''
Step 3: Create density map and show on screen
'''
#Density Map where agents drop

#for i in range (num_of_agents):
#    bacteria[i].density(environment)#moved into step 2
'''
Could not get the environment to update with new values for density plot
Tried drawing the plot above moving agents and showing the environment after.
Got it to work after integrating step 3 into step 2.
'''

plt.imshow(environment)
plt.show()

'''
Step 4: Export density map as text file
'''
#Write Environment as text file using csv writer.
write_environment= open("Bacteria_Density.txt", "w", newline='')#blank txt file
writer  =csv.writer(write_environment, delimiter= ",")
#Write each row in the environment
for row in environment:
    writer.writerow(row)
write_environment.close()

#end timer
end = time.process_time()
print ("time= " +str(end - start))