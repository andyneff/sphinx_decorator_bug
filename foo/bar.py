
# Pretend 3rd party library
import mocked_module

class SomeClass:
  ''' Some class '''
  def __init__(self):
    pass

@mocked_module.decorator2(SomeClass)
class MyClass:
  ''' This is a class '''
  pass

def foo():
  ''' Foo function '''
  pass