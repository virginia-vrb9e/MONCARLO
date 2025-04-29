import numpy as np
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# The Die class
class MonCarloDevice:
    """
    1. creates a game
    2. takes N, a number of sides for the Monte Carlo device where N<=20
    3. ...
    """
    
    img = mpimg.imread('d20_met_nyc.jpg')
    plt.imshow(img)
    print("THE MET Museum: \n\nicosahedron with faces inscribed with Greek letters \nPtolemaic Period–Roman Period\n(2nd century \
    B.C.– 4th century A.D.)\n")
    print("Read about this ancient Monte Carlo device:\nhttps://www.metmuseum.org/art/collection/search/551072")
    

    def __init__(self, faces):
        
        """ 
        This initializer:
        
        (1) takes a NumPy array (of dtype string or numbers) of DISTINCT faces as an argument. 
            - throws a TypeError if it is not a NumPy array
            - checks to see if the array values are distinct - ValueError if not
            
        (2) initializes an MC object with a default value for weights, W = 1.0.
        
        (3)Returns a private dataframe with the faces of the MC object as index.
        """
            
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
#        self.weights.extend(1.0 * x)...  # maybe replace loop with comprehension or other... 
    

        col_names = ['weights']
        self._gamestats = pd.DataFrame(
            self.weights,
            index = self.faces, 
            columns = col_names
        ).rename_axis(index ='faces')
        

    def change_facewt(self, face, nwt):
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
        df_dict['self.face'] = self.nwt
        self._gamestats = pd.DataFrame.from_dict(stat_dict, orient = 'index')
        print(self._gamestats()) # production only; take out at the end


    def roll(self, nrolls = 1):
        rolls = []
        for i in range(nrolls):
            sample = self._gamestats.sample(replace = True)
            face = sample.index[0] # selecting index value from the multiindex structure returned in the list!
            rolls.append(face)  
        return rolls
    
    # method: show die's current state
    def current_state(self):
        print(self._gamestats)
     
##############################################################################################################
# The Game class
class MonCarloGame: 

    def __init__(self, dice): 
        self.dice = dice
        
    
    # method: play
    def play(self, nrolls):
        assert isinstance(nrolls, int) 
        results_of_play = {} 

        # creates a structure like this:
#{
#  0: [results from first die],
#  1: [results from second die],
#  2: [results from third die]
#}
        
        # enumerate iterates and counts    
        for index, die in enumerate(self.dice):
            results_of_play[index] = die.roll(nrolls)
    
    # SAVES the result of the play to a private data frame
    # wide format: roll number as named index, columns for each die face (using it's list index as the column name) and the face rolled in that instance 

        
        self._rolls = pd.DataFrame(
            results_of_play
        ).rename_axis(index='roll_#')
        return self._rolls
    

    # method: SHOW results of most recent play
    # returns a COPY of the private play data frame
    # takes a parameter to return the data frame in wide (default) or narrow format 
    # Value Error if user passes an invalid option for narrow or wide
    def show_results (self, format = 'wide'):
        if format not in['wide', 'narrow']:
            raise ValueError(f"{format} is not a valid entry. Select 'narrow' or 'wide'.") 
            
        if format == 'wide':
            return self._rolls.copy()
        # narrow: MultiIndex (roll# and die#)+ single column with outcome
        # wide to narrow with stack() -- can also unstack()
        elif format == 'narrow':
#            self._rolls.reset_index().set_index(['roll_#','die_#']) # reset-set does not work here bc col of die(s) not already 'named'
            df_n = self._rolls.stack()
            df_n.index.names = ['roll_#' , 'die_#']
        return df_n
    
##############################################################################################################

    
# The Analyzer class
class MonCarloAnalyzer:

    # method: init
    # takes results of one game (game object) | ValueError
    
    def __init__(self, game):
        if not isinstance(game, MonCarloGame):
            raise ValueError("Must pass a MonCarloGame object to initiate.")
        self.game = game
        

    # method: jackpot (all faces the same)
    # computes: how many times the game resulted in a jackpot 
    # nunique(axis = 1), for row-wise
    # returns an integer: int()
    
    def jackpot(self):
        jackpot = (self.game.nunique(axis=1)==1)
        num_jackpots = sum(jackpot == True)
        return int(num_jackpots)
    

    # method: face-counts-per-roll 
    # computes how many times a particular face is rolled in each event
    # df in wide format (roll_# index)
    def facecounts_per_roll(self):
        facecounts = self.game.fillna(0)
        facecounts = self.game.count(axis='rows')
    
        # need to create a df of results... 
    
    
    # method: combo count
    # 
    
    
    
    
    
    
    # method: permutation count
    

