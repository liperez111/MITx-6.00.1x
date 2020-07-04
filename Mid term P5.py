def keysWithValue(aDict, target):
   '''
  aDict: a dictionary
  target: an integer
  '''
   # Your code here


   keys = []
   for i in aDict:
      if aDict[i] == target:
         keys.append(i)
   return sorted(keys)