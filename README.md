# Id201586111.Assignment2
 Geog5003-Assignment2

Title: GEOG5003M Assignment 2, Bacterial Bomb Density Map Model

Contents:
•	.gitattributes - automatically created by github for repository.

•	Bacteria_Density.txt - An example of the text file created by the model which features the new environment with density values.

•	bomb.txt - Raster file as text document. Contains environment (0s), with bomb location (255).

• LICENSE - MIT license file- short/simple permissive license. Conditions only requiring preservation of copyright & license notices stipulates the open source licence for code.

•	README.md - THIS File which provides instructions and overview for the project.

•	location.py - the module which is used by the main model.py. Called location due to the initial model using it to find location of bomb.

•	mainmodel.py - the main code which runs the model.


Description:
The project creates a pop out window showing a density study for 5000 bacteria particles (agents) in an environment from 1 starting position in the bomb.txt file.
These agents have been moved in directions according to the wind which was given a pre-determined probability: 5% chance that in any given second, a particle will blow
west, a 10% chance of blowing north or south, and a 75% chance of blowing east. One model iteration is one second, and for each model iteration the longest potential
movement is one pixel on screen, which is 1 metre in length. Also, the 'drop rate' of the particles has been taken into account: The building is 75m high, if the
particle is above the height of the building there is a 20% chance each second it will rise by a metre, a 10% chance it will stay at the same level, and 70% chance
it will fall. Below the height of the building there is no turbulence, and the particles will drop by a metre a second, ending at 0m.
These new positions of the agents are plotted onto the environment returning a 300x300 grid showing bomb location and bacteria agent density. The model also exports
this new environment as a text file.

'location.py' is an object-oriented code which encapsulates the agents' properties and behaviour, as well as the agents' environment. This framework code is used by
the 'mainmodel.py'. In 'locaton.py' the environment is defined as 'get_data', creating an empty list and a new list for each row of values in the environment. This was
initially used to simply find the location of the bomb. However more functions were added to code; class 'Agent' is defined creating self.x and self.y using the
coordinates of the bomb. Also, the code defines 'move' which moves the agents N (y+1), E (x+1), S (y-1) and W (x-1) using a random number between 0-1 and calculating
the probability of the wind for each direction. 'drop' is also defined to drop the agents from 75m. Again by creating a random number between 0-1 and use probability
to drop- above 74m: 20% chance agents moves up, 70% down and 10% stays same height and randomly moves x and y by 1 unit. This is carried out for the number of agents.
'location.py' also contains code that defines 'density' which allows the agents to interact with the environment: adding 1 value to the environment where each agent
lands.

'mainmodel.py' is the main model and is the code that the user can run. The model has a timer which starts before the first line of code and ends after the last line
of code for the model, printing 'time=' and the time the code took to process. The environment is set from 'location.py' the first step finds the location of the bomb
printing 'Bomb Coordinates: x,y'. These coordinates are then input into the Agent class in 'location.py' as self.x and self.y. The user can control how many bacteria
agents are plotted (num_of_agents) and how high the building is (num_of_iterations). Next using nested loop, and the bacteria agents can be moved, dropped and the
density plotted over the environment, using functions called from 'location.py. The new environment is then plotted over a 300x300 grid and shown using 'matplotlib'.
The last step is for the new environment to be exported as a text file using 'fileinput.input' which writes files. The raster text file contains comma separated
variable data, each value being equivalent to a pixel in an image- the higher the value the higher the density of bacteria agents.

How to Run/Use Project: 
Download the three files; 'mainmodel.py', 'location.py' and raster data (bomb.txt). 'mainmodel.py' will be the file where you can change the inputs, 'location.py'
should not be edited unless you are changing the raster file for the environment. If you have a new bomb location (value = 255) you can called it bomb.txt and the
model will provide you with a new set of x and y coordinates which must then be input into the 'Agent' class for 'self.x and 'self.y'in the 'location.py. The number of
bacteria agents and height of building can be altered in 'mainmodel.py'- num_of_agents/num_of_iterations.

Credits: Student ID: 201586111 Using code from University of Leeds, MSc, GEOG5003M.

Testing: The model was tested throughout using the timer to try and optimise the code and debugging to solve any issues. More information on testing and issues cn be
found in suplementry Msft Word document - GEOG5003_Ass2_201586111.docx

