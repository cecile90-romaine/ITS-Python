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