

x = (1,2,"hello",5,7) # tuple # immutable

print(x);
print(x[1])
#x[1]=5;
print(x[1])


set_type = {"hii","gii","65","65"} # set # immutable # unordered #unique
set_type1 = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
print("length is ",len(set_type))
print("length is ", len(set_type1))

for i in set_type:
    print(i);

#sequencee data types -> ordered
#string
#list
#touple

#unordered
#set
#dict

list_type = [1,"jina"]
print(list_type[0])
list_type[0]="Pallavi loves"
print(list_type[0],list_type[1])

#dict
dict_type = {"pallavi":"topper",
             "jina":"10th fail",
              "both": "gabagandu",
              "pallavi":"good student",
               "jina":"bad student" }

#mutuable #unordered 
#dict_type["jina"]="10th topper"
print(dict_type["jina"])
print(len(dict_type))


