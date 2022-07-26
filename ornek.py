"""Print İşlem"""
print("Enes")

"""Değişken,Veri Tipleri"""
a=3
b=5.5
c="Enes"
d=[1,2,3,4,5]
e={"enes":1,"emre":2,}
f=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

"""Matematik Operatörler"""

print(4+3)
print(10-3)
print(8/2)
print(10%4)
print(10//4)

print("#"*1)
print("#"*2)
print("#"*3)
print("#"*4)

"""String Ve Liste İndekslenmesi"""

isim="Enes"
sayı=[1,2,3,4,5]

print(isim[0])
print(len(isim))
print(sayı[len(sayı)-1])
# ------>>İKİNCİ İNDEKSE KADAR AL
print(sayı[0:2]) 
print(isim[2:4]) 

""" İNPUT ALMA """

# Değerler String olarak tutulur.İşlem yapmak için İnte dönüştür

# ilkSayı = int(input("İlk sayıyı giriniz"))
# ikinciSayı = int(input("İkinci sayıyı giriniz"))

# print("Sayılar toplamı = ",ilkSayı+ikinciSayı)

"""KOŞUL DURUMLARI"""
# yas = int(input("Yaşınızı giriniz"))

# if 0<yas<15:
#     print("Veletsiniz")
# elif yas<0:
#     print("Yaşınız negatif değer olamaz")
#     yas = int(input("Yaşınızı giriniz"))
# else :
#     print("Velet Değilsiniz")   

i=0
while (i<20):
    if i==5 :
        break
    print("i:",i)
    i = 1+i

    """Liste İçi Gezinme"""

q = [1,2,3,4,5,6,7]
for eleman in q:
    print(eleman)

 # -----> Range fonksiyonu   
 # Verdiğimiz aralıkta liste oluşturur

for sayi in range(1,10):
    print(sayi)

    """Fonksiyonlar"""

def selamla(isim="İsimsiz"):
       print("Merhaba ",isim)

selamla("Enes")       
      
"""Bazı Methodlar"""

u = "Araba"
y=[1,2,3,4,5]
print(u.startswith("A"))
y.append(7)
y.pop(0)

print(y)

"""Dosya Yapıları"""

file = open("dosya.txt","w")

file.write("Naber Python")

file.close()
    
    





