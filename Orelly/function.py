
#function
"""
def function(args):
    #body
    print(args)
    #body
    return args 
function("hello world")
"""

"""
def ask(message):
    #body return the message by asking

    # if message is not a string thorugh error
    if type(message) != str:
        print("please enter a string")
        return

    return message + " ?"

message = "python is good"


new_message = ask(5)
print(new_message)
"""


def print_expiary_date(day,month,year="2028"):
    print("expiary date is:\n" +
    "day:   "+day+"\n"+
    "month: "+month +"\n"+
    "year:  "+year)

print_expiary_date("01","Jan",year="2030")

#print_expiary_date("")


