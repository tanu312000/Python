def tower(n,fpole,spole,tpole):#Three poles of Hanoi
    if (n>0):
        #n is No of Discs
        tower(n-1,fpole,tpole,spole)
        print("Moving",fpole,"to",spole)
        tower(n-1,tpole,spole,fpole)


 #tower(3,'A','B','C')


