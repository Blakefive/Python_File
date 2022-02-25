from googletrans import Translator

translator = Translator()
f = open("test.txt", 'r')
Nlist = []
Nstr = ""
while True:
    line = f.readline()
    if not line: break
    Nlist.append(line)
for i in Nlist:
    Nstr += i
Ncheck = Nstr.split("\n")
Ncheckfinal = []
for i in Ncheck:
    if i != "":
        Ncheckfinal.append(i)
finallist = []
another  = []
test = ""
hh = 0
for i in range(len(Ncheckfinal)):
    if Ncheckfinal[i] == '/*':
        hh = 1
    if Ncheckfinal[i] == "*/":
        hh = 0
    if hh == 0:
        for j in range(len(Ncheckfinal[i])-1):
            if Ncheckfinal[i][j] + Ncheckfinal[i][j+1] == '//':
                finallist.append(Ncheckfinal[i][j+2:])
    elif hh == 1 and Ncheckfinal[i] != '/*' and Ncheckfinal[i] != "*/":
        finallist.append(Ncheckfinal[i])
final =[]
for i in finallist:
    result = translator.translate(i, dest="ko")
    final.append(result.text)
print(final)
f.close()
