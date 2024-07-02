"""
2.3.5. Ejercicio 1
El centro de psicología del estudiante ubicado en la ciudad de Puerto
Montt, con más de 20 años de experiencia en el área, desea generar una
serie de encuestas que permitan describir el nivel de desarrollo de los
alumnos, para que de esta forma puedan tomar medidas especiales según
los resultados obtenidos.
El test consta de 12 preguntas, cada una de las cuales posee un punto.
Se desea crear 4 categorías:
· Usted es un alumno de buen desempeño (0 a 3 ptos)
· Usted es un alumno que puede mejorar (4 a 6 ptos)
· Usted es un alumno con algunos desafíos (7 a 9 ptos)
· Usted alumno con muchos desafíos (sobre 10 ptos)
"""
#Diccionario con preguntas
pregunta = {
            1:  "¿Sientes que prestas suficiente atención durante las clases?",
            2:  "¿Completas tus tareas escolares a tiempo la mayoría de las veces?",
            3:  "¿Te consideras capaz de concentrarte en tus estudios cuando es necesario?",
            4:  "¿Eres organizado en tu trabajo académico?",
            5:  "¿Participas activamente en clase?",
            6:  "¿Te sientes motivado para alcanzar tus metas académicas?",
            7:  "¿Crees que puedes resolver problemas difíciles?",
            8:  "¿Dedicas tiempo suficiente al estudio fuera del horario de clases?",
            9:  "¿Te llevas bien con tus compañeros de clase?",
            10: "¿Puedes manejar el estrés durante los exámenes?",
            11: "¿Sueles solicitar ayuda a tus profesores cuando tienes dificultades?",
            12: "¿Estás satisfecho con tu desempeño académico hasta ahora?"
            }
puntaje = 0
#Bucle para obtener respuestas
for pregunta_actual in range(1,len(pregunta)+1):
    while True:
        print(f"Pregunta {pregunta_actual}:{pregunta[pregunta_actual]}\nPuede Responder - 's' o 'n'")
        respuesta = input("Su respuesta: ").lower()
        if respuesta == "s":
            break
        elif respuesta == "n":
            puntaje += 1
            break
        print("Respuesta incorrecta")
print("Puntaje:",puntaje)
#Escalas de puntaje
if (puntaje<=3):
    print("Usted es un alumno de buen desempeño")
elif(puntaje>3 and puntaje<=6):
    print("Usted es un alumno que puede mejorar")
elif(puntaje>6 and puntaje<=9):
    print("Usted es un alumno con algunos desafíos")
else:
    print("Usted alumno con muchos desafíos")