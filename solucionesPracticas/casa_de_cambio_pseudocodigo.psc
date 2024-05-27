Algoritmo ConversionDolares
	
    Escribir "Ingrese el valor de venta del dólar estadounidense (USD):"
    Leer cambio
    Si cambio <= 0 Entonces
        Mientras cambio <= 0 Hacer
            Escribir "El valor de venta debe ser mayor a cero. Ingrese un nuevo valor"
            Leer cambio
        FinMientras
    FinSi
	
    interesado <- 1
	
    Mientras interesado <> 0 Hacer
        Si interesado = 1 Entonces
            Escribir "Ingrese el monto a convertir a USD:"
            Leer monto
            Escribir "$", monto, " equivalen a ", monto / cambio, " dólares."
        FinSi
		
        Escribir "Desea realizar otra conversión? 2 = cambiar valor de conversión / 1 = Si / 0 = No"
        Leer interesado
		
        Si interesado = 2 Entonces
            Escribir "Ingrese el valor de venta del dólar estadounidense (USD):"
            Leer cambio
            Si cambio <= 0 Entonces
                Mientras cambio <= 0 Hacer
                    Escribir "El valor de venta debe ser mayor a cero. Ingrese un nuevo valor"
                    Leer cambio
                FinMientras
            FinSi
            interesado <- 1  
			FinSi
			Si interesado < 0 O interesado > 2 Entonces
				Mientras interesado < 0 O interesado > 2
					Escribir "La opción seleccionada no es correcta."
					Escribir "Desea realizar una conversión? 2 = cambiar valor de conversión / 1 = Si / 0 = No"
					Leer interesado
				FinMientras
			FinSi
		FinMientras
		
		Escribir "Muchas gracias por utilizar nuestro servicio!"
		
FinAlgoritmo