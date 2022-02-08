lucky_numbers= [4,7,9,11,14,777,37]
friends = ["Karel", "John", "Mike", "Denzel"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Karen")
friends.remove("John")
friends.pop() # remove last one Denzel
friends.reverse()
friends2=friends.copy() #proste to okopiruje
#friends.sort() seradit podle abecedy nebo od nejmensiho
print(friends.index("Karel"))
print(friends.count("John"))
#friends.clear()
print(friends)