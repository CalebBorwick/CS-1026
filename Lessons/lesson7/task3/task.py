# Replace the placeholders and complete the Python program.

f = open("filmdata.csv","r",encoding="utf-8")
for line in f:
    entries = line.split(",")
    if float(entries[0]) < 1990:
        print(entries[0],entries[2])
f.close()
