﻿#we create entity class that holds basic values
init python:

  class entity:

    def __init__(self,character,health=100,attack_demage=5,attack_speed=1,observation=0):
      self.C=character
      self.HP=health
      self.AD=attack_demage
      self.AS=attack_speed
      self.OBS=observation




label start:

    
    $ twitch=entity(Character("Twitch",image='twitch'),10,1,1,0)
    call reincarnation(twitch)
    #twitch gets reincarnated and after encounter with city guard he enters the town
    call introduction(twitch) #commented out lebo nefunguje hra, nevermind, fixed
    # something in town 
    # call something    

    #call test(twitch)
    return
label test(t):
    $ dummy=entity(Character("Weiss Schnee",image='dummy'),10,1,1,0)
      
    scene bg fight
    show dummy talk at left with dissolve
    show twitch talk at right with dissolve
    call fight(t,dummy)
#    if result=='loss':	
#    "you lost"
#    else:
#    "you won"
