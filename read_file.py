def readFile(fileName):
  with open(fileName) as file:
    lines = file.readlines()

  initialState = actualState = lines[0].strip()
  alphabet = lines[1].strip().split()
  states = lines[2].strip().split()
  finalState = lines[3].strip().split()
  transitions = {}

  for line in lines[4:]:
    lineList = line.strip().split()
    transitions[lineList[0], lineList[1]] = lineList
    
  return initialState, alphabet, states, finalState, transitions, actualState
  
