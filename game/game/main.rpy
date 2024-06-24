#Dependencies:
#image village = im.Scale("village.jpg", 1280, 720)
#image summoners rift = im.Scale("summoners rift.jpeg", 1280, 720)
#define v = Character("Village")


label introduction(t):
  scene village 
  with dissolve
  $ v =entity(Character("villager"),10,1,1,0)

  show twitch talk at left with dissolve

  t.C "Where am I?" #im not a literature major
  
  show villager at right

  v.C "How do you not know where you are?"
  v.C "You must know how you got here, no?"

  t.C "I kind of just {i}appeared{/i}?"

  v.C "Huh?"

  return
