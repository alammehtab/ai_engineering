# problem
# Write a program to fill in a letter template given below with name and date. letter = ''' Dear <|Name|>, You are selected! <|Date|> '''

# solution
letter = """ Dear <|Name|>, 
            You are selected! 
            <|Date|> """

user_name = "Mehtab"
date = "5/2/2025"

final_result = letter.replace("<|Name|>", user_name).replace("<|Date|>", date)

print(final_result)
