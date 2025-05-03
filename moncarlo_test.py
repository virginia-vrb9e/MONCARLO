# a test file for the MonCarlo class (moncarlo.py)

# Note that you do not need to create an __init__() method in this class, 
# nor do you have to define any class variables.
# Instead, treat every method as a small, stand-alone program 
# in which you create a new object for your test. 
# This is not the best practice in a production environment, 
# but it works and it will enable you to get the gist of unit testing.

import numpy as np
import pandas as pd
import unittest
from moncarlo import MonCarlo

class TestMonCarloDevice(unittest.TestCase):
    
    def test_1_instantiate_device(self):
        arr_test = (['a', 'b', 'c'])
        self.die_test = MonCarloDevice(arr_test)
        self.assertIn(1.0, self.weights), "The face weights are not 1.0." 
        return self.die_test
        
    def test_2_change_facewt(self):
        facewt_test = die_test.change_facewt('a', 5.0)
        self.assertIsNotNone(die_test), "facewt cannot be None."
        
    def test_3_roll(self):
        test_roll = die_test.roll(10)
        assertIn(ntimes, type(int)), "the value ntimes must be an integer."
        
    def test_4_current_state(self):
        self.assertIsNotNone(die_test._gamestats),"There is a problem with the internal recording of this class."

class TestMonCarloGame(unittest.TestCase):
    
    def test_5_initiategame(self):
        self.test_dice = [self.die_test, self.die_test]
        self.assertIsInstance(self.die_test, TestMonCarloDevice), "The object being passed is not a device from MonCarloDevice."
        self.test_game = MonCarloGame(self.test_dice)
        return self.test_game
    
    def test_6_play(self):
        self.test_dice.play(2)
        self.assertIsNotNone(self.test_dice._rolls), "There is an issue with the game results."
    
    def test_76show_results(self):
        self.assertNotIn(self.test_dice._rolls, self.test_dice), "Error: there are no results from the play." 
    

class TestMonCarloAnalyzer(unittest.TestCase, self.test_game):
    
    def test_8_instantiate_analyzer(self):
        self.test_analyzer = MonCarloAnalyzer(self.test_game)
        self.assertIsNotNone(self.test_game), "You must pass something to the initializer for MonCarloAnalyzer."
    
    def test_9_jackpot(self):
        self.assertIsNotNone(self.test_analyzer.jackpot), "Error: the system did not complete the check for jackpots."
    
    def test_10_facecounts_per_roll(self):
        self.AssertIsNotNone(self.test_analyzer.facecounts_per_roll), "Error: the system did not complete the check for facecounts."
    
    def test_11_combos(self):
        self.AssertIsNotNone(self.test_analyzer.combos), "Error: the system did not complete the check for combos."
    
    def test_12_permutations(self):
        self.AssertIsNotNone(self.test_analyzer.permutations), "Error: the system did not complete the check for permutations." 

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
        