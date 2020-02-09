def sel_sort(arr, n):
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

if __name__ == '__main__':
    print(sel_sort([6,2,8,4,-4,1,0,10],8))
            