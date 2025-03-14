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