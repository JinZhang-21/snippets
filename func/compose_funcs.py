from functools import reduce
# functools.reduce() 执行从左到右的函数组合。
# 最左边的）函数可以接受一个或多个参数;其余函数必须是一元的。

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)

def compose_left(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)

add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9