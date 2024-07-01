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

  show twitch walk at left
  
  t.C "I have to find her"

  #-------------VILLAGE-----------------

  "*you see outlines of a village*"

  #image of a village in background

  $ guard = entity(Character("City Guard",color='#444444',image='guard'),5,1,1,1)


  "manly voice" "{b}HEY YOU STOP RIGHT THERE{/b}"


  "*you see armored man approaching you*"

  show guard walk at right


  menu:
    guard.C "State your name and your business in this village"
    
    "HAVE YOU SEEN MY KITTEN???!!!??":
        guard.C "A haven't seen anyone and you better get out you dirty rat"
        twitch.C "You will pay for this"
        call fight(twitch,guard)
        "As you look trough his posessions you find flashy boots and a healing potion"
        "you heal your self and your HP is back to full"
        "As you are looking at those shoes you can't but thing you've seeen them before..."
        "YOU HAVE. Those are Berserkes Greaves . As you put them on you can feel your Attack Speed rising"
        $ twitch.AS+=1
        $ twitch.HP=10
    "*attack him*":
        call fight(twitch,guard) 
        "As you look trough his posessions you find flashy boots and a healing potion"
        "you heal your self and your HP is back to full"
        "As you are looking at those shoes you can't but thing you've seeen them before..."
        "YOU HAVE. Those are Berserkes Greaves . As you put them on you can feel your Attack Speed rising"
        $ twitch.AS+=1
        $ twitch.HP=10
    "Hello there dear sir. Would perhaps know of ...":
        guard.C "Oh I didn't realise you were such a distinguished gentleman."

        menu:    
            guard.C "Are you perhaps the person our chief is expecting? Come right through"

            "Uhhhh":
                guard.C "Oh and I'd completely forget ... Where did I put that thing"
            "Awww I'm uhhhh well I don'...":
                guard.C "Oh and I'd completely forget ... Where did I put that thing"
            "MNNnnmnm":
                guard.C "Oh and I'd completely forget ... Where did I put that thing"
        
        "The guard hands you boots"
        guard.C "Chief said you'll want them"
        "As you inspect the item you start recognizing it ..."
        "It's Berserker's Greaves"
        "As you put them on you can feel you'r attack speed increasing"
        $ twitch.AS+=1
  menu:
      "Choose your path"

      "go to city":
        "you are walking to the city's main gate"
      "go the completely oposite way":
        "as you walk to the city you realise that ... what ? you are in the city... how peculiar"

