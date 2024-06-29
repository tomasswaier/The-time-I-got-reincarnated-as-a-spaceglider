#Dependencies:
#image village = im.Scale("village.jpg", 1280, 720)
#image summoners rift = im.Scale("summoners rift.jpeg", 1280, 720)
#define v = Character("Village")


label introduction(t):
  #todo show everyhing blacj (LAUGH ITS A TWITCH REFERENCE)
  scene bg blackzR
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

  $ guard = entity(Character("City Guard",color='#444444',image='guard'),5,1,1,1)


  "manly voice" "{b}HEY YOU STOP RIGHT THERE{/b}"


  "*you see armored man approaching you*"

  show guard walk at right


  menu :
    guard.C "State your name and you business in this village"
    
    "HAVE YOU SEEN MY KITTEN???!!!??":
      guard.C "A haven't seen anyone and you better get out you dirty rat"
      
    "*attack him*":
      "test2"

    "Hello there dear sir. Would perhaps know of ...":
      guard.C "Oh I didn't realise you we're such a distinguished gentleman."

      menu:	
        guard.C "Are you perhaps the person our chief is expecting ? Come right trough"

	"Uhhhh":
	  guard.C "Oh and I'd completely forget ... Where did i put that thing"
	"Awww I'm uhhhh well I don'...":
	  guard.C "Oh and I'd completely forget ... Where did i put that thing"
	"MNNnnmnm":
	  guard.C "Oh and I'd completely forget ... Where did i put that thing"
      "you get an item --- finish this part ---"

  "TEST 00011"
label test1:
  "IN TEST 1 )(*@#)(!*#)(*#*!)(#*@!)#*) " 
