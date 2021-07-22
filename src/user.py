"""Class file for the User

    Created on: 7-21-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
"""

class User:
    def __init__(self, week) -> None:
        self.name = None
        self.tier = None
        self.team = None
        self.week = week
        # set name lowercase
        self.picks = {
            'hm1' : [0,0],
            'hm2' : [0,0],
            'hm3' : [0,0],
            'hm4' : [0,0],
            'hm5' : [0,0],
            'hm6' : [0,0],
            'hm7' : [0,0],
            'hm8' : [0,0],
            'hm9' : [0,0],
            'hm10' : [0,0],
            'hm11' : [0,0],
            'hm12' : [0,0],
            # Discord Tier Matches
            'dm1' : [0,0],
            'dm2' : [0,0],
            'dm3' : [0,0],
            'dm4' : [0,0],
            'dm5' : [0,0],
            'dm6' : [0,0],
            'dm7' : [0,0],
            'dm8' : [0,0],
            'dm9' : [0,0],
            'dm10' : [0,0],
            'dm11' : [0,0],
            'dm12' : [0,0],
            # Trance Tier Matches
            'tm1' : [0,0],
            'tm2' : [0,0],
            'tm3' : [0,0],
            'tm4' : [0,0],
            'tm5' : [0,0],
            'tm6' : [0,0],
            'tm7' : [0,0],
            'tm8' : [0,0],
            'tm9' : [0,0],
            'tm10' : [0,0],
            'tm11' : [0,0],
            'tm12' : [0,0]
        }
    
    def check_vals(self) -> None:

        ...
    
    def write(self) -> None:
        #appends csv results to the output sheet
        #use self.week to write to proper col, self.name for row
        ...