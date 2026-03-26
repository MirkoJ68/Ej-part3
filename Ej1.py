#1
personas = [{"nombre": "Juan", "edad": 17},{"nombre": "Papi", "edad": 18}]

print(f'Primer diccionario: {personas[0]}')
print(f'Nombre de la primera persona: {personas[0]["nombre"]}')
print(f'Edad de la segunda persona: {personas[1]["edad"]}')

#1.2
for persona in personas:
    for k, v in persona.items():
        print(k, ":", v)