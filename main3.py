import numpy as np
from trafficSim import *
from trafficSim.route import ArbolN

sim = Simulation()
street = ArbolN()
# Play with these
n = 10
a = -2
b = 12
l = 300

entrance_low_distance = 40
main_hight_distance = 80

NUM_OF_ROADS = 36
VEHICLE_RATE = 100
STEPS_PER_UPDATE = 2

MAIN_ROAD_INIT = (-300, 300)
MAIN_ROAD_END = (300, -300)

#TRAMO 1
MAIN_ROAD_INIT_1_1 = MAIN_ROAD_INIT
MAIN_ROAD_END_1_1 = (MAIN_ROAD_INIT_1_1[0]+main_hight_distance, MAIN_ROAD_INIT_1_1[1]-main_hight_distance)
ROAD_MAIN_1_1 = (MAIN_ROAD_INIT_1_1, MAIN_ROAD_END_1_1)

MAIN_ROAD_INIT_2_1 = (MAIN_ROAD_INIT_1_1[0]-3, MAIN_ROAD_INIT_1_1[1]-3)
MAIN_ROAD_END_2_1 = (MAIN_ROAD_INIT_2_1[0]+main_hight_distance, MAIN_ROAD_INIT_2_1[1]-main_hight_distance)
ROAD_MAIN_2_1 = (MAIN_ROAD_INIT_2_1, MAIN_ROAD_END_2_1)

MAIN_ROAD_END_3_1 = (MAIN_ROAD_INIT_2_1[0]-3, MAIN_ROAD_INIT_2_1[1]-3)
MAIN_ROAD_INIT_3_1 = (MAIN_ROAD_END_3_1[0]+main_hight_distance, MAIN_ROAD_END_3_1[1]-main_hight_distance)
ROAD_MAIN_3_1 = (MAIN_ROAD_INIT_3_1, MAIN_ROAD_END_3_1)

MAIN_ROAD_END_4_1 = (MAIN_ROAD_END_3_1[0]-3, MAIN_ROAD_END_3_1[1]-3)
MAIN_ROAD_INIT_4_1 = (MAIN_ROAD_END_4_1[0]+main_hight_distance, MAIN_ROAD_END_4_1[1]-main_hight_distance)
ROAD_MAIN_4_1 = (MAIN_ROAD_INIT_4_1, MAIN_ROAD_END_4_1)

#DESVIO 1

ENTRANCE_1_1 = (MAIN_ROAD_END_1_1[0]+3, MAIN_ROAD_END_1_1[1])
ENTRANCE_1_2 = (ENTRANCE_1_1[0]+entrance_low_distance, ENTRANCE_1_1[1]+entrance_low_distance)
ENTRANCE_TRAMO_1_1 = (ENTRANCE_1_1, ENTRANCE_1_2)

ENTRANCE_2_1 = (ENTRANCE_1_1[0]+3, ENTRANCE_1_1[1]-3)
ENTRANCE_2_2 = (ENTRANCE_2_1[0]+entrance_low_distance, ENTRANCE_2_1[1]+entrance_low_distance)
ENTRANCE_TRAMO_2_1 = (ENTRANCE_2_2, ENTRANCE_2_1)

ENTRANCE_LONG_1_1 = (ENTRANCE_2_2[0]+3, ENTRANCE_2_2[1])
ENTRANCE_LONG_2_1 = (ENTRANCE_LONG_1_1[0]+3, ENTRANCE_LONG_1_1[1]+3)

#TRAMO 2
MAIN_ROAD_INIT_1_2 = (ENTRANCE_2_1[0], ENTRANCE_2_1[1]-3)
MAIN_ROAD_END_1_2 = (MAIN_ROAD_INIT_1_2[0]+main_hight_distance, MAIN_ROAD_INIT_1_2[1]-main_hight_distance)
ROAD_MAIN_1_2 = (MAIN_ROAD_INIT_1_2, MAIN_ROAD_END_1_2)

MAIN_ROAD_INIT_2_2 = (MAIN_ROAD_INIT_1_2[0]-3, MAIN_ROAD_INIT_1_2[1]-3)
MAIN_ROAD_END_2_2 = (MAIN_ROAD_INIT_2_2[0]+main_hight_distance, MAIN_ROAD_INIT_2_2[1]-main_hight_distance)
ROAD_MAIN_2_2 = (MAIN_ROAD_INIT_2_2, MAIN_ROAD_END_2_2)

MAIN_ROAD_END_3_2 = (MAIN_ROAD_INIT_2_2[0]-3, MAIN_ROAD_INIT_2_2[1]-3)
MAIN_ROAD_INIT_3_2 = (MAIN_ROAD_END_3_2[0]+main_hight_distance, MAIN_ROAD_END_3_2[1]-main_hight_distance)
ROAD_MAIN_3_2 = (MAIN_ROAD_INIT_3_2, MAIN_ROAD_END_3_2)

MAIN_ROAD_END_4_2 = (MAIN_ROAD_END_3_2[0]-3, MAIN_ROAD_END_3_2[1]-3)
MAIN_ROAD_INIT_4_2 = (MAIN_ROAD_END_4_2[0]+main_hight_distance, MAIN_ROAD_END_4_2[1]-main_hight_distance)
ROAD_MAIN_4_2 = (MAIN_ROAD_INIT_4_2, MAIN_ROAD_END_4_2)

#INTERSECCION 1

