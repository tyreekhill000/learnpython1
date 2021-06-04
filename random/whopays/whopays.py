import random
name = input("writed the names of the people that are going with a comma seperating them: ")
name_list = (name.split(",")) 
print(name_list)
name_len = (len(name_list))
random_num = random.randint(0,name_len - 1)
# print(random_num)
who = (name_list[random_num])
print("the person that will be paying the bill is " + who)
