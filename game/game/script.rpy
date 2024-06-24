


#we create entity class that holds basic values
init python:

  class entity:

    def __init__(self,character,health=100,attack_demage=5,attack_speed=1,observation=0):
      self.C=character
      self.HP=health
      self.AD=attack_demage
      self.AS=attack_speed
      self.OBS=observation




label start:
    scene bg room

    $ twitch =entity(Character("Twitch",image='twitch'),10,1,1,0)
    
    $ examplePerson=entity(Character("Veronika"),10,1,1,0)
    show twitch walk
    twitch.C "my Name is twitch"
    
    twitch.C talk"I am talking"
    

    twitch.C "i was hiding"
    
    scene owo
    examplePerson.C "im also here"


    return