INTERSECTION_RECT_1_1 = (MAIN_ROAD_END_1_1, MAIN_ROAD_INIT_1_2)
INTERSECTION_RECT_2_1 = (MAIN_ROAD_END_2_1, MAIN_ROAD_INIT_2_2)
INTERSECTION_RECT_3_1 = (MAIN_ROAD_END_3_2, MAIN_ROAD_INIT_3_1)
INTERSECTION_RECT_4_1 = (MAIN_ROAD_END_4_2, MAIN_ROAD_INIT_4_1)
#RECT_ENTRANCE
INTERSECTION_TURN_1_1 = turn_road(MAIN_ROAD_END_1_1, ENTRANCE_1_1, TURN_RIGHT, n)
INTERSECTION_TURN_2_1 = turn_road(MAIN_ROAD_END_2_1, ENTRANCE_1_1, TURN_RIGHT, n)
INTERSECTION_TURN_3_1 = turn_road(MAIN_ROAD_END_3_2, ENTRANCE_1_1, TURN_LEFT, n)
INTERSECTION_TURN_4_1 = turn_road(MAIN_ROAD_END_4_2, ENTRANCE_1_1, TURN_LEFT, n)

INTERSECTION_TURN_1_2 = turn_road(ENTRANCE_2_1, MAIN_ROAD_INIT_1_2, TURN_RIGHT, n)
INTERSECTION_TURN_2_2 = turn_road(ENTRANCE_2_1, MAIN_ROAD_INIT_2_2, TURN_RIGHT, n)
INTERSECTION_TURN_3_2 = turn_road(ENTRANCE_2_1, MAIN_ROAD_INIT_3_1, TURN_LEFT, n)
INTERSECTION_TURN_4_2 = turn_road(ENTRANCE_2_1, MAIN_ROAD_INIT_4_1, TURN_LEFT, n)

#DESVIO 2

ENTRANCE_3_1 = (MAIN_ROAD_INIT_4_2[0], MAIN_ROAD_INIT_4_2[1]-3)
ENTRANCE_3_2 = (ENTRANCE_3_1[0]-entrance_low_distance, ENTRANCE_3_1[1]-entrance_low_distance)
ENTRANCE_TRAMO_3_1 = (ENTRANCE_3_2,ENTRANCE_3_1)

ENTRANCE_4_1 = (ENTRANCE_3_1[0]+3, ENTRANCE_3_1[1]-3)
ENTRANCE_4_2 = (ENTRANCE_4_1[0]-entrance_low_distance, ENTRANCE_4_1[1]-entrance_low_distance)
ENTRANCE_TRAMO_4_1 = (ENTRANCE_4_1,ENTRANCE_4_2)

ENTRANCE_LONG_3_1 = (ENTRANCE_4_2[0], ENTRANCE_4_2[1]-3)
ENTRANCE_LONG_4_1 = (ENTRANCE_LONG_3_1[0]-3, ENTRANCE_LONG_3_1[1]-3)

#TRAMO 3
MAIN_ROAD_INIT_1_3 = (ENTRANCE_4_1[0]+3+9, ENTRANCE_4_1[1]+9)
MAIN_ROAD_END_1_3 = (MAIN_ROAD_INIT_1_3[0]+main_hight_distance, MAIN_ROAD_INIT_1_3[1]-main_hight_distance)
ROAD_MAIN_1_3 = (MAIN_ROAD_INIT_1_3, MAIN_ROAD_END_1_3)

MAIN_ROAD_INIT_2_3 = (MAIN_ROAD_INIT_1_3[0]-3, MAIN_ROAD_INIT_1_3[1]-3)
MAIN_ROAD_END_2_3 = (MAIN_ROAD_INIT_2_3[0]+main_hight_distance, MAIN_ROAD_INIT_2_3[1]-main_hight_distance)
ROAD_MAIN_2_3 = (MAIN_ROAD_INIT_2_3, MAIN_ROAD_END_2_3)

MAIN_ROAD_END_3_3 = (MAIN_ROAD_INIT_2_3[0]-3, MAIN_ROAD_INIT_2_3[1]-3)
MAIN_ROAD_INIT_3_3 = (MAIN_ROAD_END_3_3[0]+main_hight_distance, MAIN_ROAD_END_3_3[1]-main_hight_distance)
ROAD_MAIN_3_3 = (MAIN_ROAD_INIT_3_3, MAIN_ROAD_END_3_3)

MAIN_ROAD_END_4_3 = (MAIN_ROAD_END_3_3[0]-3, MAIN_ROAD_END_3_3[1]-3)
MAIN_ROAD_INIT_4_3 = (MAIN_ROAD_END_4_3[0]+main_hight_distance, MAIN_ROAD_END_4_3[1]-main_hight_distance)
ROAD_MAIN_4_3 = (MAIN_ROAD_INIT_4_3, MAIN_ROAD_END_4_3)

#INTERSECCION 2

INTERSECTION_RECT_1_2 = (MAIN_ROAD_END_1_2, MAIN_ROAD_INIT_1_3)
INTERSECTION_RECT_2_2 = (MAIN_ROAD_END_2_2, MAIN_ROAD_INIT_2_3)
INTERSECTION_RECT_3_2 = (MAIN_ROAD_END_3_3, MAIN_ROAD_INIT_3_2)
INTERSECTION_RECT_4_2 = (MAIN_ROAD_END_4_3, MAIN_ROAD_INIT_4_2)
#RECT_ENTRANCE
INTERSECTION_TURN_4_3 = turn_road(MAIN_ROAD_END_4_3, ENTRANCE_4_1, TURN_RIGHT, n)
INTERSECTION_TURN_3_3 = turn_road(MAIN_ROAD_END_3_3, ENTRANCE_4_1, TURN_RIGHT, n)
INTERSECTION_TURN_2_3 = turn_road(MAIN_ROAD_END_2_2, ENTRANCE_4_1, TURN_LEFT, n)
INTERSECTION_TURN_1_3 = turn_road(MAIN_ROAD_END_1_2, ENTRANCE_4_1, TURN_LEFT, n)

