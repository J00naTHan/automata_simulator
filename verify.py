def verify(entry, alphabet, initialState, actualState, finalState, states, transitions):
  nextState = actualState[0] + str(int(actualState[1]) + 1)
  previousState = actualState
  for char in entry:
    if char in alphabet:
      #w.i.p
      if (actualState, actualState) in transitions and actualState in transitions[actualState, actualState] and char == transitions[actualState, actualState][2]:
        if actualState in finalState and char == entry[-1]:
          return True
        else:
          continue
      elif (actualState, previousState) in transitions:
        if actualState in transitions[actualState, previousState] and char == transitions[actualState, previousState][2]:
          if actualState in finalState and char == entry[-1]:
            return True
          previousState = actualState
          actualState = previousState
          nextState = actualState[0] + str(int(actualState[1]) + 1)
      elif actualState in transitions[actualState, nextState] and char == transitions[actualState, nextState][2]:
        if actualState in finalState and char == entry[-1]:
          return True
        previousState = actualState
        actualState = nextState
        if nextState[0] + str(int(nextState[1]) + 1) in finalState:
          nextState = nextState[0] + str(int(nextState[1]) + 1)
          continue
        else:
          continue
      else:
        return False
      #end w.i.p
    else:
      return False
