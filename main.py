# all testing list and dictoniary
Mylist = [1,2,5,6,88,88,2,2,98]
Mydict = {"allo":"Bakra","mura":"bhindi"}

def _mode(paramlist):
    # Min and max of paramlist
    Mylist_max = max(Mylist)
    Mylist_min = min(Mylist)

    Result = {}
    Result_list_proccess = []
    Min_value = 0
    Max_value = 0
    Value_of_current_num = 0

    # Try to count
    for i in paramlist:
        if (i == Mylist_min):
            Min_value = Min_value + 1
            Result.update({f"{Mylist_min}":f"{Min_value}"})

        elif (i == Mylist_max):
            Max_value = Max_value + 1
            Result.update({f"{Mylist_max}":f"{Max_value}"})
        
        else:
            # print(Result.keys())
            if i in Result_list_proccess:
                string_i = str(i)
                Result[string_i] = int(Result[string_i]) + 1
                # print(Result[i])
                # print("True")
            else:
                Value_of_current_num = 0
                Value_of_current_num = Value_of_current_num + 1
                Result.update({f"{i}":f"{Value_of_current_num}"})
                Result_list_proccess.append(i)
            # print(Value_of_current_num)

    print(Result)

    # Giving The Result
    # Result_procces = []

    # for num in Result.values():
    #     print(num)

    # max_val_of_result_procces = max(Result_procces)

    # for keys in Result:
    #     resultskeys = keys.find(max_val_of_result_procces)

    #     if resultskeys != -1:
    #         print(keys)

_mode(Mylist)


       
