from modelado.modelo2 import ordenamientoPorSeleccion
# Creamos una lista
miLista= [10, 90, 1, 20, 4, 7]
# Agregamos la lista previamente creada en una nueva con la clase ordenar por seleccion
Lista = ordenamientoPorSeleccion(miLista)
# Presentación
print("Trabajo de requisito\n- Lista 2:")
print(Lista)
print("- Lista ordenada por seleccion\n")
# A la lista la ordenamos por seleccion
Lista.ordenar_seleccion()