exec(open("logit_gate.py").read())

print("AndGate test---")
g1 = AndGate("G1")
print(g1.getOutput())


print("OrGate test---")
g2 = OrGate("G2")
print(g2.getOutput())

print("NotGate test---")
g3 = NotGate("G3")
print(g3.getOutput())

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)
