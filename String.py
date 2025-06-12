# Mavzu: String(str)
# 2025.04.30
# Muallif: Abdulloh

#Amaliyot

ism = 'Abdulloh'
familya = 'Otamirzayev'
shahar = "Uychi"
viloyat = "Namangan"
matn = "Men yangi 📱 sotib oldim"
smile = "😆"

print("Mening ismim " + ism)
print(ism + familya)
print(ism + ' ' + familya)

# f-string

ism_sharif = f"{ism} {familya}"
print(ism_sharif)
print(f"Salom mening ismim {ism}. {familya} {ism}")

# Maxsus belgilar

print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')

# String metodlar

print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())

meva = "    olma    "

print(meva)
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")

# Input

ism = input("Ismingiz nima?")
print("Assalomu aleykum, " + ism)

ism = input("Ismingiz nima?\n>>>")
print("Assalomu aleykum," + ism.title())


# Amaliyot 

kocha = "Navbahor"
mahalla = "Gulbog'"
tuman = "Uychi"
viloyat = "Namangan"

print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tummani " + viloyat + " viloyati, ")

print(" Iltimos, quyidagi ma'lumotlarni kiriting: ")
kocha = input(" Ko'changiz: ")
mahalla = input(" Mahallangiz: ")
tuman = input(" Tumaningiz: ")
viloyat = input(" Viloyatingiz: ")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")   

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())