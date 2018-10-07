# catch an error when translating a string to an integer
# E.G. int("text")

try:
    int("abc")
except Exception:
    print "Error"

print "Code is continuing"
