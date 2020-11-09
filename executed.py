from class_knight import *
from class_event import *

dictCharacter = (0.0,0.8,1.2,4.1,7.9,6.5,8.7,0.0,0.0,0.1)
dictEvent = (EventInterface(),EventInterface(),EventInterface(),EventInterface(),Event4X(),Event5X(),EventInterface(),Event7X(),Event8X(),Event9X())

def execute(knight,events):
    index = 1
    print(events)
    for event in events:
        if event == 8:
            eventIn = Event8X()
            knight.encounterK(eventIn,index,event)
            index+=1
        elif event == 0:
            break
        else:
            knight.encounterK(dictEvent[event//10], index, event, dictCharacter[event//10])
            index+=1
            
        if knight.hp < 0:
            knight.ringsign = ''
            break
        
        if knight.ringsign == '':
            break

    return knight.ringsign