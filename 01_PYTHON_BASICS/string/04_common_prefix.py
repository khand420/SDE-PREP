def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in strs[1:]:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
    return prefix


strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))