
Algoritmo sin_titulo
	
	Escribir "Ingrese la cantidad de materias"
	Leer contador
	materias<-contador
	Mientras contador > 0 Hacer
		contador<-contador - 1 
		Escribir "Ingrese las calificaciones de cada materia"
		Leer notax
		notas<- notas + notax
		Si contador <= 0
			Escribir "Su promedio es " notas / materias
		FinSi
	Fin Mientras
	
FinAlgoritmo
