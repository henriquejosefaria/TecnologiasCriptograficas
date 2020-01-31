from random import randrange


def main():
    a = 0
    cond = True
    while(cond):
        g = raw_input("Do u want to encrypt(E) or decript(D)?: ")
        if "Ee".find(g) != -1:
            a = randrange(26)
            cesarEncipt(a)
        else:
            if "Dd".find(g) != -1:
                cesarDecript(a)
            else:
                if "escESC".find(g) != -1:
                    cond = False
                else: print("No such choice!!")
#----------------------------------------------------------------------
def cesarEncipt(a):
    mini = "abcdefghijklmnopkrstuwvxyz"
    mai = "ABCDEFGHIJKLMNOPQRSTUWVXYZ"
    num = "1234567890"

    print( "Deslocamento: " )
    print(a)
    g = raw_input("Type ur message to be encripted: ")

    for x in g:
        if x.isalpha():
            if x.isupper():
                c = mai.find(x)
                c = c + a
                while (c >= 26): 
                    c = c - 26
                print(mai[c])
            else:
                c = mini.find(x)
                c = c+a
                while c >= 26: 
                    c = c - 26
                print(mini[c])
        else:
            if x.isdigit():
                c = num.find(x)
                c = c+a
                while c >= 10: 
                    c = c - 10
                print(num[c])

#-----------------------------------------
def cesarDecript(a):
    mini = "abcdefghijklmnopkrstuwvxyz"
    mai = "ABCDEFGHIJKLMNOPQRSTUWVXYZ"
    num = "1234567890"
    print( "Deslocamento: " )
    print(a)
    g = raw_input("The decoded message to decript is: ")
    for x in g:
        if x.isalpha():
            if x.isupper():
                c = mai.find(x)
                c = c - a
                while c < 0:
                    c+=26
                print(mai[c])
            else:
                c = mini.find(x)
                c = c - a
                while c < 0:
                    c+=26
                print(mini[c])
        else:
            if x.isdigit():
                c = num.find(x)
                c = c-a
                while c < 0: 
                    c = c + 10
                print(num[c])


# inicio da execucao do programa
#-------------------------------------------
if __name__ == '__main__':
    main()

