from view.view_nilai import nyari,cetak
from view.input_nilai import inputan,edit,delete
while True:
    print("PROGRAM INPUT NILAI")
    c = input("A)dd, E)dit, D)elete, S)earch, L)ist, Q)uit: ")
    if c.lower()=='q':
        print("Terima Kasih")
    elif c.lower()=='l':
        cetak()
    elif c.lower()=='s':
        nyari()
    elif c.lower()=='d':
        delete()
    elif c.lower()=='e':
        edit()
    elif c.lower()=='a':
        inputan()
    else:
        print("Terima kasih")