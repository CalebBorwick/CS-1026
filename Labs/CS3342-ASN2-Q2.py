def A(I, P):
    def B():
        #print(I, P, B)
        print(I)
    if I > 3:
        P()
    elif I > 2:
        A(4, B)
    elif I > 1:
        A(3, B)
    else:
     A(2, B)
def C():
    pass
A(1, C)

# def A(I, P):
#     def B():
#         print(I)
#     print(I, P, B)
#     if I > 3:
#         P()
#     elif I > 2:
#         A(4, P)
#     elif I > 1:
#         A(3, P)
#     else:
#         A(2, B)
# def C():
#     pass
# A(1, C)
