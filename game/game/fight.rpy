label fight(t, enemy):
    enemy.C talk 'lets fight'

    while t.HP > 0 and enemy.HP > 0:
        $ i = 0
        while i < t.AS:
            $ pressed = False

            # Show the shieldButton screen without blocking the rest of the script
            show screen shieldButton

            # This loop waits for the shield button to be pressed
            while not pressed:
                $ renpy.pause(0.1)  # Short pause to avoid freezing the game while waiting for input

            # Player hits the object behind the shield and decreases enemy HP
            "Enemy hp just dropped to [enemy.HP - t.AD]"
            $ enemy.HP = enemy.HP - t.AD
            $ i += 1

        # Enemy attacks after the player's turn
        enemy.C fighting "as the enemy attacks you and now you have [t.HP - enemy.AD] HP"
        $ t.HP = t.HP - enemy.AD
        if t.HP < 1:
            "lost"  # TODO - add something after loss
    
    return 'won'

# This screen handles the shield flashing and the object interaction
screen shieldButton():
    # We use a timer to toggle the shield's visibility every 0.5 seconds
    $ shield_visible = renpy.random.randint(0, 1)  # Randomly toggle shield visibility

    # The shield button (flashes on and off)
    if shield_visible:
        imagebutton:
            idle "shield.jpg" at right
            hover "shield.jpg"
            action SetVariable("pressed", True)  # If the shield is pressed, it sets 'pressed' to True
            focus_mask True  # Makes only the shield clickable

    # The object behind the shield (this is clickable when the shield is not visible)
    else:
        imagebutton:
            idle "object_behind_shield.jpg" at right
            hover "object_behind_shield.jpg"
            action [SetVariable("pressed", True), Function(decrease_enemy_hp)]  # If the object is pressed, it decreases the enemy HP
            focus_mask True  # Makes only the object clickable

# This function decreases the enemy's HP
init python:
    def decrease_enemy_hp():
        store.enemy.HP -= store.t.AD

