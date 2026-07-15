 # Exercice 1 — Premier script 

prenom = "yanis" 
naissance = 2007 
print(f"je m'appelle {prenom} je suis né en {naissance}") 

# Exercice 2 — Types et conversions
# Sans exécuter, prédis le résultat de chaque ligne (écris tes prédictions, ensuite seulement vérifie dans Python) :

print(type(3.0)) #float 
print("5" + "3") #53
print(int("5") + 3) #8 
print(str(5) + "3") #53
print(type(input("Tape un nombre : "))) #str

#Exercice 3 — Interaction
#Script qui demande à l'utilisateur son année de naissance, puis affiche son âge en 2026. 
# Format de sortie attendu : Tu as 19 ans en 2026.

naissance = int(input("Tapez votre année de naissance : ")) 
age = 2026 - naissance
print(f"tu as {age} ans en 2026")

#Exercice4 -  Pratique autonome (20-30 min)

#Exercice A — Calcul de moyenne
#Demande à l'utilisateur 3 notes (via input), calcule et affiche la moyenne avec une f-string.
#Format attendu : Ta moyenne est de X.XX

note1 = float(input("Votre premiere note : "))
note2 = float(input("Votre deuxieme note : "))
note3 = float(input("Votre troisieme note : "))

moyenne = (note1 + note2 + note3)/3 
print(f"Votre moyenne est de : {moyenne:.2f}")

#Exercice B — Conversion de température
#Demande une température en Celsius, convertis-la en Fahrenheit, affiche le résultat.
#Formule : F = C * 9/5 + 32

celcius = float(input("Tappez une temperature en celcius : "))
Fahrenheit = celcius * 9/5 + 32 
print(f"{celcius}C = {Fahrenheit}F")

#Exercice C — Piège de type
#Sans exécuter, prédis ce qu'affiche ce code, puis vérifie :

a = input("Nombre 1 : ")
b = input("Nombre 2 : ")
print(a + b)

#Si l'utilisateur tape 10 puis 5, le résultat est-il 15 ou 105 ? Explique pourquoi en une phrase.
# ça fais 105 car on concatene les chaine str car input nous renvoie des str 