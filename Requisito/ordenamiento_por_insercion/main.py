from modelado.modelo1 import ordenamientoPorInsercion
# Creamos una lista
miLista= [10, 90, 1, 20, 4, 7]
# Agregamos la lista previamente creada en una nueva con la clase ordenar por seleccion
Lista = ordenamientoPorInsercion(miLista)
# Presentación
print("Trabajo de requisito\n- Lista 1:")
print(Lista)
print("- Lista ordenada por insercion\n")
# A la lista la ordenamos por seleccion
Lista.ordenar_insercion()
