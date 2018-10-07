# Schreibe einen Code, der einen Fehler produziert
# Z.B. ZeroDivisionError
# Packe das ganze in ein try-except, und rette den Code

try:
    result = 22 / 0
    print result
except ZeroDivisionError:
    print "You chose 0! You lost!"
