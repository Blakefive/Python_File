Nlist1 = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y','Z']
odd = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-",
       "L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-",
       "W":".--","X":"-..-","Y":"-.--","Z":"--.."}
Ndic = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G',
        '....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N',
        '---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U',
        '...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','':''}
def start():
    N = input()
    Nstr = ""
    for i in range(len(N)):
        try:
            Nstr += odd[Nlist1[Nlist1.index(N[i])-13]] + " "
        except ValueError:
            Nstr += odd[Nlist1[Nlist1.index(N[i].upper())-13]] + " "
    print(Nstr)
    
def end(Nstr):
    Nlist2 = Nstr.split()
    Nmain = ""
    for i in range(len(Nlist2)):
        check = Nlist1.index(Ndic[Nlist2[i]])
        if check+13 < len(Nlist1):
            Nmain += Nlist1[check+13]
        else:
            Nmain += Nlist1[(check+13) - len(Nlist1)]
    print(Nmain)
