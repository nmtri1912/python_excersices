from class_knight import *

def getLevelO(indexEvent):
    b = indexEvent % 10
    if indexEvent > 6:
        if b > 5:
            levelO = b
        else:
            levelO = 5
    else:
        levelO = b
    
    return levelO

def removeTheSame(listT, number):
    numberStr = str(number)
    return listT.replace(numberStr,'')

class EventInterface:
    def __init__(self):
        pass
    def encounter(self, knight, index, idEvent, baseDamage):
        levelO = 0
        levelO = getLevelO(index)

        if knight.level > levelO: #win
            knight.ringsign = knight.ringsign + str(idEvent%10)
        if knight.level < levelO: #lose
            damage = baseDamage * levelO * 10
            knight.hp -= int(damage)

        knight.ringsign
            
            
class Event4X(EventInterface):
    def encounter(self, knight, index, idEvent, baseDamage):
        levelO = 0
        levelO = getLevelO(index)
        
        if knight.level > levelO: #win
            knight.ringsign = knight.ringsign + str(idEvent%10)
        if knight.level < levelO: #lose
            damage = baseDamage * levelO * 10
            knight.hp -= int(damage)
            knight.ringsign = removeTheSame(knight.ringsign,idEvent%10)
            
class Event5X(EventInterface):
   def encounter(self, knight, index, idEvent, baseDamage):
        levelO = 0
        levelO = getLevelO(index)
        
        if knight.level > levelO: #win
            knight.ringsign = knight.ringsign + str(idEvent%10)
        if knight.level < levelO: #lose
            damage = baseDamage * levelO * 10
            knight.hp -= int(damage)
            if len(knight.ringsign) > 3:
                knight.ringsign = knight.ringsign[3:]
            else:
                knight.ringsign = ''

class Event7X(EventInterface):
    def encounter(self, knight, index, idEvent, baseDamage):
        knight.ringsign = '0123456791'

class Event8X(EventInterface):
    def encounter(self, knight, index, idEvent,baseDamage):
        knight.hp = 999
        knight.ringsign = knight.ringsign[:-1]
        
class Event9X(EventInterface):
    def encounter(self, knight, index, idEvent, baseDamage):
        levelO = 0
        levelO = getLevelO(index)
        
        if knight.level > levelO: #win
            knight.ringsign = knight.ringsign + str(idEvent%10)
            knight.ringsign = knight.ringsign[::-1]
        if knight.level < levelO: #lose
            damage = baseDamage * levelO * 10
            knight.hp -= int(damage)

'''
class Event11X(EventInterface):
    def encounter(self, knight, index, idEvent,baseDamage):
        knight.ringsign = knight.ringsign + str(idEvent%10)
'''