#Dependencies:
#image village = im.Scale("village.jpg", 1280, 720)
#image summoners rift = im.Scale("summoners rift.jpeg", 1280, 720)
#define v = Character("Village")


label introduction:
  scene village 
  with dissolve

  show twitch at left with dissolve

  t "Where am I?" #im not a literature major
  
  show villager at right

  v "How do you not know where you are?"
  v "You must know how you got here, no?"

  t "I kind of just {i}appeared{/i}?"

  v "Huh?"

  return
