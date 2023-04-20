def hello():
    print("Hello user, welcome to python!")
hello()

def pack(name, occopation, state):
    print(name + "," + occopation + "," + state)
pack("Lijalem", "backEnd", "CA")

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")
eat_lunch(["apple","banana","sandwich","cookie"])
