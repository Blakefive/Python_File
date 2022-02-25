def factorial(N):       
    final = 1
    for i in range(1,N+1):  #1부터 N까지 loop을 시킨다.
        final *= i          #loop시키면서 각각의 값들을 final변수에 넣는다.
    return final        
