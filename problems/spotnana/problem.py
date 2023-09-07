# """
# Write a program that accepts input in this form: s3t1z5. Here any character is followed by a number. The program should return a string where the character is repeated for the corresponding number of times.
# output: ssstzzzzz
# """

def extract(texts=""):
    output = ""
    for idx, text in enumerate(texts):
        if idx % 2 != 0:
            output += f"{texts[idx-1]}"*int(texts[idx])
    return output

print(extract(texts="s3t1z5"))
print(extract(texts="s3a0"))


# Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits. We are given two arrays that represent the arrival and departure times of trains that stop.
# Examples:
# Input: arr[] = [900, 940, 950, 1100, 1500, 1800], dep[] = [910, 1200, 1120, 1130, 1900, 2000]
# Output: 3
# Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)
# Input: a

def find_minimum_platform(A, D):
    min_x = 0 
    curr  = 0 
    S = [] 
    S.extend(A)
    S.extend(D)
    C = sorted(S)
    print(A)
    for a in C: 
        if a in A:
            min_x += 1
        else:
            min_x -= 1
        if curr < min_x:
            curr = min_x
    return curr

print(find_minimum_platform([900, 940], [910, 1200]))
print(find_minimum_platform([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000]))
