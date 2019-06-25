import requests
def course(url):
	res = requests.get(url)
	data = res.json()
	return data 
urlapi="http://saral.navgurukul.org/api/courses"
data= course(urlapi)
print "*****************************@@@@@@********************************"
print "\n@@@@@@@@@@@@@@@@@@@@@@ WELCOME TO SARAL COURSE @@@@@@@@@@@@@@@@@@\n"
print "****************************@@@@@@*********************************"


course_list = []
count = 0
while count < len(data["availableCourses"]):
    course_ex = data["availableCourses"][count]
    course_name = course_ex["name"]
    course_id = course_ex["id"]
    course_list.append(course_id)
    print (str(count)+" ",course_name, course_id)
    count = count +1     
user = input("enter your exercise")
user_id = course_list[user]
print (user_id)   
print ("*************************@@@choose your exercise@@@***********************")
api2= "http://saral.navgurukul.org/api/courses/"+str(user_id)+"/exercises"
exercise=course(api2)
sub_exercises = []
slug_list =[]
def exercise_func():
    count1 = 0
    while count1 < len(exercise["data"]):
        data_ex = exercise["data"][count1]
        all_exercise = data_ex["parentExerciseId"]
        child_ex = data_ex["childExercises"]
        exercise_id = data_ex["id"]
        sub_exercises.append(child_ex)
        if all_exercise != []:
            exercise_name = data_ex["name"]
            exercise_slug = data_ex["slug"]

            slug_list.append(exercise_slug)    
            print (str(count1) + "*", exercise_name )      
            
        count1= count1+1
exercise_func()
user1 = input("enter your lesson")
use_ex=slug_list[user1]
all_exercise = slug_list[user1]
print use_ex
api3= "http://saral.navgurukul.org/api/courses/"+str(user_id)+"/exercise/getBySlug?slug="+str(use_ex)
urly= "http://saral.navgurukul.org/api/courses/"+str(user_id)+"/exercise/getBySlug?slug="
print api3

content = course(api3)
content_name=content["content"]
print content_name
sub_name=[]
slug_list1=[]
def doughter_func():
    if all_exercise != None:
        if sub_exercises[user1] != []:
            count2 = 0
            while count2<len(sub_exercises[user1]):
                doughter_sub_ex = sub_exercises[user1][count2]
                sub_ex_name = doughter_sub_ex["name"]
                sub_name.append(sub_ex_name)
                sub_ex_slug = doughter_sub_ex["slug"]
                slug_list1.append(sub_ex_slug)
                print str(count2)+"%",sub_ex_name
                count2=count2+1

            user2 = input("enter your topics:-")
            sub_content = slug_list1[user2]
            urly4 = urly + str(sub_content)
            print urly4
            print_cont=course(urly4)
            cont_name =print_cont["content"]
            print cont_name

doughter_func()

