rainbow = ["red", "orange", "green", "yellow", "blue", "black", "white", "aqua", "purple", "pink"]
del rainbow[5:8]
rainbow[2:4] = ["yellow", "green"]
rainbow[4:5] = ["blue", "indigo"]
rainbow[-2:] = "violet"
rainbow[-6:] = ["".join(rainbow[-6:])]
for i in rainbow:
    print (i)
