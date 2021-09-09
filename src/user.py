"""Class file for the User

    Created on: 7-21-2021
    Version: Python 3.8.5
    Created by: Bayley King (https://github.com/king2b3)
"""

class User:
    def __init__(self, data:dict, week:int) -> None:
        #saves the needed data AND removes them from the dict
        self.name = data.pop("Discord Tag? **case sensitive**")
        self.tier = data.pop("Which tier do you play in? ")
        self.team = data.pop("What Tranquility team(s) are you part of?")
        #remove the timestamp
        #print(data)
        #data.pop("Timestamp")
        data.pop("\ufeffTimestep")
        self.week = week
        #converts the reminaing dict into list of picks
        self.picks = list(data.values())
        self.score = 0
        self.check_vals()
                
    def check_vals(self) -> None:
        """If anything isn't filled out, make into a 0"""
        for i in range(len(self.picks)):
            if self.picks[i] == "":
                self.picks[i] = "0"
    
    def write(self) -> None:
        import csv
        #searches if the user already exists
        not_exist = True
        with open("output.csv", "r") as csv_output:
            reader = csv.reader(csv_output)
            for user in list(reader):
                if user[0] == self.name:
                    print(f"\tUSER FOUND")
                    temp_list = user
                    not_exist = False
                    break

        #re-write to new file because I didn't use Pandas (you should)
        with open("new_output.csv", "a") as csv_output:
            output = csv.writer(csv_output)
            if not_exist:
                temp_list = [self.name, self.team, self.tier,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0]
                temp_list[self.week+2] = self.score

            else:
                temp_list[self.week + 2] = self.score
            
            output.writerow(temp_list)
                
    def __eq__(self, u2) -> None:
        """u2 is considered the master user
        set the score of master vs self for the number of correct picks
        """
        for i in range(0,len(self.picks),2):
            self.score += self.match(self.picks[i],self.picks[i+1],
                    u2.picks[i],u2.picks[i+1])
    
    @staticmethod
    def match(team1_user, team2_user, team1_master, team2_master) -> int:
        """Returns the score from the match pick"""
        #don't need to typecast to int because Python is best
        #check if exactly predicted
        if ((team1_user == team1_master) and (team2_user == team2_master)):
            return 3
        
        #did the home team win?
        if team1_master > team2_master:
            master_win = True
        else:
            master_win = False

        #did the user predict the home team to win?
        if team1_user > team2_user:
            user_win = True
        else:
            user_win = False

        #did the user predict correctly?
        if master_win == user_win:
            return 1
        else:
             return 0