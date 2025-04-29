import numpy as np
import pandas as pd
import PIL
import urllib.request
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# The Die class
class MonCarloDevice:
    """
    Purpose/Action:
        This class creates a game object/device for a Monte Carlo simulation. 
    
    Input:
          - takes a numpy array of sides for the device
              - sides must be unique
              - sides can be numbers or strings
    Methods:
        __init__: 
            instantiates a game device with the given np.array
              - creates a game device with the face values of the array 
              - and a default face weight of 1.0
      
        change_facewt: 
            changes the weight of a specified side to create an unfair die
              - takes 2 arguments: 
              (1) the face value to be changed  
              (2) the new face-weight
              
        roll: 
            rolls the die
              - takes integer parameter of how many times to roll the die (defaults to 1)
          
        current_state: 
              returns the die's current state as a pandas dataframe
    """
    img = np.array(PIL.Image.open(urllib.request.urlopen('https://images.metmuseum.org/CRDImages/eg/original/10.130.1158_001.jpg')))
    plt.imshow(img)
    print("THE MET Museum: \n\nicosahedron with faces inscribed with Greek letters \nPtolemaic Period–Roman Period\n(2nd century \
    B.C.– 4th century A.D.)\n")
    print("Read about this ancient Monte Carlo device:\nhttps://www.metmuseum.org/art/collection/search/551072")
    
    def __init__(self, faces):
        """instantiates the monte carlo device""" 
        self.faces = faces
        print(type(faces))

        if not isinstance(faces, np.ndarray):  
            raise TypeError("Input of faces must be an NumPy array.") 
        else:
            print("yes, this is an np.ndarray!")  # production only; take out at the end
            
        x = len(self.faces)
        for i in range(x):
            if not isinstance(self.faces[i], (str)):
                float(i)
                print("switched to float")  # production only; take out at the end 
            else:
                print("check ok.") # production only; take out at the end   
                
        uniq = np.unique(faces)  
        if len(uniq) != len(faces):
            raise ValueError("The array of faces must be of unique values.")

        # initiate the weights as 1.0   
        self.weights = []
        self.num_faces = len(faces)
        x = len(self.faces)
        
        for i in range(x):
            self.weights.append(1.0)    

        col_names = ['weights']
        self._gamestats = pd.DataFrame(
            self.weights,
            index = self.faces, 
            columns = col_names
        ).rename_axis(index ='faces')
        

    def change_facewt(self, face, nwt):
        """
        changes the weight of one of the faces of the created game device
        input must a face on the instantiated device and the new weight must be an integer
        """
        self.nwt = nwt
        self.face = face

        is_in = np.isin(self.faces, self.face)  # simplify this!
        for f in is_in:
            if self.face not in self.faces: 
                raise IndexError(f"{face} is not a face on this device.")
            else:
                print("check okay: that face exists.") # production only; take out later
                

        if not isinstance(nwt, (int, float)):
            try:
                nwt = float(nwt)  
            except:
                raise TypeError("New weight must be numeric.")
    
        self.nwt = {'weights' : nwt}
        df_dict = self._gamestats.to_dict('index')
        df_dict[self.face] = self.nwt
        self._gamestats = pd.DataFrame.from_dict(df_dict, orient = 'index')


    def roll(self, nrolls = 1):
        """rolls the instantiated game device a specific number of times"""
        rolls = []
        for i in range(nrolls):
            sample = self._gamestats.sample(replace = True)
            face = sample.index[0] 
            rolls.append(face)  
        return rolls
    
    # method: show die's current state
    def current_state(self):
        """shows the game device's current state with its faces and face-weights"""
        print(self._gamestats)
        

# The Game class
class MonCarloGame: 
    """
    Purpose:
        Creates a game out of one or more instantiated game devices with identical faces:
    
    Input:
        - one or more game devices created with the MonCarloDevice class
        
    Actions: 
        - rolls the dice together
        - shows the user the results of the most recent roll/play
        
    Methods:
        __init__
            takes a single parameter:
                - a list of already instantiated game devices with identical faces
       
        play:
            takes an integer parameter for # of times the device(s) are to be rolled
                - int()
            saves the result of the play to a pandas dataframe
        
        show_results:
            takes a single parameter:
                - string: 'wide' or 'narrow'
                - indicates the format of the returned data
            returns the results of the play in the chosen format
    """

    def __init__(self, dice): 
        """instantiates MonCarloGame with the list of MonCarloGame objects"""
        self.dice = dice
        
    def play(self, nrolls):
        """ rolls the game device(s) for a play"""
        assert isinstance(nrolls, int) 
        results_of_play = {} 
    
        for index, die in enumerate(self.dice):
            results_of_play[index] = die.roll(nrolls)
        
        self._rolls = pd.DataFrame(
            results_of_play
        ).rename_axis(index='roll_#')
        return self._rolls
    
    def show_results (self, format = 'wide'):
        """ returns the result of the play in 'wide' or 'narrow' format"""
        if format not in['wide', 'narrow']:
            raise ValueError(f"{format} is not a valid entry. Select 'narrow' or 'wide'.") 
            
        if format == 'wide':
            return self._rolls.copy()
        # narrow: MultiIndex (roll# and die#)+ single column with outcome
        # wide to narrow with stack() -- can also unstack()
        elif format == 'narrow':
            df_n = self._rolls.stack()
            df_n.index.names = ['roll_#' , 'die_#']
        return df_n
    
    
# The Analyzer class
class MonCarloAnalyzer:
    """
    Purpose/Action:
        Takes the results of a single MonCarloGame
        computes descriptive statistical properties about it.
        
    Input:
        - one game object createa with the MonCarloGame class
        
    Methods:
        __init__:
            game object as input parameter
            
        jackpot: (all faces of all devices are the same)
            - takes no additional parameters
            - computes how many times the game resulted in a jackpot
            - returns an integer 
        
        facecounts_per_roll:
            - computes how many times a given face is rolled in each event
            - returns a pandas dataframe of results
            
        combos:
            - computes the distinct combinations of faces rolled, along with their counts
            
        permutations:
            - computes the distinct permutations of faces rolled, along with their counts
    """
    def __init__(self, game):
        """instantes the class with one MonCarloGame object"""
        if not isinstance(game, MonCarloGame):
            raise ValueError("Must pass a MonCarloGame object to initiate.")
        self.game = game
        self.df = self.game.show_results()
    
    def jackpot(self):
        """computes how many times the game resulted in a jackpot"""
        jackpot = (self.df.nunique(axis=1)==1)
        num_jackpots = sum(jackpot == True)
        return int(num_jackpots)
    
    def facecounts_per_roll(self):
        """computes how many times a given face is rolled in each event, or the raw frequencies of each face."""
        df_rawcounts = self.df.apply(pd.Series.value_counts, axis = 1)
        df_rawcounts = df_rawcounts.fillna(0)
        df_rawcounts.index.name = 'roll_#'
        return df_rawcounts
    
    # method: combo count
    def combos(self):
        """ computes the distinct combinations of faces rolled, along with their counts """
        pass
    
    
    # method: permutation count
    def permutations(self):
        """computes the distinct permutations of faces rolled, along with their counts"""
        pass

    def plot_results(self):
        """plots results using the states stored in the analyzer object (self)"""
        prob_model = pd.Series({i + 1:round(p,2) for i, p in enumerate(self.weights)})
        print("Rolls: ", self.nrolls)
        self._rolls.value_counts().sort_index().plot.bar(rot=0);
        
        