INTERSECTION_TURN_4_4 = turn_road(ENTRANCE_3_1, MAIN_ROAD_INIT_4_2, TURN_RIGHT, n)
INTERSECTION_TURN_3_4 = turn_road(ENTRANCE_3_1, MAIN_ROAD_INIT_3_2, TURN_RIGHT, n)
INTERSECTION_TURN_2_4 = turn_road(ENTRANCE_3_1, MAIN_ROAD_INIT_2_3, TURN_LEFT, n)
INTERSECTION_TURN_1_4 = turn_road(ENTRANCE_3_1, MAIN_ROAD_INIT_1_3, TURN_LEFT, n)

#DESVIO 3

ENTRANCE_1_3 = (MAIN_ROAD_END_1_3[0]+3, MAIN_ROAD_END_1_3[1])
ENTRANCE_1_4 = (ENTRANCE_1_3[0]+entrance_low_distance, ENTRANCE_1_3[1]+entrance_low_distance)
ENTRANCE_TRAMO_1_2 = (ENTRANCE_1_3, ENTRANCE_1_4)

ENTRANCE_2_3 = (ENTRANCE_1_3[0]+3, ENTRANCE_1_3[1]-3)
ENTRANCE_2_4 = (ENTRANCE_2_3[0]+entrance_low_distance, ENTRANCE_2_3[1]+entrance_low_distance)
ENTRANCE_TRAMO_2_2 = (ENTRANCE_2_4, ENTRANCE_2_3)

ENTRANCE_LONG_1_2 = (ENTRANCE_1_4[0], ENTRANCE_1_4[1]+3)
ENTRANCE_LONG_2_2 = (ENTRANCE_LONG_1_2[0]+3, ENTRANCE_LONG_1_2[1]+3)

#TRAMO 4
MAIN_ROAD_INIT_1_4 = (ENTRANCE_2_3[0], ENTRANCE_2_3[1]-3)
MAIN_ROAD_END_1_4 = (MAIN_ROAD_INIT_1_4[0]+main_hight_distance, MAIN_ROAD_INIT_1_4[1]-main_hight_distance)
ROAD_MAIN_1_4 = (MAIN_ROAD_INIT_1_4, MAIN_ROAD_END_1_4)

MAIN_ROAD_INIT_2_4 = (MAIN_ROAD_INIT_1_4[0]-3, MAIN_ROAD_INIT_1_4[1]-3)
MAIN_ROAD_END_2_4 = (MAIN_ROAD_INIT_2_4[0]+main_hight_distance, MAIN_ROAD_INIT_2_4[1]-main_hight_distance)
ROAD_MAIN_2_4 = (MAIN_ROAD_INIT_2_4, MAIN_ROAD_END_2_4)

MAIN_ROAD_END_3_4 = (MAIN_ROAD_INIT_2_4[0]-3, MAIN_ROAD_INIT_2_4[1]-3)
MAIN_ROAD_INIT_3_4 = (MAIN_ROAD_END_3_4[0]+main_hight_distance, MAIN_ROAD_END_3_4[1]-main_hight_distance)
ROAD_MAIN_3_4 = (MAIN_ROAD_INIT_3_4, MAIN_ROAD_END_3_4)

MAIN_ROAD_END_4_4 = (MAIN_ROAD_END_3_4[0]-3, MAIN_ROAD_END_3_4[1]-3)
MAIN_ROAD_INIT_4_4 = (MAIN_ROAD_END_4_4[0]+main_hight_distance, MAIN_ROAD_END_4_4[1]-main_hight_distance)
ROAD_MAIN_4_4 = (MAIN_ROAD_INIT_4_4, MAIN_ROAD_END_4_4)

#INTERSECCION 3

INTERSECTION_RECT_1_3 = (MAIN_ROAD_END_1_3, MAIN_ROAD_INIT_1_4)
INTERSECTION_RECT_2_3 = (MAIN_ROAD_END_2_3, MAIN_ROAD_INIT_2_4)
INTERSECTION_RECT_3_3 = (MAIN_ROAD_END_3_4, MAIN_ROAD_INIT_3_3)
INTERSECTION_RECT_4_3 = (MAIN_ROAD_END_4_4, MAIN_ROAD_INIT_4_3)
#RECT_ENTRANCE
INTERSECTION_TURN_1_5 = turn_road(MAIN_ROAD_END_1_3, ENTRANCE_1_3, TURN_RIGHT, n)
INTERSECTION_TURN_2_5 = turn_road(MAIN_ROAD_END_2_3, ENTRANCE_1_3, TURN_RIGHT, n)
INTERSECTION_TURN_3_5 = turn_road(MAIN_ROAD_END_3_4, ENTRANCE_1_3, TURN_LEFT, n)
INTERSECTION_TURN_4_5 = turn_road(MAIN_ROAD_END_4_4, ENTRANCE_1_3, TURN_LEFT, n)

