def verify(entry, alphabet, initialState, actualState, finalState, states, transitions):
  nextState = actualState[0] + str(int(actualState[1]) + 1)
  previousState = actualState
  
  for index, _char in enumerate(entry):
    highIndex = index
    
  for index, char in enumerate(entry):
    if char in alphabet and actualState in states:
      #FIXME: corrigir lógica
      if actualState in finalState and index == highIndex:
        return True
      elif (actualState, actualState) in transitions and char == transitions[actualState, actualState][2]:
          print(f"{actualState} -> {actualState}, {char}")
          continue
      elif (actualState, previousState) in transitions:
        if actualState in transitions[actualState, previousState] and char == transitions[actualState, previousState][2]:
          tempPrevious = previousState
          previousState = actualState
          actualState = tempPrevious
          nextState = actualState[0] + str(int(actualState[1]) + 1)
          print(f"{previousState} -> {actualState}, {char}")
          continue
      elif actualState in transitions[actualState, nextState] and char == transitions[actualState, nextState][2]:
        previousState = actualState
        actualState = nextState
        print(f"{previousState} -> {actualState}, {char}")
        if nextState[0] + str(int(nextState[1]) + 1) in states:
          nextState = nextState[0] + str(int(nextState[1]) + 1)
          continue
        else:
          continue
      else:
        return False
      #FIXME end
    else:
      return False
