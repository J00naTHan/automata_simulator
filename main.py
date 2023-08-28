#Function to read the file and define it's data as variables
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

  print(initialState, "\n", alphabet, "\n", states, "\n", finalState, "\n", transitions, "\n", actualState, "\n")

  return initialState, alphabet, states, finalState, transitions, actualState

#Function to compare user's input with file's information
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

#Main execution, formats file's name input and gets it's data
fileName = input("Insira o nome do arquivo: ")
if not fileName.endswith(".txt"):
  fileName += ".txt"

initialState,alphabet,states,finalState,transitions, actualState = readFile(fileName)

entry = input("Insira a palavra para a verificação: ")

verification = verify(entry, alphabet, initialState, actualState, finalState, states, transitions)

if verification is True:
  print("True")
else:
  print("False")
