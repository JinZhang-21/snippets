str_val = 'apples'

print(f'{str_val!r}') # 'apples'
print(f'{str_val}') # apples

# number formatting
price_val = 6.23141241
print(f'{price_val:.2f}') # 6.23

# date formatting
from datetime import datetime
date_val = datetime.now()
print(f'{date_val:%Y-%m-%d}') # 