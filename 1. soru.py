'''
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
'''

instanceList = [[[1,'a'],['cat'],2],[[[3]],'dog'],4,5]

flattenList = []

def flatten(n): #Void fonksiyonu oluşturuldu. Çünkü eğer return ile yazsaydık ilk append de fonksiyon durdurulmuş olurdu ve düzleştirilmezdi.
    for i in n:
        if isinstance(i,list): #i değişkenin tipinin liste olup olmadığını kontrol ediyor. Eğer i değeri liste ise alt kısımda fonksiyonu tekrar çalıştırarak iç listeye giriyor.
            flatten(i)
        else:
            flattenList.append(i) #i değerinin tipi artık liste olmadığı zaman (int veya str) flattenList isimli listeye ekliyor.

flatten(instanceList)

print(flattenList)