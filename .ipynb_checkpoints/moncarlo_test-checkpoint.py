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
from moncarlo import MonCarloDevice, MonCarloGame, MonCarloAnalyzer


class TestMonCarloDevice(unittest.TestCase):
    
    def setUp(self):
        arr_test = np.array(['a', 'b', 'c'])
        self.die_test = MonCarloDevice(arr_test)
        self.test_roll = self.die_test.roll(10)
    
    def test_1_instantiate_device(self):
        self.assertIn(1.0, self.die_test.weights), "The face weights are not 1.0." 
        return self.die_test
        
    def test_2_change_facewt(self):
        facewt_test = self.die_test.change_facewt('a', 5.0)
        self.assertIsNotNone(self.die_test), "facewt cannot be None."
        
    def test_3_roll(self):
        self.test_roll = self.die_test.roll(10)
        pass
        
    def test_4_current_state(self):
        self.assertIsNotNone(self.die_test._gamestats),"There is a problem with the internal recording of this class."

class TestMonCarloGame(unittest.TestCase):
    
    def setUp(self):
        arr_test = np.array(['a', 'b', 'c'])
        self.die_test = MonCarloDevice(arr_test)
        self.test_dice = [self.die_test, self.die_test]
        self.test_game = MonCarloGame(self.test_dice)
        self.test_roll = self.die_test.roll(10)
    
    def test_5_initiategame(self):
        self.assertIsInstance(self.die_test, MonCarloDevice), "The object being passed is not a device from MonCarloDevice."
    
    def test_6_play(self):
        self.test_game.play(2)
        self.assertIsNotNone(self.test_game), "There is an issue with the game results."
    
    def test_7_show_results(self):
        results = self.test_game.show_results
        self.assertNotIn(results, self.test_dice), "Error: there are no results from the play." 
    

class TestMonCarloAnalyzer(unittest.TestCase):
    
    def setUp(self):
        arr_test = np.array(['a', 'b', 'c'])
        self.die_test = MonCarloDevice(arr_test)
        self.test_roll = self.die_test.roll(10)
        self.test_dice = [self.die_test, self.die_test]
        self.test_game = MonCarloGame(self.test_dice) # analyzer analyzes THIS after the game is played and results are stored in self
        self.test_playedgame = self.test_game.play(1000) 
        self.test_analyzer = MonCarloAnalyzer(self.test_game)

    def test_8_instantiate_analyzer(self):
         self.assertIn(self.die_test, self.test_dice), "You are not passing the correct parameter."
    
    def test_9_jackpot(self):
        self.assertIsNotNone(self.test_analyzer.jackpot), "Error: the system did not complete the check for jackpots."
    
    def test_10_facecounts_per_roll(self):
        self.assertIsNotNone(self.test_analyzer.facecounts_per_roll), "Error: the system did not complete the check for facecounts."
    
    def test_11_combos(self):
        self.assertIsNotNone(self.test_analyzer.combos), "Error: the system did not complete the check for combos."
    
    def test_12_permutations(self):
         self.assertIsNotNone(self.test_analyzer.permutations), "Error: the system did not complete the check for permutations."

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
        