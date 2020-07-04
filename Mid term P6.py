def flatten(aList):
   t = []
   for i in aList:
      if not isinstance(i, list):
         t.append(i)
      else:
         t.extend(flatten(i))
   return t








