def substring_count(s, length):
    counts = {}

    # for i in range(len(s) - length + 1):
    #     substring = s[i:i + length]
    #     counts[substring] = counts.get(substring, 0) + 1
    # return counts

    for i in range(len(s) - length+1):
        subs = s[i:i+length] 
        counts[subs] = counts.get(subs, 0)+1
    return counts    

    




print(substring_count("banana", 2))