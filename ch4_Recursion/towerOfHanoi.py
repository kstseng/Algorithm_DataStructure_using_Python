def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("moving disk from {} to {}".format(fp, tp))

moveTower(3, "A", "B", "C")

'''
moveTower(2, "A", "B", "C")
    moveTower(1, "A", "C", "B")
        moveTower(0, "A", "B", "C") -> ''
        A -> C
        moveTower(0, "B", "C", "A") -> ''
    A -> B 
    moveTower(1, "C", "B", "A")
        moveTower(0, "C", "A", "B") -> ''
        C -> B 
        moveTower(0, "A", "A", "C") -> ''
'''


