def tower(n,fpole,spole,tpole):
    if (n>0):
        tower(n-1,fpole,tpole,spole)
        print("Moving",fpole,"to",spole)
        tower(n-1,tpole,spole,fpole)


tower(3,'A','B','C')


