
def eliminar_elemento(lista,elemento):
    if elemento in lista:
        lista.remove(elemento)
    else:
        print("El elemento", elemento, " no se encuentra en ", lista)

def test_eliminar_elemento():
    mi_lista = [1,2,3,4,5]
    eliminar_elemento(mi_lista,3)
    assert mi_lista == [1,2,4,5]