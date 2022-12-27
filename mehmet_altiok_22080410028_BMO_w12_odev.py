# #ilk olarak bir sözlük açıyoruz ve anahtarları ekliyoruz. 
sinav_sonuc ={
"isim": ["Ayşe K.","Ahmet M.","Nuri C.","Nawar T.","Suzan T.","Ala B."],
"cinsiyet": ["K","E","E","E","K","K"],
"Vize": [80,60,77,25,36,75],
"Final": [90,60,53,100,98,66]
}
#yenikayit adında bir fonksiyon oluşturdum içine yeni kayıt için gerekli kodları girdim ve geçme notlarını hesapladım
def yenikayit():
#Yeni kayıt için sayı istedim
    kac=int(input("Kac Yeni Öğrenci Eklemek İstersiniz: ")) 
    a=6
    for i in range(kac):
        """burada girilmesi gereken değerleri "int" veya "str" olarak belirttim çünkü isimler lsitesi "int" değer girilerek veya 
        vize notlar bölümüne "str" değer girilerek kodun çalmamasi sağlanabilir. 
        bunu yapmamış dahi olsaydım. 26. satırda işlemden dolayı hata verecekti"""
        sinav_sonuc["isim"].append(str(input("Lütfen Ogrenci Adi Giriniz: ")))
        sinav_sonuc["cinsiyet"].append(str(input(f"Lütfen {sinav_sonuc['isim'][a]} Ogrencinin Cinsiyetini Giriniz: ")))
        sinav_sonuc["Vize"].append(int(input(f"Lütfen {sinav_sonuc['isim'][a]} Ogrencisinin Vize Notunu Giriniz: ")))
        sinav_sonuc["Final"].append(int(input(f"Lütfen {sinav_sonuc['isim'][a]} Ogrencisinin Final Notunu Giriniz: ")))
        a+=1
    """burada sinav_sonuc sözlüğüne yeni bir boş "Geçme Notu" anahtarı eklemiş oldum. bunu burada ekleme 
    sebebim "tabloya yeni bir sütunda kaydeden bir fonksiyon tanımlayın" demeniz bu sebeple bende fonksiyonun içinde anahtarı ekledim"""
    sinav_sonuc["Geçme Notu"]= []
    for j in range(len(sinav_sonuc["isim"])):
        ortnot=(sinav_sonuc["Vize"][j]*0.3)+(sinav_sonuc["Final"][j]*0.7)
        sinav_sonuc["Geçme Notu"].append(round(ortnot, 2))
yenikayit() #Fonksiyonu çağırdım
print(sinav_sonuc) #sinav_sonuc adlı sözlüğü ekrana yazdırdım