import fileinput
# G -> graf
# dimensiune noduri cautate in G
k = int(input())

# nr de noduri din G
n = int(input())

# v = nodurile din G
v = []
for i in range(n):
  v.append(i+1)
 
# nr de muchii din G
m = int(input())

# muchiile din G
muchie = []

# e = perechile de muchii
e = []
# bag perechile de muchii in e
for i in range(m):
  muchie.append(input())
  e.append(muchie[i].split(" "))

lista = []

# orice nod poate fi ales in acele k noduri
# acesta este cazul care relateaza nodurile care fac parte dintr-o muchie
cazul1 = []
for i in range(m):
  for j in range(2):
    for l in range(k):
      lista.append(int(e[i][j])*k - l)
  cazul1.append(lista)
  lista = []

# acesta si cazul urmator sunt cazurile in care fiecare nod poate fi ales
# pe pozitia i insa doar un nod este ales
cazul2 = []
for l in range(k):
  for i in range(n):
    lista.append(v[i]*k - l)
  cazul2.append(lista)
  lista = []

cazul3 = []
j = 0
for l in range(n):
  for i in range(n):
    for x in range(k):
      if i > j:
        lista.append(v[j]*k - x)
        lista.append(v[i]*k - x)
        cazul3.append(lista)
      lista = []
  j = j + 1

# acesta este cazul in care un nod este ales o singura data
cazul4 = []
for i in range(n):
  for j in range(k):
    lista.append(v[i]*k - j)
  cazul4.append(lista)
  lista = []

# de aici pana la ultima linie am scris toata lista mea cu int-uri, intr-un sir
res = "("  

for i in range(len(cazul1)):
  for j in range(len(cazul1[i])):
    res = res + str(cazul1[i][j]) + "V"
  res = res[:-1]
  res = res + ")^("
res = res[:-1]
res = res + "("

for i in range(len(cazul2)):
  for j in range(len(cazul2[i])):
    res = res + str(cazul2[i][j]) + "V"
  res = res[:-1]
  res = res + ")^("
res = res[:-1]
res = res + "("

for i in range(len(cazul3)):
  for j in range(len(cazul3[i])):
    res = res + "~" + str(cazul3[i][j]) + "V"
  res = res[:-1]
  res = res + ")^("
res = res[:-1]
res = res + "("

for i in range(len(cazul4)):
  for j in range(len(cazul4[i])):
    res = res + "~" +str(cazul4[i][j]) + "V"
  res = res[:-1]
  res = res + ")^("
res = res[:-2]

print(res)