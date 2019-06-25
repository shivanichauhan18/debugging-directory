num = 10
zero_list = [ i*0 for i in range(num)]
print(zero_list)


num = 9876542345
string_wali_num =  str(num)
ek_nayi_list = [int(i) for i in string_wali_num]
print(ek_nayi_list)  



# def word_count(str):
#   new_list = [i for i in str if i != ' ']
#   print new_list
#   sum = 0
#   [(sum+=1) for i in new_list]
#   return sum
# print(word_count("""the quick brown fox jumps over the lazy dog."""))
