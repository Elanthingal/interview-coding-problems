
### Input = ["Narendra", "Modi", "Rahul", "Gandhi"]
### output = "NMRGaoaardhneiudnlhdira"

def mixMatch(A):

    ilen = max([len(x) for x in A])
    s = { x:iter(x) for x in A}
    out = ""
    for idx in range(ilen):
        for idx in s.keys():
            try:
                out += next(s[idx])
            except:
                pass
    return out

print(mixMatch(["Narendra", "Modi", "Rahul", "Gandhi"]))



