def format_name(fname,lname):
    return_fname=fname.title()   #title first letter capital
    return_lname=lname.title()
    #print(f"{fname,lname}")
    return f"{fname},{lname}"
    print()
format_name("Harry","Ron")    #what are scales
#######################################
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

print(function_2(function_1("Harry")))
###################################################

def function_3(firstname,lastname):
    if firstname == "" and lastname == "":
        return ("Enter valid name")
    f_name=firstname.title()
    l_name=lastname.title()
    return f"{f_name} {l_name}"

print(function_3(input("Enter first name: "),input("Enter last name: ")))

###########################################################################