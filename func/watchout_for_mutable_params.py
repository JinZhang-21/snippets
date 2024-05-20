# *这里我们想要说明, python中默认参数若为可变类型可能会导致不同调用时的参数共享问题
def append(n, l = []):
  l.append(n)
  return l

append(0) # [0]
append(1) # [0, 1]

# *如果使用可变对象作为默认值是必须的, 那么推荐使用None
def append(n, l = None):
  if l is None:
    l = []
  l.append(n)
  return l

append(0) # [0]
append(1) # [1]