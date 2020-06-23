def sorting(assignments):
    assignments = sorted(assignments)
    assignments = (assignments[1],assignments[2])
    return assignments

####################################only edit these variables
asn1 = 91
asn2 = 94
asn3 = 99
M = 59
F = 100
####################################
Wasn = WF = 0.15
WM = 0.55
G = (sorting([asn1,asn2,asn3]),M,F)
#print(G)
AvgWF = Wasn*G[0][0] + Wasn*G[0][1] + WM*G[1] + WF*G[2]
print("Average with final: " + str(AvgWF))
Wasn = Wasn + WF/4 #distribute the weight evenly between the other assessments
WM = WM + WF/2
AvgNF = Wasn*G[0][0] + Wasn*G[0][1] + WM*G[1]
print("Average without final: " + str(AvgNF))
Grade = sorted([AvgNF,AvgWF])
Grade = Grade[1]
print("Final Grade: " + str(Grade))
