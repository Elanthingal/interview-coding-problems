
# Max substr from the given list

def substr(s):

    matcher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    curr = ""

    for char in s:
        curr += char
        if char.isupper() and curr not in matcher:
            out.append(curr[:-1])
            curr = ""
            curr += char
        elif char.islower() and curr not in matcher.lower():
            out.append(curr[:-1])
            curr = ""
            curr += char
            
    if curr:
        out.append(curr)
    return out

#find the pairs which are lower than the target, first list left to right and second list righ to left

def find(a,s,k):

    AF = iter(a)
    SF = iter(reversed(s))
    count = 0
    for idx in range(len(a)):
        if int(f"{next(AF)}{next(SF)}") < k:
            count += 1
    return count

print(find([1,2,3],[1,1,3],31))


print(substr("ABCDEFFDEfghCBA"))