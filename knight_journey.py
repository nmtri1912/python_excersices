from class_knight import *
from class_event import *
from executed import *

def knight_journey(fileName):
    with open(fileName, 'r') as f:
        lines = f.read().split('\n')

    try:
        info = lines[0].split(' ')
        eventStr = lines[1].split(' ')

        knight = Knight(int(info[0]),int(info[1]),info[2])
        events = []

        for event in eventStr:
            try:
                event = int(event)
                if event == 0 or event == 8:
                    events.append(event)
                elif event//10 > 0 and event//10 < 8 or event//10 == 9:
                    events.append(event)
            except:
                pass
        #executed
        return execute(knight,events)
    except:
        return ''