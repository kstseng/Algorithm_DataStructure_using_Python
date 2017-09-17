from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    ## initialize a quene
    simqueue = Queue()
    ## add item into the quene
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        ## extract front(right) and append to the end(left) for num times
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        ## remove the front
        simqueue.dequeue()

    ## return this element
    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
