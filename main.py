fileName = input("Insira o nome do arquivo: ")
if not fileName.endswith(".txt"):
  fileName += ".txt"

initialState, alphabet, states, finalState, transitions, actualState = readFile(fileName)

entry = input("Insira a palavra para a verificação: ")

verification = verify(entry, alphabet, initialState, actualState, finalState, states, transitions)

if verification is True:
  print("True")
else:
  print("False")
  
