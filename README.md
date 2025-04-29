# DS 5100 Final Project
## **A Monte Carlo Simulation Game & Stats**
<img src="https://github.com/virginia-vrb9e/DS5100-project-repo/blob/main/mcd/d20_met_nyc.jpg" width=200 height=200 align='left'>

### Purpose
 This is the end of semester final project for UVA School of Data Science course DS 5100, Programming for Data Science. Our purpose was to create a simple Monte Carlo Simulator using a set of three related classes 
 - a die class named *MonCarloDevice*,
 - a game class named *MonCarloGame*, and
 - an analyzer class called *MonCarloAnalyzer*.  

 The simulator allow a user to create one or more die objects with weighted sides to simulate rolls where dies can be rolled and results are provided. 
#### Notes about language
 - **die**: Please note that the word 'die' will refer to any discrete random variable assoicated with a stochastic process (e.g. rolling an actual die, flipping a coin, or speaking a language)
.
 - **face**: 'face' refers to one of the discrete random variables of the device created.  One can imagine the 'faces' of a die.
 - **xx**:

### METADATA
### Package Information:
- **Name**: moncarlo
- **Version**: 1.0
- **Release Date**: April 29, 2025
- **License**: MIT
- **Python Compatibility**: Tested in Python 3.12.5
### Necessary Packages:
- numpy
- pandas
- matplotlib
### Installation:
{bash} pip install moncarlo

### SYNOPSIS
This Python module consists of three classes that work together in sequence to simulate a Monte Carlo device. There is no parent class, per se, but the classes are called in this sequence:

[die class] --> [game class] --> [analyzer class], 

wherein products from the previous class are used to initiate the next class in the sequence. 

### *MonCarloDevice*
The first class in the sequence is called *MonCarloDevice*.  It represents a die or group of random variables associated with a stochastic process.  
#### Instantiation:
It initializes with a numpy array of either strings or numbers that must be unique values in the array. 
#### Additional Methods: 
After instantiation, the user can either 
- roll the dice, or
- change the weight of one side to create an 'unfair' die. 

### *MonCarloGame*
#### Instantiation:
#### Additional Methods: 

### *MonCarloAnalyzer*
#### Instantiation:
#### Additional Methods:

SHowing how each class is called:
- what the class does
- how to initialize it 
- examples of method calls
- sample code snippets showing syntax

## API Reference

## MonCarloDevice (die class)

    Actions: This class creates a game object/device for a Monte Carlo simulation.
    
    Instantiation: requires a numpy array of sides for the device
            - must be a NumPy array
            - sides or faces must be unique
            - sides can be numbers or strings

### Methods:

        __init__: 
            instantiates a game device with the given np.array
              - creates a game device with the face values of the array 
              - and a default face weight of 1.0
Input:              
| Parameter | Type       | Description                                                             |
| :-------- | :--------- | :---------------------------------------------------------------------- |
| `faces`   | `np.array` | **Required**. must be a NumPy array of unique values, either int or str |


        change_facewt: 
            changes the weight of a specified side to create an unfair die
              - takes 2 arguments: 
              (1) the face value to be changed  
              (2) the new face-weight 
 Input:              
| Parameter | Type            | Description                                                                |
| :-------- | :-------------- | :------------------------------------------------------------------------- |
|  `face`   | `string or int` | **Required**. must match one of the face values of the instantiated object |
|   `nwt`   | `int or float`  | **Required**. must be an int or float                                      |


        roll: 
            rolls the die
              - takes integer parameter of how many times to roll the die (defaults to 1)      
Input:              
| Parameter | Type  | Description                      |
| :-------- | :-----| :------------------------------- |
| `nrolls`  |  `int`| **Required**. must be an integer |


        current_state: 
              returns the die's current state as a pandas dataframe
Input: 
| Parameter | Type     | Description  |
| :-------- | :------- | :----------- |
|   none    |   na     |   na         |

## MonCarloGame (game class)

    Action: Creates a game out of one or more instantiated game devices with identical faces
            - rolls the dice all together
            - shows user the results of the most recent roll/play
    
    Instantiation:
            - one or more game devices created with the MonCarloDevice class

### Methods:

        __init__
            takes a single parameter:
                - a list of already instantiated game devices with identical faces
Input:              
| Parameter | Type  | Description                                                          |
| :-------- | :-----| :------------------------------------------------------------------- |
|  `dice`   | `list`| **Required**. must be list of objects instantiated by MonCarloDevice |


        play:
            takes an integer parameter for # of times the device(s) are to be rolled
                - int()
            saves the result of the play to a pandas dataframe
Input:              
| Parameter | Type   | Description     |
| :-------- | :------| :-------------- |
|  `nrolls`   | `int`| **Default = 1** |


        show_results:
            takes a single parameter:
                - string: 'wide' or 'narrow'
                - indicates the format of the returned data
            returns the results of the play in the chosen format
Input: 
| Parameter | Type     | Description  |
| :-------- | :------- | :----------- |
|   none    |   na     |   na         |


## MonCarloAnalyzer (analyzer class)
    
    Action:
        Takes the results of a single MonCarloGame and computes descriptive statistical properties about it
        
    Instantiation:
        - a single game object created with the MonCarloGame class
 
### Methods: 
    
        __init__:
            game object as input parameter
Input:              
| Parameter | Type                      | Description                                                          |
| :-------- | :-------------------------| :------------------------------------------------------------------- |
|  `game`   | `instantiated game object`| **Required**. must be one instantiated game object from MonCarloGame |


        jackpot: (all faces of all devices are the same)
            - takes no additional parameters
            - computes how many times the game resulted in a jackpot
            - returns an integer 
Input: 
| Parameter | Type     | Description  |
| :-------- | :------- | :----------- |
|   none    |   na     |   na         |


        facecounts_per_roll:
            - computes how many times a given face is rolled in each event
            - returns a pandas dataframe of results
Input: 
| Parameter | Type     | Description  |
| :-------- | :------- | :----------- |
|   none    |   na     |   na         |


        combos:
            - computes the distinct combinations of faces rolled, along with their counts
Input: 
| Parameter | Type     | Description  |
| :-------- | :------- | :----------- |
|   none    |   na     |   na         |


        permutations:
            - computes the distinct permutations of faces rolled, along with their counts
Input: 
| Parameter | Type     | Description  |
| :-------- | :------- | :----------- |
|   none    |   na     |   na         |


### Author
- [@virginia-vrb9e (https://github.com/virginia-vrb9e)]
 
### Thanks
- []