INTERSECTION_TURN_1_6 = turn_road(ENTRANCE_2_3, MAIN_ROAD_INIT_1_4, TURN_RIGHT, n)
INTERSECTION_TURN_2_6 = turn_road(ENTRANCE_2_3, MAIN_ROAD_INIT_2_4, TURN_RIGHT, n)
INTERSECTION_TURN_3_6 = turn_road(ENTRANCE_2_3, MAIN_ROAD_INIT_3_3, TURN_LEFT, n)
INTERSECTION_TURN_4_6 = turn_road(ENTRANCE_2_3, MAIN_ROAD_INIT_4_3, TURN_LEFT, n)

#DESVIO 4

ENTRANCE_3_3 = (MAIN_ROAD_INIT_4_4[0], MAIN_ROAD_INIT_4_4[1]-3)
ENTRANCE_3_4 = (ENTRANCE_3_3[0]-entrance_low_distance, ENTRANCE_3_3[1]-entrance_low_distance)
ENTRANCE_TRAMO_3_2 = (ENTRANCE_3_4,ENTRANCE_3_3)

ENTRANCE_4_3 = (ENTRANCE_3_3[0]+3, ENTRANCE_3_3[1]-3)
ENTRANCE_4_4 = (ENTRANCE_4_3[0]-entrance_low_distance, ENTRANCE_4_3[1]-entrance_low_distance)
ENTRANCE_TRAMO_4_2 = (ENTRANCE_4_3,ENTRANCE_4_4)

ENTRANCE_LONG_3_2 = (ENTRANCE_3_4[0]-3, ENTRANCE_3_4[1])
ENTRANCE_LONG_4_2 = (ENTRANCE_LONG_3_2[0]-3, ENTRANCE_LONG_3_2[1]-3)

#TRAMO 5
MAIN_ROAD_INIT_1_5 = (ENTRANCE_4_3[0]+3+9, ENTRANCE_4_3[1]+9)
MAIN_ROAD_END_1_5 = (MAIN_ROAD_INIT_1_5[0]+main_hight_distance, MAIN_ROAD_INIT_1_5[1]-main_hight_distance)
ROAD_MAIN_1_5 = (MAIN_ROAD_INIT_1_5, MAIN_ROAD_END_1_5)

MAIN_ROAD_INIT_2_5 = (MAIN_ROAD_INIT_1_5[0]-3, MAIN_ROAD_INIT_1_5[1]-3)
MAIN_ROAD_END_2_5 = (MAIN_ROAD_INIT_2_5[0]+main_hight_distance, MAIN_ROAD_INIT_2_5[1]-main_hight_distance)
ROAD_MAIN_2_5 = (MAIN_ROAD_INIT_2_5, MAIN_ROAD_END_2_5)

MAIN_ROAD_END_3_5 = (MAIN_ROAD_INIT_2_5[0]-3, MAIN_ROAD_INIT_2_5[1]-3)
MAIN_ROAD_INIT_3_5 = (MAIN_ROAD_END_3_5[0]+main_hight_distance, MAIN_ROAD_END_3_5[1]-main_hight_distance)
ROAD_MAIN_3_5 = (MAIN_ROAD_INIT_3_5, MAIN_ROAD_END_3_5)

MAIN_ROAD_END_4_5 = (MAIN_ROAD_END_3_5[0]-3, MAIN_ROAD_END_3_5[1]-3)
MAIN_ROAD_INIT_4_5 = (MAIN_ROAD_END_4_5[0]+main_hight_distance, MAIN_ROAD_END_4_5[1]-main_hight_distance)
ROAD_MAIN_4_5 = (MAIN_ROAD_INIT_4_5, MAIN_ROAD_END_4_5)

#INTERSECCION 4

INTERSECTION_RECT_1_4 = (MAIN_ROAD_END_1_4, MAIN_ROAD_INIT_1_5)
INTERSECTION_RECT_2_4 = (MAIN_ROAD_END_2_4, MAIN_ROAD_INIT_2_5)
INTERSECTION_RECT_3_4 = (MAIN_ROAD_END_3_5, MAIN_ROAD_INIT_3_4)
INTERSECTION_RECT_4_4 = (MAIN_ROAD_END_4_5, MAIN_ROAD_INIT_4_4)
#RECT_ENTRANCE
INTERSECTION_TURN_4_7 = turn_road(MAIN_ROAD_END_4_5, ENTRANCE_4_3, TURN_RIGHT, n)
INTERSECTION_TURN_3_7 = turn_road(MAIN_ROAD_END_3_5, ENTRANCE_4_3, TURN_RIGHT, n)
INTERSECTION_TURN_2_7 = turn_road(MAIN_ROAD_END_2_4, ENTRANCE_4_3, TURN_LEFT, n)
INTERSECTION_TURN_1_7 = turn_road(MAIN_ROAD_END_1_4, ENTRANCE_4_3, TURN_LEFT, n)

INTERSECTION_TURN_4_8 = turn_road(ENTRANCE_3_3, MAIN_ROAD_INIT_4_4, TURN_RIGHT, n)
INTERSECTION_TURN_3_8 = turn_road(ENTRANCE_3_3, MAIN_ROAD_INIT_3_4, TURN_RIGHT, n)
INTERSECTION_TURN_2_8 = turn_road(ENTRANCE_3_3, MAIN_ROAD_INIT_2_5, TURN_LEFT, n)
INTERSECTION_TURN_1_8 = turn_road(ENTRANCE_3_3, MAIN_ROAD_INIT_1_5, TURN_LEFT, n)

