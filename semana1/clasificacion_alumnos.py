def clasificar_alumno(promedio):
    if promedio >= 90:
        return "Excelente"
    elif promedio >= 70:
        return "Aprobado"
    else:
        return "Reprobado"
    
def resumen_alumno(nombre, materia, promedio):
     
     estado = clasificar_alumno(promedio)
     
     return f"Alumno: {nombre} | Materia: {materia} | Promedio: {promedio} | Estado: {estado}"
 
alumnos = [
     {"nombre": "María", "materia": "Español", "promedio": 95},
     {"nombre": "Luis", "materia": "Historia", "promedio": 75},
     {"nombre": "Maricruz", "materia": "Inglés", "promedio": 100},
     {"nombre": "Diego", "materia": "Programación", "promedio": 50},
     {"nombre": "Ángel", "materia": "Física", "promedio": 80},
 ]

for alumno in alumnos:
    print(resumen_alumno(alumno["nombre"], alumno["materia"], alumno["promedio"]))