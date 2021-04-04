from art import logo

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  answer = float(input("What's the first number? "))
  operation_symbol = "U"

  while operation_symbol != "=":
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the list abobe,\nOr type '=' to calculate end result and start over,\nOr type anything else to exit: ")
    if operation_symbol in operations:
      num = float(input("What's the number? "))
      calculation = operations[operation_symbol]
      answer_new = calculation(answer, num)
      print(f"{answer} {operation_symbol} {num} = {answer_new}")
      answer = answer_new
    elif operation_symbol == "=":
      print(f"Final answer of all calculations is {answer}")
      calculator()
    else:
      print(f"Final answer of all calculations is {answer}")
      operation_symbol = "="

calculator()
