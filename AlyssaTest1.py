# NAME:         FIXME
# GUESS: WHAT ARE WE MAKING??? ______a square root checker_____________

# Example
def hello_world():
    return "Hello!"

def function_1(data):
    if (type(data)) == int:
      sqrt = data ** 0.5
      print("sqrt", sqrt)
      hasRemainder = sqrt % 1
      print(hasRemainder)
      return hasRemainder == 0
    return False

def main():
    print("Function 1: ", function_1(100))

main()
