#%%v12
yorum_birakanlar = ["Huseyin YILMAZ", "Furkan DIREN", "Emre kayik", "Berat Koc"]
for kullanici in yorum_birakanlar:
    print(kullanici)

kullanici_sayisi = 0
for kullanici in yorum_birakanlar:
    kullanici_sayisi += 1
    print(kullanici_sayisi, kullanici)

kullanici_sayisi = 0
for kullanici in yorum_birakanlar:
    kullanici_sayisi += 1
    ad, soyad = kullanici.split()[0], kullanici.split()[1]
    print("{0}. kullanicinin Adi {1} ve soyadi {2}".format(kullanici_sayisi, ad, soyad))

moderator = "Huseyin YILMAZ"
kullanici_sayisi = 0
moderator_sayisi = 0
for kullanici in yorum_birakanlar:
    ad, soyad = kullanici.split()[0], kullanici.split()[1]
    if kullanici == moderator:
        moderator_sayisi += 1
        print("{0}. Moderatorun Adi {1} ve soyadi {2}".format(moderator_sayisi, ad, soyad))
    else:
        kullanici_sayisi += 1
        print("{0}. Kullanicinin Adi {1} ve soyadi {2}".format(kullanici_sayisi, ad, soyad))

#%%v13
tup1 = (1, 3, 5, 7)
for sayi in tup1:
    print(sayi)

liste = [[1,2],[3,4],["a","b"]]
for x,y in liste:
    print(x,y)

liste = [[1,2],[3,4]]
for x,y in liste:
    print(x,y)

kullanici1 = {
    "ad": "Huseyin",
    "soyad": "YILMAZ"
}
kullanici1.keys()

kullanici1 = {
    "ad": "Huseyin",
    "soyad": "YILMAZ"
}
kullanici1.values()

kullanici1 = {
    "ad": "Huseyin",
    "soyad": "YILMAZ"
}
kullanici1.items()

for k, v in kullanici1.items():
    print("Key: {} \t Value: {}".format(k, v))

#%% alistirma 0
sira = ["0157", "0233", "0891", "0412"]
cikan = sira.pop(1)
for kupe in sira:
    print(kupe)
print("cikan:", cikan)
#0157
#0891
#0412
#cikan:0233
#%% alistirma 1
kayitlar = ["27.10.2026:482.5", "28.10.2026:478.7", "29.10.2026:490.0", "30.10.2026:471.2", "31.10.2026:485.3"]
toplam_sut = 0
gun_sayisi = 0
for x in kayitlar:
    tarih, sut = x.split(":")
    toplam_sut += float(sut)
    gun_sayisi += 1
ortalama = round((toplam_sut / gun_sayisi),1)
print(f"Toplam: {round(toplam_sut,1)} litre ve Ortalama {ortalama} litre")

#%% alistirma 2
kayitlar = ["27.10.2026:482.5", "28.10.2026:478.7", "29.10.2026:490.0", "30.10.2026:471.2", "31.10.2026:485.3"]
hedef = 480
hedef_altinda_kalan_gun = 0
gun_sayisi = 0
for x in kayitlar:
    tarih, sut = x.split(":")[0],float(x.split(":")[1])
    gun_sayisi += 1
    if sut < hedef:
        print(f"{tarih[:5]}: hedefin {round((hedef - sut),1)} litre altında")
        hedef_altinda_kalan_gun += 1
    else:
        print(f"{tarih} tarihinde hedef tutturuldu")
print(f"{gun_sayisi} günün {hedef_altinda_kalan_gun} gün kadarında hedef tutmadı")

#%%alistirma 3
hayvanlar = {"TR340157": "sagmal", "TR340233": "kuru", "TR340891": "sagmal", "TR340412": "duve"}
sagmal_sayisi = 0
kuru_sayisi = 0
diger = 0
for kupe_numarası, durum in hayvanlar.items():
    print(kupe_numarası[-4:],durum)
    if durum == "sagmal":
        sagmal_sayisi += 1
    elif durum == "kuru":
        kuru_sayisi += 1
    else:
        diger += 1
print(f"Sagmal: {sagmal_sayisi}, Kuru: {kuru_sayisi}, Diger: {diger}")
    
    
#%%alistirma 4
seanslar = [("kitap", 25, 25), ("spor", 30, 12), ("su", 10, 3), ("kitap", 25, 25)]
cuzdan = 100
seans_sayisi = 0
for aliskanlik,secilen_sure,gecen_sure in seanslar:
    if gecen_sure >= secilen_sure:
        cuzdan += secilen_sure
        seans_sayisi += 1
        print(f"{aliskanlik} seansı tamamladınız +{secilen_sure} para")
    elif gecen_sure < 5:
        print(f"{aliskanlik} kısa sure")
    else:
        cuzdan += gecen_sure
        print(f"{aliskanlik} icin gecen sure kadar +{gecen_sure} para kazandınız")
print(f"bakiyeniz {cuzdan} su kadar seans tamamladınız {seans_sayisi}")

    
    
    


