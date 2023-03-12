l_min, l_max = 0, 99

a =  int(input(f"pls insert nomor between {l_max} and {l_min} to guessss: "))

if a < l_min or a > l_max:
  exit(1)

#long - лист значений от 1 до 100 (list)
def gener(l_min, l_max, deep=0):
  #lst = long
  deep+=1
  if deep > 10:
    print("Stop Iter")
    return

  w_min, w_max = l_min, l_max

  print(f"you number > {w_min} ?")
  answer = input("Answer: ")
  if answer == "1":
    w_min += (w_max - w_min)//2
  else:
    w_max_tmp = w_max
    w_max = w_min
    w_min -= (w_max_tmp - w_min)//2
  if(w_max - w_min < 2):
    print(f"Number: {w_max} {w_min}")
    return
  else:
    gener(w_min, w_max, deep)

gener(l_min, l_max)


