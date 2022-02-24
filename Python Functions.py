"""def my_function():
    print("Hello from a function")

my_function()



def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")



def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil")



def my_function(fname, ):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")



def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")



name = 'Pascal.pedro'

print('I love ' + name)
print('I love {}'.format(name))
print(f'I love {name}')
print(''.join(('I love ', name)))
print('I love %s' %name)



def f():
    return "Hello World!"
print(f())



def f(name="World"):
    return "Hello, {}!".format(name)
print(f())
print(f("Python"))



def f(v, l= 'Python'):
    return "{}, {}!".format(v, l)
print(f("Hello"))
print(f('Bye', 'C/C++'))


def f(*args, con='&'):
    print(isinstance(args, tuple))
    print("Hello", con.join(args))

f("Python", "C", "C++", con="/")



def f(*args, **kargs):
    print('args', args)
    print('kargs', kargs)
    print('fp: {} & Scripts: {}'.format(kargs.get('fp'), '/'.join(args)))

f('Python', 'Javascript', ms = 'C++', fp = 'Haskell')



pairs = [(1,'one'), (2,'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pair: pair[1])
print(pairs)

pairs.sort(key = lambda pair: pair[0])
print(pairs)



def log(f):
    def wrapper():
        print("Hey log ~")
        f()
        print("Bye log~")
    return wrapper()
@log
def fa():
    print("This is fa!")

def fb():
    print("this is fb!")
fb = log(fb)

fa()
print("*" * 10)
fb()"""


def hello_func(name):
    return "Hello Function."


hello_func()
