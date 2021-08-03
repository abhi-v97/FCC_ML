

# Initial instinct was to counter each player individually, but the course is called machine learning, so should try to look for patterns instead.
play_order = {}


def player(prev_play, opponent_history=[]):
  global play_order
  # n is the number of past plays it looks at
  #3 seems to give the best result. Going over 10 seems to cause a meltdonwn. 
  # Maybe 1000 games sample is too small, so smaller n works best
  
  n = 3
  
  guess = "S" #First guess seems to matter a lot more than I thought it would. Could be improved upon.

  if prev_play != "":
    opponent_history.append(prev_play)
  else:
    play_order = {} 
    opponent_history = [] # Flush opponent history, otherwise the program will think its playing 4000 games against the same person, instead of 4 different players.
  
  if len(opponent_history)>n:
    pattern = "".join(opponent_history[-n:])


    if "".join(opponent_history[-(n+1):]) in play_order.keys():
      play_order["".join(opponent_history[-(n+1):])]+=1
      
    else:
      play_order["".join(opponent_history[-(n+1):])]=1
      

    possible =[pattern+"R", pattern+"P", pattern+"S"]
    

    for i in possible:
      if not i in play_order.keys():
        play_order[i] = 0

    predict = max(possible, key=lambda key: play_order[key])
    

    if predict[-1] == "P":
      guess = "S"
    if predict[-1] == "R":
      guess = "P"
    if predict[-1] == "S":
      guess = "R"

  return guess