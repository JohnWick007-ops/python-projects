print("this password generater has 1 lower 1 upper char and 1 digit and 1 sigh char(punctuation)")
import string
import random
all_char = string.ascii_letters + string.digits + string.punctuation
password = [  random.choice(string.ascii_lowercase),  
              random.choice(string.ascii_uppercase),
              random.choice(string.digits),  
              random.choice(string.punctuation)    ]
while True: 

    password.append(random.choice(all_char))
    if(len(password)== 12):
        break
    else:
        continue

main_password = "".join(password) ##password is list  
print(f"the generate password is {main_password}")