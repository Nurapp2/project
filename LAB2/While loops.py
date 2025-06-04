#While loops1
i = 1
while i < 6:
  print(i)
  i += 1

#While loops2
i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#While loops3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#While loops4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
