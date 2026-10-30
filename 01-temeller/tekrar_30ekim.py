kupe = "TR34-0157"
print(kupe[5:])
print(kupe[-4:])

satir = "16.09.2026;485;120"
parca = satir.split(";")
print(parca[1]+parca[2])
#split her zaman metin döndürür bunlar sayı olmadığı için "485"+"120" sonucu 485120 çıkar....

sut = [485,502,478]
sonuc = sut.sort()
print(sonuc)
#sort listeyi yerinde sıralar sut listesini değiştirir fakat geriye bir şey vermez none oalrak görünür

kupeler = ["0157", "0233", "0157", "0891"]
print(len(kupeler))
print(len(set(kupeler)))

liste = ["a","b","c"]
liste.append("d")
liste.pop()
print(liste)
#append listenin sonuna d yi ekler pop ise () yani parantez boşsa listenin sonundakini atar
#sort append reverse geriye none döndürür pop istisna attığı elemanı geri verir x = liste.pop() dersek x "d" olur

hayvan = {"ad": "boz", "dogum": {"tarih": "12.03.2023"}}
print(hayvan["dogum"]["tarih"])

t = (1, 2, 3)
t[0] = 5
print(t)
# tuple değişmez dogru Ama Python değiştirme isteğini sessizce yok saymaz, kırmızı bir hata verip durur

#%%2.tur
tarih = "30.10.2026"
print(tarih[:2])
print(tarih[3:5])
print(tarih[-4:])


satir = "30.10.2026;248;244"
parca = satir.split(";")
print("{} tarihinde toplam {} litre sut".format(parca[0], int(parca[1])+ int(parca[2])))


sut = [485, 502, 478]
sirali = sorted(sut)
print(sut)
print(sirali)
sut.sort()
print(sut)


sagmal = ["0157", "0233"]
sagmal.append("0891")
cikan = sagmal.pop(0)
print(sagmal)
print(cikan)