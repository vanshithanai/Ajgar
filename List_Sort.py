# Make a list of 5 numbers taken from the user, sort it into asceding/descending as per user instruction

dotdot = input("Enter numbers separated with space: ")
todo = input("Enter A for Ascending and D for Descedning: ")
dotdot = (dotdot.split(" "))
print(dotdot)
numdotdot = [float(i) for i in dotdot]

if todo == "A":
    for i in range(len(numdotdot)):
        for j in range(len(numdotdot)):
            if numdotdot[i] < numdotdot[j]:
                h = numdotdot[j]
                numdotdot[j] = numdotdot[i]
                numdotdot[i] = h
    print(numdotdot)

elif todo == "D":
    for i in range(len(numdotdot)):
        for j in range(len(numdotdot)):
            if numdotdot[i] > numdotdot[j]:
                h = numdotdot[j]
                numdotdot[j] = numdotdot[i]
                numdotdot[i] = h
    print(numdotdot)
    

else:
    print ("NIKAL")


