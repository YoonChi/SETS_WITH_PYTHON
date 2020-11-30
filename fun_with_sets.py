import copy 
import time 


def power_set(list1):

    # Base case 
    if len(list1) == 0:
        return [list1] # return [{}] 
    
    # pop off the far right element from list1 
    remove_item = list1.pop()

    # Recursive call 
    subsets = power_set(list1)

    # recursiveness is done. traversing back up now. 

    # make a copy of subsets each time the power_set function is called 
    list2 = copy.deepcopy(subsets)

    # add item that was removed from last function call into list2 
    list2.append([remove_item])
    
    # insert removed item into each subset that is in the 'subsets' list 
    # then combine 'subsets' list and list2 
    for sub in subsets:
        # cannot take sub(set) of an empty set 
        if sub:
            list2.append(sub+[remove_item]) 
            
    return list2


def k_subsets_naive(list1, k):
    list2 = []

    if k < 0 or k > len(list1):
        return []

    list2 = power_set(list1)
   
    k_list = []

    for sub in list2:
        # print(len(sub))
        if len(sub) == k: # add all 2-subsets of list into k_list 
            k_list.append(sub)

    return k_list


def k_subsets_better(list1, k):

    # Base case : return list within a list 
    if len(list1) == k:
        return [list1]
    
    # returns nothing if k is invalid integer  
    if k < 0 or k > len(list1): 
        return []

    # remove the right most element in the list
    remove_item = list1.pop()

    list2 = copy.deepcopy(list1)

    # Recursive call 1 : find all 1-subsets of list1 
    subset1 = k_subsets_better(list1, k - 1) 

    # insert the removed element back into each subset within the 'subsets' list 
    for sub in subset1: 
        sub.append(remove_item) 

    # Recursive call 2 : find all 2-subsets of list2 that don't contain x 
    subset2 = k_subsets_better(list2, k) 

    # combine the k-subsets from recursive call 1 & 2 to get final_list 
    final_list = subset1 + subset2

    return final_list 


if __name__ == "__main__":
    
    print("\nQuestion 1:")
    S = ["Piplup", "Torchic", "Rowlett"]
    print(power_set(S))

    print("\nQuestion 2:")
    S = [6, 7, 8]
    print(k_subsets_naive(S, 2))

    print("\nQuestion 3:")
    X = ["x", "y", "z"]
    print(k_subsets_better(X, 2))

    print("\nQuestion 4:" )
    k_sub_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    start_time = time.process_time()
    k_subsets_naive(k_sub_list, 2)
    end_time = time.process_time()

    print("k_subsets_naive elapsed time is ", end_time - start_time)

    start_time = time.process_time()
    k_subsets_better(k_sub_list, 2)
    end_time = time.process_time()

    print("k_subsets_better elapsed time is ", end_time - start_time)
  

