import sys

file = open("snoozed.txt", "a+")

def snooze():
  if len(sys.argv) != 4:
    print("Error: expected three arguments")
    return
  try:
    int(sys.argv[2])
  except ValueError:
    print("Error: expected integer argument")
    return
  file.write(sys.argv[2] + "\n")
  file.write(sys.argv[3] + "\n")

def check():
  toCheck = []
  file.seek(0)
  while True:
    line1 = file.readline()
    if line1 == "":
      break
    line2 = file.readline()
    lst = [line1.rstrip(), line2.rstrip()]
    toCheck.append(lst)
  for lst in toCheck:
    try:
      num = int(lst[0])
    except ValueError:
      toCheck.remove(lst)
    if num == 1:
      print(lst[1])
      toCheck.remove(lst)
    else:
      lst[0] = str(num - 1)
  file.seek(0)
  file.truncate()
  for lst in toCheck:
    file.write(lst[0] + "\n")
    file.write(lst[1] + "\n")

if sys.argv[1] == "snooze":
  snooze()
elif sys.argv[1] == "check":
  check()
print("finished.")
