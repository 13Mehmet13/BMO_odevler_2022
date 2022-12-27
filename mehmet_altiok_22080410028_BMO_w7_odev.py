
#paralel kenarın içine str veya int değerlerinde herhangi bir şey girmediğimiz için boş bir listedir
kisiler=[]
""" girmek istedğimiz isimleri tek bir kisiler.append komutuna yazarsak listeye tek bir elaman olarak ekler
bu yüzden ayrı ayrı komutlar şeklinde yazmalıyız

ödev pdfinde kullnacının ekrana girdiği isimleri ekleyin diye belirtildiği için input kullnarak yaptım
fakat kodu yazan kişi girilecek isimleri belirleyecekse aşağıdaki komutları kullabiliriz.
kisiler.append("eklemek istedeiğimiz 1. isim")
kisiler.append("eklemek istedeiğimiz 2. isim")
kisiler.append("eklemek istedeiğimiz 3. isim") 

"""
kisiler.append(input("1. ismi giriniz: "))
kisiler.append(input("2. ismi giriniz: "))
kisiler.append(input("3. ismi giriniz: "))
print(kisiler)
print("Listenin Uzunlugu:",len(kisiler))
#2.liste elemanını yazdırmak için index 1'i kullanırız çünkü listelerde 1. elemanın indexi 0'dır
print("Listenin 2.Elemanı:",kisiler[1])
#kisiler.pop(2) veya kisiler.remove("Son Liste Elemanının ismi") metotlarınıda kullanarak silebilirz
kisiler.pop(-1)
print(kisiler)