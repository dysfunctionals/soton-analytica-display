import requests
import random
from display.constants import move_speed

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
            move[player] = dict()
            maxCommand = None
            maxAmount = -1
            for command, amount in commands.items():
                if amount > maxAmount:
                    maxCommand = command
                    maxAmount = amount

            if maxAmount == 0:
                move[player] = 0
            elif maxCommand == 'up':
                move[player] = -3
            elif maxCommand == 'down':
                move[player] = 3

        return move

    def democracy(self, seconds):
        data = self.__getData__(seconds)
        move = dict()
        for player, commands in data.items():
            total = 0
            commandSum = 0
            for command, amount in commands.items():
                if command == 'up':
                    commandSum -= amount
                elif command == 'down':
                    commandSum += amount
                total += amount
                
            if total == 0:
                move[player] = 0
            else:
                move[player] = commandSum / total * move_speed
        print(move)
        return move