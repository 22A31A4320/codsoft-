def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def mul(x,y):
  return x*y
def div(x,y):
  if y==0:
    return "Error!,Division not possible "
  else:
    return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
  a=input("Enter choice(1/2/3/4):")
  if a in ('1','2','3','4'):
    n1=float(input("Enter first number:"))
    n2=float(input("Enter second number:"))
    if a=='1':
      print("result:",add(n1,n2))
    elif a=='2':
      print("result:",sub(n1,n2))
    elif a=='3':
      print("result:",mul(n1,n2))
    elif a=='4':
      print("result:",div(n1,n2))
    b=input("Do you want to do another calculation(yes/no):")
    if b.lower()!="yes":
      break
  else:
    print("Invalid input")
