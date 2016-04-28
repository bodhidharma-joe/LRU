# -*- coding: utf-8 -*-
"""
This class defines a LRU data structure with a maximal size using a list to 
store the keys and a dictionary to store the values. The getValueByKey method 
prints the corresponding value for an existing key or NOTFOUND for a 
nonexisting key. The setKeyAndValue method insert a new key and its value to 
LRU, and maintain the LRU size.

Created on Tue Apr 26 08:00:02 2016
@author: Congzhou Wang
"""

class LRU:
    """
    LRU class
    """
    MAXSIZE = 0
    # The last element in keys is the most recently called key,
    # while the first element in keys is the least recently called
    keys = []
    keyToValue = {}
    curSize = len(keys)
    def __init__(self, maxSize): # Initialize a LRU object
        self.MAXSIZE = maxSize
        print "SIZE OK"
        
    def getValueByKey(self, key):
        """
        Return the corresponding value for a given key string
        If the key does not exist, print ERROR
        """
        if key in self.keys:
            print "GOT " + str(self.keyToValue[key])
            # Put the key to the end of the list since it is just called
            self.keys.remove(key) 
            self.keys.append(key)
        else:
            print "NOTFOUND"
    
    def setKeyAndValue(self, key, value):
        """
        Update the key list and the dictionary using a given key/value pair
        """
        if key in self.keys:
            self.keyToValue[key] = value
            print "SET OK"
        elif self.curSize < self.MAXSIZE:
            # Always append the new key to the end of the list
            self.keys.append(key)
            self.keyToValue[key] = value
            self.curSize = len(self.keys)
            print "SET OK"
        elif self.curSize == self.MAXSIZE:
            # If maximal size reached, remove the first key in the list
            # since it is the least recently called.
            # Always append the new key to the end of the list
            keyToRemoved = self.keys.pop(0)
            del self.keyToValue[keyToRemoved]
            self.keys.append(key)
            self.keyToValue[key] = value
            self.curSize = len(self.keys)
            print "SET OK"
        else:
            print "ERROR"

def lruOperation():
    started = False
    exitReceived = False
    while not exitReceived: # Keep running until receiving "exit"
        line = str(raw_input()) # Get input
        if not started: # If LRU object is not initialized yet
            commands = line.split(" ")
            if len(commands) != 2: # Will only accept size+int format
                print "ERROR"
                continue
            elif commands[0].upper() != "SIZE": # Check if command is "size"
                print "ERROR"
                continue
            else:
                try:
                    size = int(commands[1])
                    lru = LRU(size)
                    started = True
                except: # if the second part is not an int
                    print "ERROR"
                    continue
        else: # If LRU object has been there already
            commands = line.split(" ")
            # Will only accept three command formats
            if len(commands) < 1 or len(commands) > 3: # If too long or too short
                print "ERROR"
                continue
            elif commands[0].upper() == "GET" and len(commands) == 2:
                lru.getValueByKey(commands[1]) # If command is in get+key
            elif commands[0].upper() == "SET" and len(commands) == 3:
                lru.setKeyAndValue(commands[1], commands[2]) # If command is in set+key+value
            elif commands[0].upper() == "EXIT" and len(commands) == 1:
                exitReceived = True # If command is exit, break the while loop
                break
            else:
                print "ERROR"
                continue

lruOperation()
            
##Sample inputs and outputs:
#size 3
#SIZE OK
#
#get foo
#NOTFOUND
#
#set foo 1
#SET OK
#
#get foo
#GOT 1
#
#set foo 1.1
#SET OK
#
#get foo
#GOT 1.1
#
#set spam 2
#SET OK
#
#get spam
#GOT 2
#
#set ham third
#SET OK
#
#set parrot four
#SET OK
#
#get foo
#NOTFOUND
#
#get spam
#GOT 2
#
#get ham
#GOT third
#
#get ham parrot
#ERROR
#
#get parrot
#GOT four
#
#exit



