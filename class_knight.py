from class_event import *

class Knight:
    def __init__(self,hp, level, ringsign):
        self.hp = hp
        self.level = level
        self.ringsign = ringsign
    def encounterK(self, event, index,idEvent,baseDamage = 0.0):
        event.encounter(self,index,idEvent,baseDamage)
