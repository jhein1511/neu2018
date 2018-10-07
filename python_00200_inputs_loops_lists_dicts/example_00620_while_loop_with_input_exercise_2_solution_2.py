# Schreibe eine while Schleife
# sie bricht nur dann ab, wenn der User "yes" oder "no" eingegeben hat
while True:
    answer = raw_input("Are you human?").strip()
    if answer.lower() in ["yes", "no"]:
        print "cool"
        break
    else:
        print "still awesome"