#CAMINOS DE DESVIOS
ENTRANCE_LONG_TRAMO_1 = (ENTRANCE_LONG_1_2, ENTRANCE_LONG_1_1)
ENTRANCE_LONG_TRAMO_2 = (ENTRANCE_LONG_2_1, ENTRANCE_LONG_2_2)
ENTRANCE_LONG_TRAMO_3 = (ENTRANCE_LONG_3_1, ENTRANCE_LONG_3_2)
ENTRANCE_LONG_TRAMO_4 = (ENTRANCE_LONG_4_2, ENTRANCE_LONG_4_1)
#curva desvio
ENTRANCE_TURN_1_1 = turn_road(ENTRANCE_LONG_1_1, ENTRANCE_2_2, TURN_RIGHT, n)
ENTRANCE_TURN_1_2 = turn_road(ENTRANCE_1_2, ENTRANCE_LONG_2_1, TURN_LEFT, n)

ENTRANCE_TURN_2_1 = turn_road(ENTRANCE_1_4, ENTRANCE_LONG_1_2, TURN_RIGHT, n)
ENTRANCE_TURN_2_2 = turn_road(ENTRANCE_LONG_2_2, ENTRANCE_2_4, TURN_LEFT, n)

ENTRANCE_TURN_3_1 = turn_road(ENTRANCE_4_2, ENTRANCE_LONG_3_1, TURN_RIGHT, n)
ENTRANCE_TURN_3_2 = turn_road(ENTRANCE_LONG_4_1, ENTRANCE_3_2, TURN_LEFT, n)

ENTRANCE_TURN_4_1 = turn_road(ENTRANCE_LONG_3_2, ENTRANCE_3_4, TURN_RIGHT, n)
ENTRANCE_TURN_4_2 = turn_road(ENTRANCE_4_4, ENTRANCE_LONG_4_2, TURN_LEFT, n)

raiz_principal = street.insertar(None)

calleprincipalentrada1_1 = street.insertar(ROAD_MAIN_1_1, 1, [raiz_principal])
calleprincipalentrada2_1 = street.insertar(ROAD_MAIN_2_1, 1, [raiz_principal])
calleprincipalentrada3_5 = street.insertar(ROAD_MAIN_3_5, 1, [raiz_principal])
calleprincipalentrada4_5 = street.insertar(ROAD_MAIN_4_5, 1, [raiz_principal])

intersecciontecta1_1 = street.insertar(INTERSECTION_RECT_1_1, 2, [calleprincipalentrada1_1])
intersecciontecta2_1 = street.insertar(INTERSECTION_RECT_2_1, 2, [calleprincipalentrada2_1])
intersecciontecta3_4 = street.insertar(INTERSECTION_RECT_3_4, 2, [calleprincipalentrada3_5])
intersecciontecta4_4 = street.insertar(INTERSECTION_RECT_4_4, 2, [calleprincipalentrada4_5])

calleprincipalentrada1_2 = street.insertar(ROAD_MAIN_1_2, 1, [intersecciontecta1_1])
calleprincipalentrada2_2 = street.insertar(ROAD_MAIN_2_2, 1, [intersecciontecta2_1])
calleprincipalentrada3_4 = street.insertar(ROAD_MAIN_3_4, 1, [intersecciontecta3_4])
calleprincipalentrada4_4 = street.insertar(ROAD_MAIN_4_4, 1, [intersecciontecta4_4])

intersecciontecta1_2 = street.insertar(INTERSECTION_RECT_1_2, 2, [calleprincipalentrada1_2])
intersecciontecta2_2 = street.insertar(INTERSECTION_RECT_2_2, 2, [calleprincipalentrada2_2])
intersecciontecta3_3 = street.insertar(INTERSECTION_RECT_3_3, 2, [calleprincipalentrada3_4])
intersecciontecta4_3 = street.insertar(INTERSECTION_RECT_4_3, 2, [calleprincipalentrada4_4])

calleprincipalentrada1_3 = street.insertar(ROAD_MAIN_1_3, 1, [intersecciontecta1_2])
calleprincipalentrada2_3 = street.insertar(ROAD_MAIN_2_3, 1, [intersecciontecta2_2])
calleprincipalentrada3_3 = street.insertar(ROAD_MAIN_3_3, 1, [intersecciontecta3_3])
calleprincipalentrada4_3 = street.insertar(ROAD_MAIN_4_3, 1, [intersecciontecta4_3])

intersecciontecta1_3 = street.insertar(INTERSECTION_RECT_1_3, 2, [calleprincipalentrada1_3])
intersecciontecta2_3 = street.insertar(INTERSECTION_RECT_2_3, 2, [calleprincipalentrada2_3])
intersecciontecta3_2 = street.insertar(INTERSECTION_RECT_3_2, 2, [calleprincipalentrada3_3])
intersecciontecta4_2 = street.insertar(INTERSECTION_RECT_4_2, 2, [calleprincipalentrada4_3])

calleprincipalentrada1_4 = street.insertar(ROAD_MAIN_1_4, 1, [intersecciontecta1_3])
calleprincipalentrada2_4 = street.insertar(ROAD_MAIN_2_4, 1, [intersecciontecta2_3])
calleprincipalentrada3_2 = street.insertar(ROAD_MAIN_3_2, 1, [intersecciontecta3_2])
calleprincipalentrada4_2 = street.insertar(ROAD_MAIN_4_2, 1, [intersecciontecta4_2])

intersecciontecta1_4 = street.insertar(INTERSECTION_RECT_1_4, 2, [calleprincipalentrada1_4])
intersecciontecta2_4 = street.insertar(INTERSECTION_RECT_2_4, 2, [calleprincipalentrada2_4])
intersecciontecta3_1 = street.insertar(INTERSECTION_RECT_3_1, 2, [calleprincipalentrada3_2])
intersecciontecta4_1 = street.insertar(INTERSECTION_RECT_4_1, 2, [calleprincipalentrada4_2])

