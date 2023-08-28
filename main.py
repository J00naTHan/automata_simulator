import os
from read_file import readFile
from verify import verify

fileName = input("Insira o nome do arquivo: ")
if not fileName.endswith(".txt"):
  fileName += ".txt"
fileName = os.path.join("testes", fileName)

initialState, alphabet, states, finalState, transitions, actualState = readFile(fileName)

entry = input("Insira a palavra para a verificação: ")

verification = verify(entry, alphabet, initialState, actualState, finalState, states, transitions)

if verification is True:
  print("\nAceita")
else:
  print("\nRejeita")
  
