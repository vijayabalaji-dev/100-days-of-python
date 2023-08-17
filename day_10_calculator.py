from replit import clear
""" docstrings in python used as comment and it can be used to give description about the function while will be displayed by the editor 
********************************************************
parameter vs argument
parameter => data variables def data(a => parameter, b => parameter)
argument => the actual value passed to the argument data(3 => argument, 5 => argument)
"""
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a,b):
  """ adds two numbers """
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}
def suceesor(num1,num2,op):
  function = operations[op]
  return function(num1,num2)

exiter = False
previous = 0
while not exiter:
  num1 = 0
  num2 = 0
  
  if previous == 0:
    print(logo)
    num1 = int(input("Enter the first number: "))
    for symbol in operations:
      print(symbol)
  else:
    num1 = previous
  op_choosed = input("Select any one one above operation: ")
  num2 = int(input("Enter the next number: "))
  result = suceesor(num1,num2,op_choosed)
  print(f"{num1} {op_choosed} {num2} = {result}")
  con = input("do you want to continue with previous calculation? type 'y' or to start a new operation type 's' or to end type 'n': ")
  if con == "y":
    previous = result
    continue
  elif con == "s":
    clear()
    previous = 0
  else:
    exiter = True
  
    
