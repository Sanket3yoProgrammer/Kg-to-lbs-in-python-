weight = float(input("Your Weight:"))
kglbs = input("Convert to kg or lbs: ")
if kglbs == "lbs":
    print(weight * 2.205)
elif kglbs == "kg":
    print(weight / 2.205)
