def evaluar_posfija(expresion):
    pila = []
    
    for token in expresion.split():
        if token.isdigit():
            pila.append(int(token))
        else: 
            operando2 = pila.pop()
            operando1 = pila.pop()
            
            if token == '+':
                pila.append(operando1 + operando2)
            elif token == '-':
                pila.append(operando1 - operando2)
            elif token == '*':
                pila.append(operando1 * operando2)
            elif token == '/':
                pila.append(operando1 / operando2)
                
    return pila[0]

expresion = "3 4 + 2 * 7 /"
resultado = evaluar_posfija(expresion)
print(f"Resultado de la expresión posfija '{expresion}': {resultado}")
