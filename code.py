if __name__ == '__main__':
    n = int(input()) #input n
    arr = map(int, input().split()) #list in put
    arr = list(set(list(arr))) #convert the input to list 
    arr_arngment = sorted(list(arr)) #sort the list 
    ar = len(arr) #get the length 
    print(arr_arngment[ar-2])#print thr runner up 
