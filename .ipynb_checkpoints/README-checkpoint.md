
# DS 5100 Final Project
## A Monte Carlo Simulation Game & Stats
This is the end of semester final project for **UVA School of Data Science** course *DS 5100,* *Programming for Data Science*. 

Our purpose was to create a simple **Monte Carlo Simulator** using a set of three related classes - a die class named *'MonCarloDevice'*, A game class named *MonCarloGame'*, and an analyzer class called *'MonCarloAnalyzer'*.

The games allow a user to create one or more die objects with weighted sides to simulate rolls where dies are rolled and results are provided. 

**NOTE:   'die' refers to any discrete random variable assoicated with a stochastic process (e.g. rolling an actual die, flipping a coin, or speaking a language.)**


## Author

- [@virginia-vrb9e (hhttps://github.com/virginia-vrb9e)]


## Synopsis
This Python module consists of three classes that work together in sequence to simulate a Monte Carlo device. There is no parent class, per se, but the classes are called in this sequence:

[die class] --> [game class] --> [analyzer class]

wherein products from the previous class are used to initiate the next class in the sequence. 

#### Calling the die class: 'MonCarloDevice'

The first class in the sequence is called MonCarloDevice.  It represents a die or group of random variables associated with a stochastic process.  It initializes with a numpy array of either strings or numbers that must be unique values in the array. After instantiation, the user can either roll the dice, or change the weight of one side to create an 'unfair' die. 







SHowing how each class is called:
- what the class does
- how to initialize it 
- examples of method calls
- sample code snippets showing syntax

## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

