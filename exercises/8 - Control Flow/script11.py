a = [1,2,3,4]
a_sqrt = [item*item for item in a]
print(a_sqrt)
a_sqrt_more_than_2_or_equal = [item*item for item in a if item >= 2]
print(a_sqrt_more_than_2_or_equal)
a_sqrt_dic = {item:item*item for item in a}
print(a_sqrt_dic)