#1
kupeler = ["0157","0233","0157","0891","0233","0412"]
print(len(set(kupeler)))
#2
sut = [485, 502, 478, 511, 495, 468, 507]
tuple(sut)
sut.sort()
print("en dusuk {}, en yuksek {}".format(sut[0],sut[-1]))
#print(min(sut), max(sut))
#3
sonuc = sut.sort()
print(sonuc)
#4
hedef = 480
sagmal = 14
bugun = 495
print(bugun > hedef)
print(bugun > hedef and sagmal < 15)
print(not bugun > hedef)
#5
hayvan = {
    "kupe":"0157",
    "ad":"boz",
    "dogum": {"tarih":"12.03.2023", "buzagi_cinsiyet": "disi"}
}
print("{} {} - {} tarihinde {} buzagi".format(hayvan["ad"].upper(), hayvan["kupe"], hayvan["dogum"]["tarih"], hayvan["dogum"]["buzagi_cinsiyet"]))
#6
#küpe ve doğum için tuple süt için list 
