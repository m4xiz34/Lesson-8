num = int(input("Numerator:  "))
dem = int(input("Denomerator:  "))

sum = num%dem

if sum == 0:
    print("Yes. It is divisable.")
else:
    print("No. It isn't.")