calleprincipalentrada1_5 = street.insertar(ROAD_MAIN_1_5, 1, [intersecciontecta1_4])
calleprincipalentrada2_5 = street.insertar(ROAD_MAIN_2_5, 1, [intersecciontecta2_4])
calleprincipalentrada3_1 = street.insertar(ROAD_MAIN_3_1, 1, [intersecciontecta3_1])
calleprincipalentrada4_1 = street.insertar(ROAD_MAIN_4_1, 1, [intersecciontecta4_1])

#INTERSECCION 1
#calle externa
desvioabajocurva_1_1_1 = street.insertar_curva(INTERSECTION_TURN_1_1, calleprincipalentrada1_1)
desvioabajocurva_1_2_1 = street.insertar_curva(INTERSECTION_TURN_2_1, calleprincipalentrada2_1)
desvioabajocurva_1_3_1 = street.insertar_curva(INTERSECTION_TURN_3_1, calleprincipalentrada3_2)
desvioabajocurva_1_4_1 = street.insertar_curva(INTERSECTION_TURN_4_1, calleprincipalentrada4_2)

desvioabajorecta_1_1_1 = street.insertar(ENTRANCE_TRAMO_1_1, 1, [desvioabajocurva_1_1_1, desvioabajocurva_1_2_1, desvioabajocurva_1_3_1, desvioabajocurva_1_4_1])

desvioabajocurva_1_1_2 = street.insertar_curva(ENTRANCE_TURN_1_2, desvioabajorecta_1_1_1)

desvioabajorecta_1_1_2 = street.insertar(ENTRANCE_LONG_TRAMO_2, 1, [desvioabajocurva_1_1_2])

desvioabajocurva_1_1_3 = street.insertar_curva(ENTRANCE_TURN_2_2, desvioabajorecta_1_1_2)

desvioabajorecta_1_1_3 = street.insertar(ENTRANCE_TRAMO_2_2, 1, [desvioabajocurva_1_1_3])

desvioabajocurva_1_1_4 = street.insertar_curva(INTERSECTION_TURN_1_6, desvioabajorecta_1_1_3)
desvioabajocurva_1_2_4 = street.insertar_curva(INTERSECTION_TURN_2_6, desvioabajorecta_1_1_3)
desvioabajocurva_1_3_4 = street.insertar_curva(INTERSECTION_TURN_3_6, desvioabajorecta_1_1_3)
desvioabajocurva_1_4_4 = street.insertar_curva(INTERSECTION_TURN_4_6, desvioabajorecta_1_1_3)

street.enlazar(desvioabajocurva_1_1_4, calleprincipalentrada1_4)
street.enlazar(desvioabajocurva_1_2_4, calleprincipalentrada2_4)
street.enlazar(desvioabajocurva_1_3_4, calleprincipalentrada3_3)
street.enlazar(desvioabajocurva_1_4_4, calleprincipalentrada4_3)

#calle interna


desvioabajocurva_2_1_4 = street.insertar_curva(INTERSECTION_TURN_1_5, calleprincipalentrada1_3)
desvioabajocurva_2_2_4 = street.insertar_curva(INTERSECTION_TURN_2_5, calleprincipalentrada2_3)
desvioabajocurva_2_3_4 = street.insertar_curva(INTERSECTION_TURN_3_5, calleprincipalentrada3_4)
desvioabajocurva_2_4_4 = street.insertar_curva(INTERSECTION_TURN_4_5, calleprincipalentrada4_4)

desvioabajorecta_2_1_3 = street.insertar(ENTRANCE_TRAMO_2_1, 1, [desvioabajocurva_2_1_4, desvioabajocurva_2_2_4, desvioabajocurva_2_3_4, desvioabajocurva_2_4_4])

desvioabajocurva_2_1_3 = street.insertar_curva(ENTRANCE_TURN_1_1, desvioabajorecta_2_1_3)

desvioabajorecta_2_1_2 = street.insertar(ENTRANCE_LONG_TRAMO_1, 1, [desvioabajocurva_2_1_3])

desvioabajocurva_2_1_2 = street.insertar_curva(ENTRANCE_TURN_2_1, desvioabajorecta_2_1_2)

desvioabajorecta_2_1_1 = street.insertar(ENTRANCE_TRAMO_1_2, 1, [desvioabajocurva_2_1_2])

desvioabajocurva_2_1_1 = street.insertar_curva(INTERSECTION_TURN_1_2, desvioabajorecta_2_1_1)
desvioabajocurva_2_2_1 = street.insertar_curva(INTERSECTION_TURN_2_2, desvioabajorecta_2_1_1)
desvioabajocurva_2_3_1 = street.insertar_curva(INTERSECTION_TURN_3_2, desvioabajorecta_2_1_1)
desvioabajocurva_2_4_1 = street.insertar_curva(INTERSECTION_TURN_4_2, desvioabajorecta_2_1_1)

street.enlazar(desvioabajocurva_2_1_1, calleprincipalentrada1_2)
street.enlazar(desvioabajocurva_2_2_1, calleprincipalentrada2_2)
street.enlazar(desvioabajocurva_2_3_1, calleprincipalentrada3_1)
street.enlazar(desvioabajocurva_2_4_1, calleprincipalentrada4_1)

