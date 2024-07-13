from scipy.spatial import distance
import numpy as np

class NodoN:
    def __init__(self, id, position, type):
        self.id = id
        self.index_route = None
        self.position = position
        self.type = type#1 pista normal, 2 curva
        self.pre_enlaces = []
        self.enlaces = []
        self.quantity_vehicles = 0
        
    def longitud(self):
        return distance.euclidean(self.position[0], self.position[1])
    
    def siguiente_nodo(self, index_route):
        for enlace in self.enlaces:
            if(enlace.index_route == index_route):
                return enlace
        return None
    def random_nodo(self):
        #for enlace in self.enlaces:
            #print('enlaces', enlace.index_route)
        if(len(self.enlaces) > 0):
            nodo = self.enlaces[-1]
            #print('id', nodo.index_route)
            nodo = np.random.choice(self.enlaces)
            return nodo.index_route
        else:
            return None
        
class ArbolN:
    def __init__(self):
        self.raiz = None
        self.contador_id = 0
        self.index_route = 0
        self.draw = []
        self.buscador = []
        
    def insertar(self, position, type=1, pre_enlaces=[]):
        nuevo_nodo = NodoN(self.contador_id, position, type)
        self.contador_id += 1
        for padre in pre_enlaces:
            padre.enlaces.append(nuevo_nodo)
            nuevo_nodo.pre_enlaces.append(padre)
        if not pre_enlaces: # Si no se especifican pre_enlaces, el nodo es la raíz
            self.raiz = nuevo_nodo
        return nuevo_nodo
    
    def enlazar(self, inicio, fin):
        inicio.enlaces.append(fin)
        fin.pre_enlaces.append(inicio)
        
    def insertar_curva(self, curva, padre):
        padre_temp = padre
        for indice, curv in enumerate(curva):
            nuevo_nodo = NodoN(self.contador_id, curv, 2)
            self.contador_id += 1
            padre_temp.enlaces.append(nuevo_nodo)
            nuevo_nodo.pre_enlaces.append(padre_temp)
            padre_temp = nuevo_nodo
        return padre_temp
    
  
    def imprimir(self):
        if self.raiz:
            self._imprimir_recursivo(self.raiz)
        else:
            print("El árbol está vacío.")
        return self.draw
    
    def _imprimir_recursivo(self, nodo):
        if(nodo.index_route is None):
            #print(str(nodo.id) + ": " + (nodo.position) + " => " + str(len(nodo.pre_enlaces)))
            if(nodo.position is not None):
                self.draw.append(nodo.position)
                nodo.index_route = self.index_route
                self.index_route += 1
            for hijo in nodo.enlaces:
                self._imprimir_recursivo(hijo)
    def buscar_nodo_por_index_route(self, index_route):
        nodo = self.buscar_nodo_por_index_route_recursivo(self.raiz, index_route)
        self.buscador.clear()
        return nodo
    
    def buscar_nodo_por_index_route_recursivo(self, nodo, index_route):
        if(nodo.index_route not in self.buscador):
            self.buscador.append(nodo.index_route)
            if (nodo.index_route == index_route):
                return nodo
            for enlace in nodo.enlaces:
                result = self.buscar_nodo_por_index_route_recursivo(enlace, index_route)
                if result is not None:
                    return result
        return None
    
    
    # estructura [inicio y fin]
    # tenemos que evitar bucles
    # considerar longitudes de caminos
    
    #def generar_camino(self, inicio, fin):#inicio y fin son nodos
    #    camino = []
    #    self.buscar_camino(inicio, fin, camino)
    #    
    #def buscar_camino(self, nodo, fin, camino=[]):
    #    if(nodo.index_route in camino):
    #        camino.append(nodo.index_route)
    #        if(nodo.index_route is fin.index_route):
    #            None
    #        else:
    #            for hijo in nodo.enlaces:
    #                self.buscar_camino(camino, hijo, fin)
                    
    

# Ejemplo de uso
#arbol_n = ArbolN()  # Árbol ternario, cada nodo puede tener hasta 3 enlaces
#nodo2 = arbol_n.insertar("Nodo 2")
#print(nodo2.position)
#nodo2_1 = arbol_n.insertar("Nodo 2_1", 1, [nodo2])
#nodo_curva1 = arbol_n.insertar_curva(["curva 1", "curva 2", "curva 3"], nodo2)
#nodo_curva2 = arbol_n.insertar_curva(["curva 4", "curva 5", "curva 6"], nodo2_1)
#print(nodo_curva1.position)
#nodo6 = arbol_n.insertar("Nodo 6", 1, [nodo_curva1, nodo_curva2])
#print(nodo6.position)
#
#arbol_n.enlazar(nodo6, nodo2_1)
#
#print(arbol_n.raiz.position)
#print(arbol_n.raiz.enlaces[0].position)
#print("-------------------------")
#
#temp = arbol_n.imprimir()
#print( '[' + ', '.join(map(str, temp)) + ']')