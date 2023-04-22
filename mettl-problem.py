""" 
  A company has hired N interns, labeled from 1 to N. Each intern is given a device which generates a number everyday that will be used as a password for their authentication at the office door every day in the morning. The internship is for 50 days numbered from 0 to 49. Initially (on the 1st day), the number in the device of the kth intern will be equal to (5000"k). 
  
  From the 2nd day (ie., i=1), a new number will be generated every day in each device in the following way 
        
        • Day(i)= Day(i-1) + 5000+ i 
    
    Find the label of an intern from the given password used by him/her. 
  
  Input Specification: 
    input1: N, number of interns 
    input2: P, password used 
    Output: 3 
    
    Explanation: 
      15000 is the number of the third intern on day 0 
      20001 is the number of the third inter on day 1
      25003 is the number of the third intern on day 2
    
    Output Specification: Return the label of the intem to whom the given word belongs to 
  
      Example 1: 
        Input: 2 
        input2: 5000 
        Output: 1 
      
        Explanation: 5000 is the number of the first intern on day 0. 
      
      Example 2: 
        input1: 10 
        input2: 25003 
        Output: 3 
        
        Explanation: 25003 in the number of the third into an nannt in the number of the third 
 """



def prevPassword(intern=4, days=5):
    
    password = 0
    
    for i in range(days):
        if i == 0:
            password += 5000 * intern
        else:
            password += 5000 + i
    return password
    

def check(interns, passwords):
    
    for day in range(49):
        for intern in range(interns):
            if(day == 0 and (intern * 5000) == passwords):
                return intern
            else:
                if(prevPassword(intern , day + 1) == passwords):
                    return intern

print(check(10, 20001))
    