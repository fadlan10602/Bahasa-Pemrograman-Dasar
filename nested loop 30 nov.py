for i in range(1,5,1):
    for j in range(0,3,1):
        print(i*j, end="")
    print()

#pola segitiga
baris=int(input('tentukan baris segitiga: '))
for i in range(1,baris+1):
    for j in range(1,i+1):
        print('*', end= " ")
    print()

#pola segitiga
baris=int(input('tentukan baris segitiga: '))
angka=1
for i in range(1,baris+1):
    for j in range(1,i+1):
        print(i, end= " ")
        i=i+1
    print()

#pola segitiga
baris=int(input('tentukan baris segitiga: '))
angka=1
for i in range(1,baris+1):
    for j in range(1,i+1):
        print(angka, end= " ")
        angka=angka+1
    print()