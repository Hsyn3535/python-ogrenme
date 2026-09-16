kupe = "TR34-0157"
print(kupe[5:])

print(kupe[-4:])

satir = "16.09.2026;485;120"
print("{} tarihinde {} litre sut,{} kg yem".format(satir.split(";")[0],satir.split(";")[1],satir.split(";")[2]))

sut =float(satir.split(";")[1])
sagmal = 14
print(round(sut / sagmal,1))

s = "sagmal"
print(s[2:5])
print(s[-1])
print(s[::2])
print(len(s))
print(s[1::2])

a = "boz"
b = 18.5
print("{} adli hayvan bugun {} litre sut verdi".format(a.upper(),b))
