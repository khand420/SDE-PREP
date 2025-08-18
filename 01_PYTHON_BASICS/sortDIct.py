d = {"Pasha": 32, "Badshah":12, "Mama Thakur": 19, "Tapu":443, 'altaf raja':3}

# print(d.keys())

print(sorted(d.items(), key= lambda x:x[0]))

revDict = {v:k for k,v in d.items()}
print(revDict) 