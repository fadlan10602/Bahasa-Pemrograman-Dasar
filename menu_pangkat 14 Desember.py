print("Program menghitung x pangkat n")
x = 0
n = 0
pangkat = 1

def masukan():
    global x,n
    x = int(input("Inputkan nilai x : "))
    n = int(input("Inputkan nilai n : "))

def hitung():
    global x,n,pangkat
    for i in range(n):
        pangkat = pangkat*x

def tampil():
    print(x," pangkat ", n, "=", pangkat)
    
masukan()
hitung()
tampil()