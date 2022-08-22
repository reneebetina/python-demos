people = [{"name": "Jane", "age": 20},
          {"name": "Barbie", "age": 20},
          {"name": "Jill", "age": 19},
          {"name": "Zoe", "age": 18},
          {"name": "Annie", "age": 16},
          {"name": "Jack", "age": 20},
          {"name": "Abby", "age": 23},
          ]

# by age
print("Sort by AGE ONLY: ")
print(sorted(people, key=lambda i: i['age']))

# by age
print("\nSort by NAME ONLY: ")
print(sorted(people, key=lambda i: i['name']))

# by both age and name.
print("\nSort by AGE then NAME: ")
print(sorted(people, key=lambda i: (i['age'], i['name'])))



#
#Sort by AGE ONLY: 
#[{'name': 'Annie', 'age': 16}, 
#{'name': 'Zoe', 'age': 18}, 
#{'name': 'Jill', 'age': 19}, 
#{'name': 'Jane', 'age': 20}, 
#{'name': 'Barbie', 'age': 20}, 
#{'name': 'Jack', 'age': 20}, 
#{'name': 'Abby', 'age': 23}]

#Sort by NAME ONLY: 
#[{'name': 'Abby', 'age': 23}, 
#{'name': 'Annie', 'age': 16},
#{'name': 'Barbie', 'age': 20}, 
#{'name': 'Jack', 'age': 20}, 
#{'name': 'Jane', 'age': 20}, 
#{'name': 'Jill', 'age': 19}, 
#{'name': 'Zoe', 'age': 18}]

#Sort by AGE then NAME: 
#[{'name': 'Annie', 'age': 16}, 
#{'name': 'Zoe', 'age': 18}, 
#{'name': 'Jill', 'age': 19}, 
#{'name': 'Barbie', 'age': 20}, 
#{'name': 'Jack', 'age': 20}, 
#{'name': 'Jane', 'age': 20}, 
#{'name': 'Abby', 'age': 23}]
