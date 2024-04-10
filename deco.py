# 09-04-2024
#def simple_function():
    # Want to do more stuff!
    # Do simple stuff return something

# @some_decorator
#def simple_func():
    # Do simple stuff
    #return somthing

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")

hello()