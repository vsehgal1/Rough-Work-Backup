# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")

def solution(N):
    # write your code in Python 3.6
    
    num = {2: "Codility", 3: "Test", 5:"Coders"}
    for i in range(1,N+1):
        factors = []
        if (i%2 == 0 or i%3 ==0 or i%5 ==0):
            for j in range(1,N+1):
                if (i%j == 0):
                    factors.append(j)
            if  all(elem in num  for elem in factors):
                print("CodilityTestCoders")
            else:
                for q in num:
                    if q in factors:
                        print(num[q], end ="")
                print("")
        else: print(i)
        
        
    pass