#INTERSECCION 2
#calle interna
desvioarribacurva_1_1_1 = street.insertar_curva(INTERSECTION_TURN_2_1, calleprincipalentrada2_1)
desvioarribacurva_1_2_1 = street.insertar_curva(INTERSECTION_TURN_2_1, calleprincipalentrada2_1)
desvioarribacurva_1_3_1 = street.insertar_curva(INTERSECTION_TURN_3_1, calleprincipalentrada3_2)
desvioarribacurva_1_4_1 = street.insertar_curva(INTERSECTION_TURN_4_1, calleprincipalentrada4_2)

desvioarribarecta_1_1_1 = street.insertar(ENTRANCE_TRAMO_4_1, 1, [desvioarribacurva_1_1_1, desvioarribacurva_1_2_1, desvioarribacurva_1_3_1, desvioarribacurva_1_4_1])
desvioarribacurva_1_1_2 = street.insertar_curva(ENTRANCE_TURN_3_1, desvioarribarecta_1_1_1)

desvioarribarecta_1_1_2 = street.insertar(ENTRANCE_LONG_TRAMO_3, 1, [desvioarribacurva_1_1_2])
desvioarribacurva_1_1_3 = street.insertar_curva(ENTRANCE_TURN_4_1, desvioarribarecta_1_1_2)

desvioarribarecta_1_1_3 = street.insertar(ENTRANCE_TRAMO_3_2, 1, [desvioarribacurva_1_1_3])

desvioarribacurva_1_1_4 = street.insertar_curva(INTERSECTION_TURN_4_7, desvioarribarecta_1_1_3)
desvioarribacurva_1_2_4 = street.insertar_curva(INTERSECTION_TURN_3_7, desvioarribarecta_1_1_3)
desvioarribacurva_1_3_4 = street.insertar_curva(INTERSECTION_TURN_2_7, desvioarribarecta_1_1_3)
desvioarribacurva_1_4_4 = street.insertar_curva(INTERSECTION_TURN_1_7, desvioarribarecta_1_1_3)

street.enlazar(desvioarribacurva_1_1_4, calleprincipalentrada1_5)
street.enlazar(desvioarribacurva_1_2_4, calleprincipalentrada2_5)
street.enlazar(desvioarribacurva_1_3_4, calleprincipalentrada3_4)
street.enlazar(desvioarribacurva_1_4_4, calleprincipalentrada4_4)

#calle externa
desvioarribacurva_2_1_4 = street.insertar_curva(INTERSECTION_TURN_1_6, calleprincipalentrada1_2)
desvioarribacurva_2_2_4 = street.insertar_curva(INTERSECTION_TURN_2_6, calleprincipalentrada2_2)
desvioarribacurva_2_3_4 = street.insertar_curva(INTERSECTION_TURN_3_6, calleprincipalentrada3_3)
desvioarribacurva_2_4_4 = street.insertar_curva(INTERSECTION_TURN_4_6, calleprincipalentrada4_3)

desvioarribarecta_2_1_3 = street.insertar(ENTRANCE_TRAMO_3_1, 1, [desvioarribacurva_2_1_4, desvioarribacurva_2_2_4, desvioarribacurva_2_3_4, desvioarribacurva_2_4_4])
desvioarribacurva_2_1_3 = street.insertar_curva(ENTRANCE_TURN_3_2, desvioarribarecta_2_1_3)

desvioarribarecta_2_1_2 = street.insertar(ENTRANCE_LONG_TRAMO_4, 1, [desvioarribacurva_2_1_3])
desvioarribacurva_2_1_2 = street.insertar_curva(ENTRANCE_TURN_4_2, desvioarribarecta_2_1_2)

desvioarribarecta_2_1_1 = street.insertar(ENTRANCE_TRAMO_4_2, 1, [desvioarribacurva_2_1_2])

desvioarribacurva_2_1_1 = street.insertar_curva(INTERSECTION_TURN_1_8, desvioarribarecta_2_1_1)
desvioarribacurva_2_2_1 = street.insertar_curva(INTERSECTION_TURN_2_8, desvioarribarecta_2_1_1)
desvioarribacurva_2_3_1 = street.insertar_curva(INTERSECTION_TURN_3_8, desvioarribarecta_2_1_1)
desvioarribacurva_2_4_1 = street.insertar_curva(INTERSECTION_TURN_4_8, desvioarribarecta_2_1_1)

street.enlazar(desvioarribacurva_2_1_1, calleprincipalentrada1_3,)
street.enlazar(desvioarribacurva_2_2_1, calleprincipalentrada2_3,)
street.enlazar(desvioarribacurva_2_3_1, calleprincipalentrada3_2,)
street.enlazar(desvioarribacurva_2_4_1, calleprincipalentrada4_2,)

