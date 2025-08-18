s = 'avd#fbgf@gd%gh&ghkl*lg'

new_str = [i for i in s if i.isalpha()]
# print(new_str)

new_str.reverse()
new_indx = 0
lst = []

for i in s:
    if i.isalpha():
        lst.append(new_str[new_indx])
        new_indx+=1
    else:
        lst.append(i)

lst = "".join(lst)
print((lst))



