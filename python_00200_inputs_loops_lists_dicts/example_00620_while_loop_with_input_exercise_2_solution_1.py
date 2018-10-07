# coding=utf-8
# Schreibe eine while Schleife
# sie bricht nur dann ab, wenn der User "yes" oder "no" eingegeben hat
while True:
    answer = raw_input("Are you human?")
    if answer == "yes" or answer == "no":
        print "cool"
        break
    else:
        print "still awesome"

# diese Lösung ist gut, aber vielleicht können wir noch etwas mehr zusammenfassen, und auch großgeschriebene YES und NO gelten lassen