# Convert Fahrenheit to Celsius

temp = input("Enter temperature: ")

let = ""
num = "0"

for i in temp:
    if i.isdigit():
        num += i
    else:
        let += i

num = float(num)

if let == "F":
    degC = (num - 32) * 5/9
    print(round(degC,2), "C")

elif let == "C":
    degF = 32 + num * 9/5
    print(round(degF,2), "F")

else:
    print("Tameez se likhna seekh")


