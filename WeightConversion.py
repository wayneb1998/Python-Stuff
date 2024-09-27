weight = int(input("How much do you weigh?:  "))
unit = input("Is this in (L)bs or (K)g? Please input L or K:  ")
if unit.upper() == "L":
    conversion = weight * 0.45
    print(f'Your weight in LBs is: {conversion} LBs')
elif unit.upper() == "K":
    conversion2 = weight / 0.45
    print(f'Your weight in KG is: {conversion2} KGs ')









































