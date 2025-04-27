import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# The Die class
class MonCarloDevice():
    
#    img = mpimg.imread('d20_met_nyc.jpg')
#    plt.imshow(img)
#    print("THE MET Museum: \nicosahedron with faces inscribed with Greek letters \nPtolemaic Period–Roman Period\n(2nd century B.C.– 4th century A.D.)")
#    print("Read about this ancient Monte Carlo device: https://www.metmuseum.org/art/collection/search/551072")
    
    # method: the initializer
    
    def __init__(self, faces):
        self.faces = faces
        print(type(faces))
            
            
        # check that faces is np.array
        if not isinstance(faces, np.ndarray):  
            raise TypeError("Input of faces must be an NumPy array.") 
        else:
            print("yes, this is an np.ndarray!")
            
            
        # check that faces are strings or numbers
                # https://github.com/numpy/numpy/issues/17325
                # https://stackoverflow.com/questions/30086936/what-is-the-difference-between-the-types-type-numpy-string-and-type-str
        x = len(self.faces)
        for i in range(x):
            if not isinstance(self.faces[i], (str)):
                float(i)
                print("switched to float")
            else:
                print("check ok: this face is either a string or number.") 
    
    
        # check that faces are unique values 
        uniq = np.unique(faces)  # np.unique returns array of unique values
        if len(uniq) != len(faces):
            raise ValueError("The NumPy array of faces for your device must be of unique values.")


        # initiate the weights as 1.0   
        self.weights = []
        self.num_faces = len(faces)
        x = len(self.faces)
        for i in range(x):
            self.weights.append(1.0)
#        self.weights.extend(1.0 * x) for... # replacing for loop with comprehension
    
        # return faces and weights in a private df w/ faces as index
        col_names = ['weight']
        self._gamestats = pd.DataFrame(
            self.weights,
            index = self.faces, columns = col_names).rename_axis(index='faces')
            
            
    # method: change the weight of a single side
    def change_facewt(self, face, nwt):
        self.nwt = float(nwt)
        self.face = face
        x = len(self.faces)
            # checks to see if face passed is valid - if it's in the die array | IndexError
        is_in = np.isin(self.faces, self.face)
        for _ in is_in:
            if self.face not in self.faces: 
                raise IndexError(f"{face} is not a face on this device.")
            else:
                print("check okay: that face exists.")   
            # check if nwt is int or float - OR castable | TypeError
        if not isinstance(nwt, (int, float)):
            try:
                nwt = float(nwt)  
            except:
                raise TypeError("New weight must be numeric.")
        

    # method: roll the die one or more times
    def roll_ntimes(self, ntimes = 1):
        rolls = []
        for index in self._gamestats.iterrows():
#            rolls.append(self.faces.sample(replace = True))  
            rolls.append(index[0])
        return rolls
    
    # method: show die's current state
    def check(self):                      # !!!!
        return self._gamestats()