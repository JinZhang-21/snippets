a = { 'max': 200 }
b = { 'min': 100, 'max': 250 }
c = { 'min': 50 }

a['min'] + b['min'] + c['min'] # throws KeyError
a.get('min', 0) + b.get('min', 0) + c.get('min', 0) # 150

# *get 提供了一个默认值，如果键不存在的话