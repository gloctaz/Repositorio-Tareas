#for i in range(1,6):
#    for j in range(i):
#        print("*", end="\t")
#    print ()
#for i in range(6,1,-1):
#   for j in range(i):
#        print("*", end="\t")
#   print ()


for k in range(1,6):
    for l in range(6-k):
        print(" ", end=" ")
    for m in range(2*k-1):
      print("*", end=" ")
    print()

for k in range(4,0,-1):
    for l in range(6-k):
        print(" ", end=" ")
    for m in range(2*k-1):
      print("*", end=" ")
    print()