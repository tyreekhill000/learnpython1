def format_name(first, last):
  if(first == "" or last ==""):
    return "first or last name cannot be empty"
  firstname = first.title()
  lastname = last.title()
  formatedname = firstname + lastname
  return formatedname
  


f_name=input("What is the firstname?\n")
l_name=input("What is the lastname?\n")






print(format_name(f_name,l_name))