#desvioarribacurva / desvioarribarecta
#curvaentrada1 = street.insertar_curva(INTERSECTION_TURN_1_1, 1, [calleprincipalentrada1])
#curvaentrada2 = street.insertar_curva(INTERSECTION_TURN_2_1, 1, [calleprincipalentrada2])
sim.create_tree_routes(street)
sim.create_roads([
    *street.imprimir()
#   ROAD_MAIN_1_1,#0
#   ROAD_MAIN_2_1,#1
#   ROAD_MAIN_3_1,#2
#   ROAD_MAIN_4_1,#3
#   ROAD_MAIN_1_2,#4
#   ROAD_MAIN_2_2,#5
#   ROAD_MAIN_3_2,#6
#   ROAD_MAIN_4_2,#7
#   ROAD_MAIN_1_3,#8
#   ROAD_MAIN_2_3,#9
#   ROAD_MAIN_3_3,#10
#   ROAD_MAIN_4_3,#11
#   ROAD_MAIN_1_4,#12
#   ROAD_MAIN_2_4,#13
#   ROAD_MAIN_3_4,#14
#   ROAD_MAIN_4_4,#15
#   ROAD_MAIN_1_5,#16
#   ROAD_MAIN_2_5,#17
#   ROAD_MAIN_3_5,#18_cu
#   ROAD_MAIN_4_5,#19
#   ENTRANCE_TRAMO_1_1,#20
#   ENTRANCE_TRAMO_2_1,#21
#   ENTRANCE_TRAMO_1_2,#22
#   ENTRANCE_TRAMO_2_2,#23
#   ENTRANCE_TRAMO_3_1,#24
#   ENTRANCE_TRAMO_4_1,#25
#   ENTRANCE_TRAMO_3_2,#26
#   ENTRANCE_TRAMO_4_2,#27
#   ENTRANCE_LONG_TRAMO_1,#28
#   ENTRANCE_LONG_TRAMO_2,#29
#   ENTRANCE_LONG_TRAMO_3,#30
#   ENTRANCE_LONG_TRAMO_4,#31
#   INTERSECTION_RECT_1_1,#32
#   INTERSECTION_RECT_2_1,
#   INTERSECTION_RECT_3_1,
#   INTERSECTION_RECT_4_1,
#   INTERSECTION_RECT_1_2,
#   INTERSECTION_RECT_2_2,
#   INTERSECTION_RECT_3_2,
#   INTERSECTION_RECT_4_2,
#   INTERSECTION_RECT_1_3,
#   INTERSECTION_RECT_2_3,
#   INTERSECTION_RECT_3_3,
#   INTERSECTION_RECT_4_3,
#   INTERSECTION_RECT_1_4,
#   INTERSECTION_RECT_2_4,
#   INTERSECTION_RECT_3_4,
#   INTERSECTION_RECT_4_4,
#   *INTERSECTION_TURN_1_1,
#   *INTERSECTION_TURN_2_1,
#   *INTERSECTION_TURN_3_1,
#   *INTERSECTION_TURN_4_1,
#   *INTERSECTION_TURN_1_2,
#   *INTERSECTION_TURN_2_2,
#   *INTERSECTION_TURN_3_2,
#   *INTERSECTION_TURN_4_2,
#   *INTERSECTION_TURN_1_3,
#   *INTERSECTION_TURN_2_3,
#   *INTERSECTION_TURN_3_3,
#   *INTERSECTION_TURN_4_3,
#   *INTERSECTION_TURN_1_4,
#   *INTERSECTION_TURN_2_4,
#   *INTERSECTION_TURN_3_4,
#   *INTERSECTION_TURN_4_4,
#   *INTERSECTION_TURN_1_5,
#   *INTERSECTION_TURN_2_5,
#   *INTERSECTION_TURN_3_5,
#   *INTERSECTION_TURN_4_5,
#   *INTERSECTION_TURN_1_6,
#   *INTERSECTION_TURN_2_6,
#   *INTERSECTION_TURN_3_6,
#   *INTERSECTION_TURN_4_6,
#   *INTERSECTION_TURN_1_7,
#   *INTERSECTION_TURN_2_7,
#   *INTERSECTION_TURN_3_7,
#   *INTERSECTION_TURN_4_7,
#   *INTERSECTION_TURN_1_8,
#   *INTERSECTION_TURN_2_8,
#   *INTERSECTION_TURN_3_8,
#   *INTERSECTION_TURN_4_8,
#   *ENTRANCE_TURN_1_1,
#   *ENTRANCE_TURN_1_2,
#   *ENTRANCE_TURN_2_1,
#   *ENTRANCE_TURN_2_2,
#   *ENTRANCE_TURN_3_1,
#   *ENTRANCE_TURN_3_2,
#   *ENTRANCE_TURN_4_1,
#   *ENTRANCE_TURN_4_2
])


#buscar = street.buscar_nodo_por_index_route(2)
#print(buscar.id)
#print(buscar.index_route)
#print(buscar.type)
#print(calleprincipalentrada2_1.index_route)
def road(a): return range(a, a+n)
sim.create_gen({
'vehicle_rate': VEHICLE_RATE,
'vehicles':[
    # 1st Lane
    [2, {'path': [calleprincipalentrada1_1.index_route, intersecciontecta1_1.index_route, calleprincipalentrada1_2.index_route, intersecciontecta1_2.index_route, calleprincipalentrada1_3.index_route, intersecciontecta1_3.index_route, calleprincipalentrada1_4.index_route, intersecciontecta1_4.index_route, calleprincipalentrada1_5.index_route]}],
    #[2, {'path': [calleprincipalentrada2_1.index_route, intersecciontecta2_1.index_route, calleprincipalentrada2_2.index_route, intersecciontecta2_2.index_route, calleprincipalentrada2_3.index_route, intersecciontecta2_3.index_route, calleprincipalentrada2_4.index_route, intersecciontecta2_4.index_route, calleprincipalentrada2_5.index_route]}]
]})

"""
sim.create_signal([[0], [1], [2], [3]])
sim.create_signal([[12], [13], [14], [15]])

# Create Green Light for 3rd Lane
sim.create_signal([[24]])
sim.create_signal([[25]])
sim.create_signal([[26]])
sim.create_signal([[27]])
"""

# Start simulation
win = Window(sim)
win.zoom = 10
if(sim.isPaused == False):
    win.run(steps_per_update=STEPS_PER_UPDATE)
