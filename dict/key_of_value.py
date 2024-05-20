def find_key(dict, val):
    # ! next() returns the next item from the iterator
  return next(key for key, value in dict.items() if value == val)

ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
  'Isa': 11,
}
iter = find_key(ages, 11)
print(iter) # Isabel
print(iter) # 为什么还是 Isabel ？ 