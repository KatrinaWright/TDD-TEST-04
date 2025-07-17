import EricCTest1 as E1;

# Example Passing Test
def test_hello_pass():
    assert hello.hello_world() == "Hello!"

# Example Failed Test
# Uncomment, run once & then comment out again
#def test_hello_fail():
#    assert hello.hello_world() == "Hello World!"

#########################
#  HW Assignment Tests  #
#########################

# Problem 1 Tests
def test_function_one():
    assert E1.function_1( 1 ) == True
