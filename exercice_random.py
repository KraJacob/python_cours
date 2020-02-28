import random
a = random.randint(0, 50)
b = random.randint(0, 50)
if a == b:
    print("Le nombre a et le nombre b sont égaux.")
elif b > a:
    print("Le nombre b est plus grand que le nombre a.")
elif b < a :
    print("Le nombre a est plus grand que le nombre b.")