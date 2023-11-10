import unittest

def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    else:
        print("El elemento", elemento, " no se encuentra en ", lista)

class TestEliminarElemento(unittest.TestCase):
    def test_eliminar_elemento(self):
        mi_lista = [1, 2, 3, 4, 5]
        eliminar_elemento(mi_lista, 3)
        self.assertEqual(mi_lista, [1, 2, 4, 5])

if __name__ == '__main__':
    unittest.main()
