import requests
import random


def standardAddress():
    return "http://10.9.174.43/data"

class CrowdInput:    
    def __init__(self, address):
        self.address = address

    def __getData__(self, seconds):
        r = requests.get(self.address + "?seconds=" + str(seconds))
        return r.json()

    def popular(self, seconds):
        data = self.__getData__(seconds)
        move = dict()
        for player, commands in data.items():
            maxCommand = None
            maxAmount = -1
            for command, amount in commands.items():
                if amount > maxAmount:
                    maxCommand = command
                    maxAmount = amount

            if maxAmount == 0:
                move[player] = "none"
            else:
                move[player] = maxCommand
        return move

    def democracy(self, seconds):
        data = self.__getData__(seconds)
        move = dict()
        for player, commands in data.items():
            commandSum = 0
            for command, amount in commands.items():
                commandSum += amount
            if commandSum == 0:
                move[player] = "none"
            else:
                rand = random.randint(0, commandSum - 1)
                for command, amount in commands.items():
                    if rand > amount:
                        rand -= amount
                    else:
                        move[player] = command
                        break
        return move

                

print(CrowdInput(standardAddress()).popular(0))