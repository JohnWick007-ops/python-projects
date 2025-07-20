import socket
print("Let's scan the port :::")
que = input("taget is IP(press 1) or the target is domian name (press 2)")
if(que == "1"):
  target = input("enter the target IP :: ")
elif(que == "2"):  
 target =socket.gethostbyname(input("enter the domain name : "))
else:
  print("invalid input")

for i in range(1,101):
  try:
    s = socket.socket()
    s.connect((target,i))
    s.settimeout(0.5)
    print(f"the port {i} is open")
    s.close()
  except:
    print(f"the port {i} is close")