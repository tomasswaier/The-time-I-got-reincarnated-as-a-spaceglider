
label reincarnation(twitch):
  $ d = entity(Character('Draven',color='#b35555'),1,1,1,1)

  $ t = entity(Character('Thresh',color='#888888'),1,1,1,1)
  $ l = entity(Character('Lulu',color= '#d130b2'),1,1,1,1)
  scene bg rift
  show lulu talk at right 
  l.C 'How are we going to beat them SENPAI ?'
  show twitch talk at left 
  twitch.C "Don't worry kitten. Just don't get hooked and we-"
  scene bg rift
  show lulu walk at left
  show thresh attack at right
  l.C '{b}OH NOOOOOOOOO I GOT HOOOKED{/b}'


  #show lulu death announcer 
  #death announcer sound add

  scene bg rift
  show twitch talk
  twitch.C "HOW DARE YOU HURT MY KITTEN"
  scene bg rift
  show draven base at left
  d.C 'digusting spaceglider L9 wannabe. I will make sure you never glide again'
  show thresh base at right 
  t.C 'where is he?'
  #todo change up the scene bg 
  scene bg rift
  show thresh attack at right 
  t.C 'I think I see him'
  #todo : add appearing animation
  show twitch walk at left
  twitch.C "I was hiding! Hehehahaa, grr!" 
  t.C "COME HERE {b}RAT BOY{/b}"
  #add death announcer mby ?
  twitch.C ""
  return 





