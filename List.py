lst = ["apple", "Guave", "Mango", "Banana", "Kiwi"]

print ("Length of List:", len(lst))
print ("First Element:", lst[0])
print ("Last Element:", lst[-1])

lst.append("Papaya")
print ("Updated List :", lst)

lst.sort()
print ("Updated List :", lst)

lst.pop(1)
print ("Updated List :", lst)

lst.reverse()
print ("Reversed List :", lst)

print ("Multiplication on List :", lst*2)

lst = lst[:4]
print ("SLiced List :", lst)

lst.clear()
print("Updated List :", lst)