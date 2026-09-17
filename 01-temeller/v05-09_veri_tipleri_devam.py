# %% boolen 5.video
a = True
b = False

print(a)

yas1 = 20
yas2 = 18
print(yas2 > 18)

yas2 == 18

yas2 != 18

not yas2 > 18

not yas2 == 18 
# %% Video 6 List ve Set

liste = ["a","b","c","d","e","a"]
print(liste)

liste = liste +["f"]
liste
liste[4:5]

liste.append("g")#g yi eklemek icin.append   append de listeye tekrar atamaya gerek yok liste = liste.... gibi
liste

liste.pop() #listenin son elemanini atmak icin.pop
liste

liste.pop(5)
print(liste)

sayilar = [123,2431,4534,32,32,32,2,2]
sayilar.sort()
print(sayilar)

sayilar.reverse()
print(sayilar)

set(sayilar)
# %% Video 7 Tuple

liste = ["a","b","c","d","e","a"]
print(liste)
tup = ("a","b","c","d","e","a")
print(tup)

liste[0] = 222
liste

#tup[0] = 222  # tuple değiştirilemez
#tup

tup.count("a")
tup.count("True")
tup.index("b")
tup.index("a")
# %% Video 8 Dictionary

dict1 = {"isim": "Hsyn","yas":32, "lokasyon": " izmir"}
dict1

dict2 = {
    "isim":"Hsyn",
    "yas": 32,
    #"lokasyon":"izmir",
    "dogdugu_ulke":"Turkiye"
    }

dict3 = {
    "isim":"Hsyn",
    "yas": 32,
    "lokasyon":{
        "dogdugu_sehir":"izmir"
        }
    }
dict3

dict2["yas"]

dict3["lokasyon"]["dogdugu_sehir"]

dict2.get("yas")

dict3.keys()
dict3.values()

dict3.items() #her bir satırı tek tek 
