b=raw_input("enter")
for i in range(0,8):
    print "hello ",i,b,"navgurukul"


i = raw_input("enter")
print "hii", i , "your no is this"
for i in range(0,9):
	print i



for i in range (1,200):
    number = i
    result = 0
while (number > 0):
    digit = number % 10
    result = result + (digit**3)
    number = number/10
    print number
print result
print digit
print number
if i==result:
    print i



dict2 = { "Name1": "shivani", "Age": 19, "User_Name": "chouhan"}
print (dict2["Name1"] , dict2["User_Name"])
dict1 = {"name" :"zeba", "age": 9}
print {dict1["name"], dict1["age"]}
if dict2["Name1"]==dict1["name"]:
    print "yes "
else:
    print "bye"