def len_pattern_pair(pattern, secuence):
  acum = 0
  for i in range(len(secuence) -1):
      pair = secuence[i] + secuence[i+1]
      if pair == pattern:
        acum = acum + 1
    
  return acum;

def len_single_letter(letter, secuence):
  acum = 0
  for i in range(len(secuence) -1):
      if secuence[i] == letter:
        acum = acum + 1
  return acum

partidos = "LLLWEWELLWEEWLLELWLWLLWLWWWLLLLLWWWWWWEEELELWWLWLELWLW" 

#input("Escribir de forma seguida los últimos resultados del equipo-L perdida, E empate, W victoria: ")

# Contamos cuantas victorias hay dado que ganó
nWW = len_pattern_pair("WW", partidos)

# Contamos cuantas derrotas hay dado que ganó
nWL = len_pattern_pair("WL", partidos)

# Contamos cuantos empates hay dado que ganó
nWE = len_pattern_pair("WE", partidos)

# Contamos cuantas victorias hay dado que perdió
nLW = len_pattern_pair("LW", partidos)

# Contamos cuantas derrotas hay dado que perdió
nLL = len_pattern_pair("LL", partidos)

# Contamos cuantos empates hay dado que perdió
nLE = len_pattern_pair("LE", partidos)

# Contamos cuantas victorias hay dado que empató
nEW= len_pattern_pair("EW", partidos)

# Contamos cuantos empates hay dado que empató
nEE= len_pattern_pair("EE", partidos)

# Contamos cuantas derrotas hay dado que empató
nEL= len_pattern_pair("EL", partidos)

# Cuantas victorias hay antes de que suceda otro evento
nW = len_single_letter("W", partidos)

# Cuantas derrotas hay antes de que suceda otro evento
nL = len_single_letter("L", partidos)

# Cuantas derrotas hay antes de que suceda otro evento
nE = len_single_letter("E", partidos)

# Probabilidad de que gane dado que ganó 
P_W_W = nWW/nW 

# Probabilidad de que gane dado que perdió 
P_W_L = nLW/nL

# Probabilidad de que pierda dado que ganó
P_L_W = nWL/nW

# Probabilidad de que pierda dado que perdió
P_L_L = nLL/nL

# Probabilidad de que gane dado que empató
P_W_E = nEW/nE

# Probabilidad de que empate dado que ganó
P_E_W = nWE/nW

# Probabilidad de que empate dado que empató
P_E_E = nEE/nE

# Probabilidad de que empate dado que perdió
P_E_L = nLE/nL

# Probabilidad de que pierda dado que empató
P_L_E = nEL/nE

print("Probabilidad de que gane a pesar de haber ganado el partido anterior ",P_W_W)
print("Probabilidad de que gane a pesar de haber empatado el partido anterior ",P_W_E)
print("Probabilidad de que gane a pesar de haber perdido el partido anterior ",P_W_L)
print("Probabilidad de que empate a pesar de haber ganado el partido anterior",P_E_W)
print("Probabilidad de que empate a pesar de haber empatado el partido anteior",P_E_E)
print("Probabilidad de que empate a pesar de haber perdido el partido anterior",P_E_L)
print("Probabilidad de que pierda a pesar de haber ganado el partido anterior ",P_L_W)
print("Probabilidad de que pierda a pesar de haber empatado el partido anterior ",P_L_E)
print("Probabilidad de que pierda a pesar de haber perdido el partido anterior",P_L_L)

import numpy as np

# Definimos cuantos juegos futuros queremos a futuro para la predicción (n = juegos futuros)
n = 8

print (n)

# El estado inicial es que gane
X0 = np.array([[1],[0],[0]])

# Definimos la matriz de transición
T = np.array([[P_W_W, P_E_W, P_L_W], [P_W_E, P_E_E,P_L_E], [P_W_L, P_E_L, P_L_L]])
print("Matriz de transición: \n",T)

# La matriz en el juego n 
Xn = np.linalg.matrix_power(T,n)*X0
print("Matriz T elevada a n:\n",Xn)