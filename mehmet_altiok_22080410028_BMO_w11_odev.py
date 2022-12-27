
#ilk olarak bir Sözcük oluşturuyoruz ve bu sözcüğe anahtarlar ekliyoruz.
tur_E=[]
sinav_sonuc ={
"isim": ["Ayşe K.","Ahmet M.","Nuri C.","Nawar T.","Suzan T.","Ala B."],
"cinsiyet": ["K","E","E","E","K","K"],
"Matematik": [80,60,77,25,36,77],
"Türkçe": [90,50,53,100,98,66]
}
sayi_E=0;sayi_K=0;mat_E=0;mat_K=0
for d in range(len(sinav_sonuc["cinsiyet"])):   #range ile listemizin uzunluğunu aldık
    if  sinav_sonuc["cinsiyet"][d] == "E":      #Burada Eğer cinsiyet listesinde "E" ile karşılaşırsa "sayi_E"yi bir arttır dedik
        sayi_E +=1 
        mat_E = mat_E + sinav_sonuc["Matematik"][d]
    else: 
        sayi_K +=1                               #Burada Eğer cinsiyet listesinde "K" ile karşılaşırsa "sayi_K"yı bir arttır dedik
        mat_K = mat_K + sinav_sonuc["Matematik"][d]
""" 
Alt taraftaki satırda sonuçları ekrana yazdırmasını istedik round fonksiyonunu kullanmızdaki amaç sayı karmaşasıından kurtulmak
round(*****,2) yaptım yani virgülden sonra 2 basamak bırak demektir.
"""
print("Erkeklerin Matematik Not Ortalaması:",round(mat_E/sayi_E,2) ,"\nKadınların Matematik Not Ortalaması:",round(mat_K/sayi_K,2) )
#Burayı For döngüsü açarak yapabiliriz. Fakat sum listede bulunan değerleri toplayan bir foksiyondur.
toplam=sum(sinav_sonuc["Türkçe"])
adet=len(sinav_sonuc["Türkçe"])
print("Türkçe Dersinin Sınıf Ortalaması:",round(toplam/adet,2))
"""
Burada Erkeklerin ve Kadınların türkçe notlarının girmek için liste açtım 
böylelikle max metotunu kullarak rahatlıkla en yüksek notu bulacağız.
"""
tur_E=[] 
tur_K=[]
for m in range(len(sinav_sonuc["cinsiyet"])):
    if sinav_sonuc["cinsiyet"][m]=="E":
       tur_E.append(sinav_sonuc["Türkçe"][m])
    else:
        tur_K.append(sinav_sonuc["Türkçe"][m])
print("Erkeklerin En Yükesek Türkçe Notu:",max(tur_E),"\nKadınların En Yüksek Türkçe Notu:",max(tur_K))