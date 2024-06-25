#Dependencies:
#image village = im.Scale("village.jpg", 1280, 720)
#image summoners rift = im.Scale("summoners rift.jpeg", 1280, 720)
#define v = Character("Village")


label introduction(t):
  #todo show everyhing blacj (LAUGH ITS A TWITCH REFERENCE)
  scene bg black
  t.C "wait... what's happening? Why is everything black ?"

  
  #make waking up animation or some kinda of trainsition
  scene village with dissolve

  $ v =entity(Character("villager",color="#aa8833"),10,1,1,0)

  show twitch talk at left with dissolve

  t.C "Who's following me?" #im not a literature major
  
  show villager standing at right

  v.C "What? Oh no are you also retarded like the girl that just passed by ?"


  t.C "Are you talking about my kitten? Where is she? Tell me or I WILL SPACEGLIDE"

  v.C "Huh?"

  v.C "That little monster was screaming and running that way"

  hide twitch talk

  v.C "what the "

  scene bg filler1

  show twitch walk
  
  t.C "I have to find her"

  #-------------VILLAGE-----------------

  "*you see outlines of a village*"

  #image of a village in background


  "manly voice" "{b}HEY YOU STOP RIGHT THERE{/b}"


  "*you see a man approaching you*"

