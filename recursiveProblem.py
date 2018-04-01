def max(list):
    ## Check if the list has only one number
    if len(list) == 1:
        return list[0] ## return the first in the list
    
    else:
        m = max(list[1:]) ##Recursive function to get the rest of the list except the first one in the list
        
        
        if m >list[0]: ## if list is has more then one in the list
            return m
        else:
            list[0]
            

def min(list):
    
    if len(list) == 1:
        return list[0]
    
    else: ## get the min value
        n = min(list[1:])
  
        return n if n < list[0] else list[0]
    

def reverse(list):
    ## if nothing is in list 
    if not list: 
        return list
    return list[-1:] + reverse(list[:-1]) ##reverse

        
            
            
def main():
        
    ## sequence list    
    list = [1,2,3,4,5,6,7]
    
    print ("The sequence is:", list)
    print("The max number: ", max(list))
    print("The min number: ", min(list))
    print ("The reverse of this sequence is", reverse(list))


main()



    