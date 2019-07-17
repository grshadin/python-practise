# def reverse_list(l):
#     l.reverse()
#     return l
#
# number=[1,2,3,4]
# print(reverse_list(number))

# def reverse_list(l):
#    return l[::-1]
#
#
# number=[1,2,3,4]
# print(reverse_list(number))


def reverse_list(l):
    r_list=[]
    for i in range(1,len(l)+1):
        pop_item=l.pop()
        r_list.append(pop_item)
    return r_list


number =[1,2,3,4]
print(reverse_list(number))