
#Find Anagram Staring Index 

def findA(s="dbacedcbaed", p="abcd"):

    c = p
    out = []
   
    for idx, val in enumerate(s):
        if val in p:
            c = c.replace(val,"")
            pattern = True
            if idx <= len(s)-len(c)-1:
                for jdx in range(len(c)):
                    if s[idx+jdx+1] not in c:
                        pattern = False
            else:
                pattern = False
           
            if pattern:
                out.append(idx)
        c = p    
    print(out)
   
findA()


#Linked list Clone
#Linked list array
    




