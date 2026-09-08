
# dictionary in python
# non-sequence
# mutuable

# define a dictionary

employee = {"emp_name": "Narayan",
            "emp_id": 12345,
            "emp_age": 30,
            "emp_gender": "male"}
employee["emp_age"]=31 # updating a dictionary
print(employee["emp_age"])

print("emp_salary" in employee) #salary not yet added
#adding a new item to a dictionary
employee["emp_salary"] = 100000.00

print(employee)

#finding an item exist or not in a dictionary
print("emp_name" in employee)


def printDict(dict):
    for x in dict:
        print(x,dict[x])

printDict(employee)


#deleting an item from a dictionary

del employee["emp_age"];
print(employee)

#another efficient way is to use pop method

deleted_value = employee.pop("emp_salary")
print(employee)
print(type(deleted_value))
