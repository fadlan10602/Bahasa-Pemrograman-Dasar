number_list = []
n = int(input("Input Ukuran List : "))
jum = 0
print("\n")
for i in range(0,n):
    print("Input nilai pada indeks ke -",i)
    List_item = int(input())
    jum = jum+List_item
    number_list.append(List_item)
    
print("List Data : ",number_list)
print("Jumlah : ",jum)
