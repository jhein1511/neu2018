# coding=utf-8
# Schreibe eine Schleife, die nach einem Input fragt,
# bis man eines der Grundrechenarten eingegeben hat.
while True:
    answer = raw_input("Enter a valid operation (+ - * /): ")
    if answer in ["*", "+", "-", "/"]:
        print "Thank you"
        break

# diese lösung ist besser. Achte auf den Unterschied
