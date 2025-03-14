'''print("Hello world") # text
#esercizio2_3 personal message
name:str = "cecile" 
print(f"Hello {name} how are you? would you like to learn some python today?")

# esrcizio2_4 name cases:
name:str = "cecile"
print(f"Lower:{name.lower()}")
print(f"Upper: {name.upper()}")
print(f"Title:{name.title()} ")

print(name.lower())
print(name.upper())
print(name.title())

# esercizio2_5 famous quote

frase:str = "chi lavora la dura"
print(f'cecile once said:"{frase} "')

#esercizio2_6 famous quote#2

famous_person:str = "cecile"
message:str = "chi lavora la dura"
print("cecile once said:\{frase}\"")


#esercizio3_1 names

name_list = ["aliya", "achille","bianca", "ginevra"] 
print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list[3])

for name in name_list:
    print(name)

   #esercizio3_2 Greetings

name_list =["aliya", "achille", "bianca", "ginevra"] 
message:str = "Buongiorno a tutti"

for name in name_list:
    print(f"{message}, {name}")

   #esercizio3_3Your own list


car:list = ["BMV", "TESLA", "OPEL", "FIAT"] 
print(f"I own a {car[0]} car. ") 
'''

#esercizio3_4 Guest list

# we use the last list\line 41 in exo3_2

invited:list = ["aliya", "achille", "bianca", "ginevra"]
message:str =  "I like to invited you to dinner saturday "
print("invited")
print(f"{invited[0]}, you receive one invitation{message} ")
print(f"{invited[1]},  you receive one invitation{message} ")
print(f"{invited[2]},  you receive one invitation{message} ")
print(f"{invited[3]},  you receive one invitation{message} ")

print(f"sorry,{invited[0]}, guest can not  come.")

#esercizio3_5 Changing Guest list


invited:list = ["aliya", "achille", "bianca", "ginevra"]
message:str =  "I like to invited you to dinner saturday "

print(f"sorry,{invited[0]}, guest can not  come.")

#invited.insert(0, "elena")

invited[0] = "elena" 

print("invited")
print(f"{invited[0]}, you receive one invitation{message} ")
print(f"{invited[1]},  you receive one invitation{message} ")
print(f"{invited[2]},  you receive one invitation{message} ")
print(f"{invited[3]},  you receive one invitation{message} ")


#esercizio3_6 More Guests
# we start with exercise3_4 or3_5



invited:list = ["elena", "achille", "bianca", "ginevra"]

message:str =  "I like to invited you to dinner saturday "

for i in invited:
    print(f"information,{i} i found the bigger table because i am invited other tree person")
invited.insert(0, "luna")
invited.insert(3, "sole")
invited.append("stela")
# print a new set of invitation

print(f"{invited},{message} ")
print("n\invited to dinner:\n")

for i_agg in invited:
    print(f"{i_agg}, you are receive one invitation {message} ")

   # esercizio3_7 shrinking guest list
  #start with ex3_6
invited.pop(0)  


 
















