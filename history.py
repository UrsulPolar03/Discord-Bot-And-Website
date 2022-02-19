
history = []

def showh():
  return history

def addh(x):
  if len(history) <= 10:
    history.append(x)
  elif len(history) >10:
    history.pop(0)
    history.append(x)