from display.constants import dataTypes
import random

class DataManager:
    def __init__(self):
        self.dataSafe = list(dataTypes)
        self.dataRemaining = list(dataTypes)

    def drop(self):
        if len(self.dataRemaining) == 0:
            return None
        lost = self.dataRemaining[random.randint(0, len(self.dataRemaining) - 1)]
        print(lost)
        return lost

    def pickup(self, data):
        try:
            self.dataRemaining.remove(data)
        except ValueError:
            pass

    def getRemaining(self):
        state = dict()
        for dataType in dataTypes:
            state[dataType] = False
        for dataType in self.dataRemaining:
            state[dataType] = True

        return state
        
    