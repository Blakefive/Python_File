(lambda x: print(f'{int(x//3600)} : {int((x%3600)//60)} : {int(x%60)}'))(float(input())/100*42195)
