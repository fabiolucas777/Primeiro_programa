#!/home/fabio/PycharmProjects/Myproject/venv/bin/python3
#calculo da area do trapezio
print(
    '\n\nBem vindo a calculadora'
    ' de trapezio\n\nIMPORTANTE: NO'
    ' LUGAR DE "," USE "."\n\n\n'
)
bme = float(
    input(
        'Valor da base menor: '
    )
)
bma = float(
    input(
        'Valor da base maior: '
    )
)
alt = float (
    input(
        'Valor da altura: '
    )
)
soma = (alt*(bma+bme))/2
print(
    '\nO valor da area do trapezio é \na altura ({}) vezes a base maior'
    ' mais a base menor ({} + {}) \n é igual há {}'.format(alt, bma, bme, soma)
)
input(
    '\nPressione "enter" para sair.'
)
