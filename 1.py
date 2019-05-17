def three_minimum_in_list (list, min=[]):
    if len(list)<3:
        print("В массиве недостаточно элементов!")
    else:
        for i in range (0,3):
            min.append(list[i])
        else:
            if len(list)==3:
                print(*min)
            else:
                for i in range (3, len(list)):
                    if list[i]<max(min):
                        min.pop(min.index(max(min)))
                        min.append(list[i])
                else:
                    print(*min)