


label fight(t,enemy):
  
  enemy.C talk'lets fight'
   
  while t.HP >0 and enemy.HP >0:
    $ i =0 
    while i<t.AS:
      "Enemy hp just dropped to [enemy.HP - t.AD]"
      $ enemy.HP = enemy.HP- t.AD
      $ i+=1
    enemy.C fighting"as the enemy attacks you and now you have  [t.HP - enemy.AD] HP"
    $ t.HP = t.HP- enemy.AD
    
  return 'won'
