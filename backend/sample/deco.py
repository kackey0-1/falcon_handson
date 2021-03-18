
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print('Whee!')


if __name__ == '__main__':
    say_whee()
    # The so-called decoration happens at the following line:
    say_whee = my_decorator(say_whee)
    say_whee()
