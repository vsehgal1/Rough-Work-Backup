import random

def maxSubArraySum(lst): 
    max_sf = 0
    max_end = 0
    start = 0
    stop = 0
    for i in range(0, len(lst)): 
        max_end = max_end + lst[i]
        if max_end < 0:
            if max_end <0 and max_end > max_sf:
                start=i
                stop=i
                max_end = 0
            else: 
                if max_end <= max_sf:
                    max_end = 0
                else:
                    max_end = 0
                    start+=1
                    stop+=1            
            
        if max_end > max_sf:
            max_sf = max_end
            if max_sf == lst[i]:
                stop = i
                start = i
            else: stop = i
    #     print "element: ", lst[i]
    #     print "start is", start
    #     print "stop is", stop
    #     print "max_end after", max_end
    #     print "max_sf is", max_sf
    #     print "_______________________"
    print("%d %d" %(start,stop))
 

if __name__=="__main__":
    #l = [13, -5, -13, 5, -1, 9, -13]
    #l = [6,-9,0,-9,9,-7,2]
    #l = [12, 14, 1, -2, -14, -3, -8]
    #l = [-5,-2,-1,-9]
    l=[1,2,3,4,5,-10]
    print(l)
    maxSubArraySum(l)

    # length = int(raw_input("ENTER NUM OF ITEMS: "))
    # l = list()
    # for i in range(0, length):
    #     l.append(random.randint(-15, 15))
    # print(l)
    # maxSubArraySum(l)