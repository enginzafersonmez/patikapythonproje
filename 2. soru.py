'''
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

'''

liste1 = [[1, 2], [3, 4], [5, 6, 7]]
liste2 = []
def sorting(n):
    n=n[::-1] #ana listedeki elemanlar tersine döndürüldü.
    for i in range(len(n)):
        listTemp = n[i] #Geçici Liste oluşturuldu ve 1. listenin ilk elemanı buraya eklendi
        listTemp = listTemp[::-1] #Geçici liste içindeki elemanlar tersine döndürüldü
        liste2.append(listTemp) #Geçici liste içindeki düzenlenmiş elemanlar 2. listeye eklendi.


sorting(liste1)

print(liste2)