import timeit
#programe em py uma funcao para fazer o somatorio de n valores. Um numero deve ser repassado como parametro. e a funcao deve realizar o somatorio onde 1 ate n.
#por exemplo se a entrada for 10, vai somar 1+2+3+4+5+6+7+8+9+10 e o resultado deve ser 55.
def somatorio(n):
    return (n*(n+1))/2

temp_start = timeit.default_timer()
somatorio(10)
temp_final = timeit.default_timer()
print("O somatório de 1 até 10 é: ", somatorio(10))
print("Tempo de execução: ", temp_final - temp_start)

#uma mao no codigo e a outra no terminal.