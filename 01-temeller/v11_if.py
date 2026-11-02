#%% Video 11 if
hava_durumu = "yagisli"
if hava_durumu == "yagisli":
    print("semsiye al")

hava_durumu = "karlı"
if hava_durumu == "yagisli":
    print("semsiyeni al")
else:
    print("bir şey yapma")

hava_durumu = "gunesli"
if hava_durumu == "karlı":
    print("atkını al")
elif hava_durumu == "yagmurlu":
    print("semsiyeni al")
else:
    print("tadını cıkar")
#%% alistirma
#1
satir = "02.11.2026:478.7"
hedef = 480
parca = satir.split(":")
sut = float(parca[1])
gun = parca[0]
if sut < hedef:
    print("{}: hedefin {} litre altında".format(gun,round(hedef-sut,1)))
else:
    print("{}: hedef tuttu".format(gun))
#2
yem_stok = 350
gunluk_yem = 120
kac_gun_yetecek = round((yem_stok / gunluk_yem),1)
print(kac_gun_yetecek)
if kac_gun_yetecek < 2:
    print("ACIL: yem siparis et")
elif kac_gun_yetecek < 5:
    print("Bu hafta siparis et")
else:
    print("Stok yeterli")
#ilk 5 ten az mı ddiye sorsaydık evet diyip döngüden çıkardı hatalı bir kullanım olurdu

#3
kupe = "TR35-0412"
parca = kupe.split("-")
if parca[0] == "TR34":
    print("Bizim ilden")
else:
    print("disaridan gelen hayvan: {}".format(parca[0]))
#3 un 2.yolu ve sanırım senin istediğin yol ikisinide yaptım 
kupe = "TR35-0412"
if kupe[0:4] == "TR34":
    print("Bizim ilden")
else:
    print("disaridan gelen hayvan: {}".format(kupe[0:4]))

#4
cuzdan = 100
secilen_sure = 25
gecen_sure = 12
if gecen_sure >= secilen_sure:
    cuzdan += secilen_sure
    print("Seans tamamlandi! +{} para".format(secilen_sure))
elif gecen_sure < 5:
    print("Cok kısa, para yok")
else:
    cuzdan += gecen_sure
    print("Erken bitti, +{} para".format(gecen_sure))
print("Cüzdan bakiyesi: {}".format(cuzdan))

#5
#kitap
#spor, su, erken kalk
#daha 3 aliskanlik var 
