def show_how_it_works(func):
    def my_function(*args,**kwargs):
        print('Running function:',func.__name__)
        print('Positional arguments:',args)
        print('Keyword arguments:',kwargs)
        result = func(*args,**kwargs)
        print('Result:',result)
        return result
    return my_function

#@show_how_it_works
def add_two_numbers(a,b):
    return a + b
#print(add_two_numbers(1,8))
decolated_func = show_how_it_works(add_two_numbers)
#print(decolated_func(1,8))
if __name__ == '__main__':
    decolated_func(1,8)

