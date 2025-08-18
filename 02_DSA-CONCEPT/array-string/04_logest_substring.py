# Given a string S, find the length of the longest substring without repeating characters.



def longestUniqueSubsttr(s):
    res = start = pos = 0
    temp = {}
    
    for i in s:
        if i in temp:
            end = temp.get(i, start-1)+1
            for c in s[start:end]: del temp[c]
            start = end
        # res, temp[i], pos = max(res, pos-start+1), pos, pos+1
        res =  max(res, pos-start+1)
        temp[i] = pos
        pos= pos+1
    return res



s= "geeksforgeeks"
print(longestUniqueSubsttr(s))
# Output:
# 7
# Explanation:
# Longest substring is
# "eksforg".


def longestUniqueSubsttr(self, S):
    d={}
    l=0
    mlen=0
    for r in range(len(S)):
        if S[r] in d and d[S[r]]>=l:
            l=d[S[r]]+1
        d[S[r]]=r
        mlen=max(mlen,r-l+1)
    return mlen





# Sliding Window

def longestUniqueSubsttr(self, S):
    # code here
    charSet = set()
    l, r, res = 0, 0, 0
    
    for r in range(len(S)):
        while charSet and S[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(S[r])
        res = max(res, r-l+1)
    
    return res