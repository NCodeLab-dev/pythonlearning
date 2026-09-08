

#reverse in python

list_num = [1,2,3,4,5]

print(list_num[::-1]) # is not a generic way


employee = {"emp_name": "Narayan",
            "emp_id": 12345,
            "emp_age": 30,
            "emp_gender": "male"}

for x in reversed(employee):
    print(x,employee[x])


#while loops -> looping over a condition

count = 1;
name = "pallavi"

while count<=5:
    print(name)
    count+=1