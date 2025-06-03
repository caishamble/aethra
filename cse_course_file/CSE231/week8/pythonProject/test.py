def floats(a_list):
  new_list = []
  for element in a_list:
    if isinstance(element,float):
      new_list.append(element)
  return new_list

a_list = ['abc','2','x.y','2.34','2.5e2','hello','0.2','.5','bye']
print(floats(a_list))