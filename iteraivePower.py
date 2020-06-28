## iterative
def iterPower(base,exp):
    y=1
    while exp > 0:
          y= base*y
          exp -= 1
    return y