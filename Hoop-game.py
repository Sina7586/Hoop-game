#Hope game with loop breaking commands in Python and condition precedence :)
n = 0
while n <= 39:
    n += 1
    if n == 37:
        break
    if n % 3 == 0 and n % 4 == 0:# (Or n % 12 == 0) Remember the least common multiple (LCM) of the number:)
        print("Hoop Hip")
        continue
    if n % 3 == 0:
        print("Hoop")
        continue
    if n % 4 == 0:
        print("Hip")
        continue
    print(n)
#ُSina_Afshar
#Github account --> @Sina7586

