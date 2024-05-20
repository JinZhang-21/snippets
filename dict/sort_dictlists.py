"""
Author: ZhangJin
Date: 2024-05-15 10:38:42
Email: jinzhang.hit@gmail.com
LastEditTime: 2024-05-15 10:38:43
FilePath: \snippets\dict\sort_dictlists.py
"""

friends =  [
  {"name": "John", "surname": "Doe", "age": 26},
  {"name": "Jane", "surname": "Doe", "age": 28},
  {"name": "Adam", "surname": "Smith", "age": 30},
  {"name": "Michael", "surname": "Jones", "age": 28}
]

print(
    sorted(
        friends,
        key=lambda friend:
            (friend["age"], friend["surname"], friend["name"])
    )
)

# PRINTS:
# [
#   {'name': 'John', 'surname': 'Doe', 'age': 26},
#   {'name': 'Jane', 'surname': 'Doe', 'age': 28},
#   {'name': 'Michael', 'surname': 'Jones', 'age': 28},
#   {'name': 'Adam', 'surname': 'Smith', 'age': 30}
# ]