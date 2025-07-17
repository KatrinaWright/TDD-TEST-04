import AlyssaTest1 as A1;

# Example Passing Test
def test_hello_pass():
    assert A1.hello_world() == "Hello!"

# Example Failed Test
# Uncomment, run once & then comment out again
#def test_hello_fail():
#    assert hello.hello_world() == "Hello World!"

#########################
#  HW Assignment Tests  #
#########################

# Problem 1 Tests
def test_function_one():
    assert A1.function_1( 1 ) == True
