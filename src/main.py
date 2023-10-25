def ordenamientoBurbuja(listaNumeros: list) -> list:
    """Función del famoso algoritmo de ordenamiento burbuja el cual consiste en ir recorriendo una lista de valores para ir comprobando si el anterior es mayor que el siguiente y de esta forma ordenar una lista completa de longitud n.

    Args:
        listaNumeros (list): es una lista que se le pasa por parametro.

    Returns:
        list: devuelve una copia de la lista pero ya ordenada así no modificamos la lista original.
    """
    tamañoLista = len(listaNumeros)
    listaOrdenada = listaNumeros.copy()  # Crear una copia de la lista para evitar modificar la lista original

    for i in range(tamañoLista - 1):
        for j in range(tamañoLista - 1 - i):
            if listaOrdenada[j] > listaOrdenada[j + 1]:
                listaOrdenada[j], listaOrdenada[j + 1] = listaOrdenada[j + 1], listaOrdenada[j]

    return listaOrdenada

if __name__=="__main__":
    print(ordenamientoBurbuja([8, 3, 1, 19, 14]))