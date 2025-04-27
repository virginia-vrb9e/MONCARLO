import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# The Die class
class MonCarloDevice():
    img = mpimg.imread('d20_met_nyc.jpg')
    plt.imshow(img)
    print("THE MET Museum: \nicosahedron with faces inscribed \
    with Greek letters \nPtolemaic Period–Roman Period\n(2nd century \
    B.C.– 4th century A.D.)")
    print("Read about this ancient Monte Carlo device:\
    https://www.metmuseum.org/art/collection/search/551072")
    
    # method: the initializer
    def __init__(self, faces):
        self.faces = faces
        print(type(faces))
            
        # check that faces is np.array
        if not isinstance(faces, np.ndarray):  
            raise TypeError("Input of faces must be an NumPy array.") 
        else:
            print("yes, this is an np.ndarray!")  # production only; take out at the end
            
        # check that faces are strings or numbers
        x = len(self.faces)
        for i in range(x):
            if not isinstance(self.faces[i], (str)):
                float(i)
                print("switched to float")  # production only; take out at the end 
            else:
                print("check ok.") # production only; take out at the end   
                
        # check that faces are unique values 
        uniq = np.unique(faces)  # np.unique returns array of unique values
        if len(uniq) != len(faces):
            raise ValueError("The array of faces must be of unique values.")

        # initiate the weights as 1.0   
        self.weights = []
        self.num_faces = len(faces)
        x = len(self.faces)
        
        for i in range(x):
            self.weights.append(1.0)
#        self.weights.extend(1.0 * x)...  # maybe replace loop with comprehension or other... 
    
        # return faces and weights in a private df w/ faces as index
        col_names = ['weight']
        self._gamestats = pd.DataFrame(
            self.weights,
            index = self.faces, 
            columns = col_names
        ).rename_axis(index ='faces')
        
    # method: change the weight of a single side
    def change_facewt(self, face, nwt):
        self.nwt = float(nwt)
        self.face = face
        x = len(self.faces)

        # checks to see if face passed is in the die array | IndexError
        is_in = np.isin(self.faces, self.face)
        for _ in is_in:
            if self.face not in self.faces: 
                raise IndexError(f"{face} is not a face on this device.")
            else:
                print("check okay: that face exists.") # production only; take out later
                
        # check if nwt is int or float or castable | TypeError
        if not isinstance(nwt, (int, float)):
            try:
                nwt = float(nwt)  
            except:
                raise TypeError("New weight must be numeric.")
            
        # change the self.face weight with self.nwt
        # still working on this part...
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
        stat_dict = self._gamestats.to_dict('index')
        stat_dict['self.face'] = self.nwt
        self._gamestats = pd.DataFrame.from_dict(stat_dict, orient = 'index')
        print(self._gamestats()) # production only; take out at the end


    # method_2: roll the device one or more times
    def roll_ntimes2(self, ntimes = 1):
        rolls = []
        for i in range(ntimes):
            rolls.append(self._gamestats.sample(replace = True))  
        return rolls
    
    # method: show die's current state
    def current_state(self):
        print(self._gamestats())
        
# The Game class
class Game(MonCarloDevice):
    # method: initializer/constructor
    def __init__(self, *dice): 
        self.dice = dice
        assert isinstance(nroll, int)
        throws = []
        
        # enumerate iterates and counts 
        for index, die in enumerate(self.dice):
            throws.append(die)
        throws_dict = ((i,j) for i,j in throws)
        return throws, throws_dict 
        
    # method: play
    def play(self, n_rolls):
        self.n_rolls = n_rolls
        
        
    
    # SAVES the result of the play to a private data frame
    # wide format: roll number as named index, columns for each die face (using it's list index as the column name) and the face rolled in that instance 
    def save_results(self):
    
    
    
    # method: SHOW results of most recent play
    # returns a COPY of the private play data frame
    # takes a parameter to return the data frame in wide (default) or narrow format 
    # Value Error if user passes an invalid option for narrow or wide
    def show_results (self, format = 'wide'):
    
    
    
    
    
    
# The Analyzer class
class Analyzer():
    
    # method: init
    # takes results of one game (game object) | ValueError
    
    
    
    
    
    
    # method: jackpot (all faces the same)
    # computes: how many times the game resultsed in a jackpot
    # returns an integer
    
    
    
    
    
    # method: face-counts-per-roll 
    # computes how many times a particular face is rolled in each event
    # df in wide format (roll_# index)
    
    
    
    
    # method: combo count
    # 
    
    
    
    
    
    
    # method: permutation count
