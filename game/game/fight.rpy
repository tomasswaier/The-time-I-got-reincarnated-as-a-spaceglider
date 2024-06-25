


label fight(t,enemy):
  
  enemy.C talk'lets fight'
   
  while t.HP >0 and enemy.HP >0:
    $ i =0 
    while i<t.AS:
      t.C walk "I attack and your HP is now [enemy.HP - t.AD]"
      $ enemy.HP = enemy.HP- t.AD
      $ i+=1
    enemy.C fighting"I attack and your HP is now [t.HP - enemy.AD]"
    $ t.HP = t.HP- enemy.AD
    
  return 'won'
