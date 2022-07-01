#print
print("belajar pyton")
#tipe data dictionary
saya = {"nama":"Firman", "umur": 17}
del saya['umur'] # hapus entri dengan key 'umur'
#dict.clear()     # hapus semua entri di dict
#del dict         # hapus dictionary yang sudah ada
print(saya)
#check type
print(type(saya))

#ifelse
bilangan=10

if(bilangan>10):
    print('halo')
elif(bilangan<10):
    print('hai')
else:
    print('yoyoi')

#loop
list = [1,2,3,4,5,6,7,8,9]
for x in list:
    print(x)

#list
list = ['fisika','kimia',10,20]
print("value list ke 3 :" ,list[2])
print ("list[0:2]: ", list[0:2])
#update list 
list[1] = 'matematika'
print(list)
#delete list 
del list[3]
print(list)

#Contoh sederhana pembuatan tuple pada bahasa pemrograman python
tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup = ('fisika', 'kimia', 1993, 2017)
print(tup)

# hapus tuple dengan statement del
del tup

text = 'uhuy'
def test(str):
    print(str)
    return

test(text)