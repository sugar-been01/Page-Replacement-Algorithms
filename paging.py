from queue import Queue
from random import randrange
from weakref import ref
import sys

def generate(lngth):#given the left of reference string this method generates the reference string
    arr=[]
    for i in range(lngth):
        arr.append(randrange(0,10))
    return arr



def LRU(size,pages):
    #the frames list represents the pages currently in main memory ordered based on when last the page was reference,
    #the last element being the most recently referenced  page
    #pages represents the pages that will be referenced 
    frames=[] 
    faults=0
    hits=0
    for i in pages:
        if (len(frames)<size and i not in frames): 
            #when memory is not full and the page being referenced is not in memory ,
            #the page is just placed in memory without need for any replacement 
            frames.append(i)
            faults+=1
        elif i in frames: 
            #when a page being referenced is in memory ,
            #the page is moved to the end of the array to indicate that it was recently referenced  
            hits+=1
            frames.remove(i)
            frames.append(i)
        else:
            #when main memory is full i.e the frames list and the page being referenced is not in memoy ,a page fault occurs
            #and the first element in the frames list is removed since it indicates that it is the least referenced 
            faults+=1
            frames.remove(frames[0])
            frames.append(i)
    return faults


def FIFO(size,pages):
    #the frames list represents the pages currently in main memory in an unorder manner
    #the count variable helps us keep track of the page that was loaded first i.e the page that should be replaced in the event of a page fault
    count=0 
    frames=[]
    hits=0
    faults=0
    for i in pages:
        if len(frames)<size and i not in frames: 
            #when memory is not full and the page being referenced is not in memory ,
            #the page is just placed in memory without need for any replacement
            frames.append(i)
            faults+=1
        elif i in frames:
            #increment the hits variable when the page being referenced is in memory
            hits+=1
        else:
            #when main memory is full i.e the frames list, and the page being referenced is not in memoy,
            #the page that was first loaded into memory is found and replaced  
            frames[count]=i
            faults+=1
            if count+1>=size:
                count=0
            else:
                count+=1
    return faults
def OPT(size,pages):
    frames=[]
    faults=0
    hits=0
    counter=0
    for i in pages:
        if len(frames)<size and i not in frames: 
            #when memory is not full and the page being referenced is not in memory ,
            #the page is just placed in memory without need for any replacement 
            frames.append(i)
            faults+=1
        elif i in frames:
            #increment the hits variable when the page being referenced is in memory
            hits+=1
        else:
            faults+=1
            toBe=pages[counter:]#pages to be referenced in futer
            max=0
            rvm=0
            for j in frames:
                if j not in toBe:
                    #removes the page if won't be referenced in the future
                    rvm=j
                    break
                else: 
                    #checks which page will be referenced later in time by using their index and removes it
                    if toBe.index(j)>max:
                        max=toBe.index(j)
                        rvm=j
            frames.remove(rvm)
            frames.append(i)
        counter+=1
    return faults


def main():
    
    size = int(sys.argv[1])
    pageLenght=int(input("Enter string length: "))
    pages=generate(pageLenght)
    print(pages)
    print ('FIFO',FIFO(size,pages),'page faults.')
    print('LRU', LRU(size,pages), 'page faults.')
    print('OPT', OPT(size,pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of pages]')
    else:
     main()
