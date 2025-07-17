# NAME:         FIXME
# GUESS: WHAT ARE WE MAKING??? ___________________

# Example
def hello_world():
    return "Hello!"

def function_1(data):
    if (type(data)) == str:
      return False
    if data %2 == 1:
      return True
    if data %2 == 0 and data > 50:
      return True
    else:
      return False

def main():
    print("Function 1: ", function_1(100))

main()
