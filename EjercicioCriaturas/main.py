from EjercicioCriaturas.ArenaDeCombate import ArenaDeCombate
from EjercicioCriaturas.BabosaToxica import BabosaToxica
from EjercicioCriaturas.DragonSolar import DragonSolar
from EjercicioCriaturas.Laboratorio import Laboratorio
from EjercicioCriaturas.RobotOmega import RobotOmega


def separator(title):

    print(f"\n\n=======================================================")
    print(f"                   {title}                        ")
    print("=======================================================")


LOG_FUNCTION = print



separator("A. CREACION DE CRIATURAS Y ENTORNOS")


Drago = DragonSolar("Drago", "Solara", 50, log_func=LOG_FUNCTION)
Slyme = BabosaToxica("Slyme", "Toxonia", 20, log_func=LOG_FUNCTION)
Omni = RobotOmega("Omni", "Cibernia", 8, log_func=LOG_FUNCTION)


arena = ArenaDeCombate(log_func=LOG_FUNCTION)
laboratorio = Laboratorio(log_func=LOG_FUNCTION)


arena.registrar_criatura(Drago)
arena.registrar_criatura(Slyme)
arena.registrar_criatura(Omni)


separator("B. EVOLUCION Y ESTADISTICAS INICIALES")


Drago.evolucionar()
Slyme.evolucionar()
Slyme.evolucionar()

LOG_FUNCTION("\n--- Estadísticas al inicio de la demostración ---")
Drago.mostrar_stats()
Slyme.mostrar_stats()
Omni.mostrar_stats()



separator("C. ENFRENTAMIENTO EN LA ARENA (Batalla 1 y 2)")


ganador1 = arena.enfrentar_aleatorio()
if ganador1 and isinstance(ganador1, (DragonSolar, BabosaToxica, RobotOmega)):
    LOG_FUNCTION(f"\n[Arena] GANADOR DEL COMBATE 1: {ganador1.nombre} (¡ha evolucionado por ganar!)")


Drago.recargar_energia()
Slyme.recargar_energia()
Omni.recargar_energia()

ganador2 = arena.enfrentar_aleatorio()
if ganador2 and isinstance(ganador2, (DragonSolar, BabosaToxica, RobotOmega)):
    LOG_FUNCTION(f"\n[Arena] GANADOR DEL COMBATE 2: {ganador2.nombre} (¡ha evolucionado por ganar!)")



separator("D. LABORATORIO DE CLONACIÓN Y PRUEBA DE DEFECTOS")


Slyme_Clone = laboratorio.clonar_criatura(Slyme)
arena.registrar_criatura(Slyme_Clone)

LOG_FUNCTION("\n--- Comparativa Original vs Clon (Defecto) ---")
Slyme.mostrar_stats()
Slyme_Clone.mostrar_stats()



separator("E. BATALLA FINAL: Prueba de Clon y Encapsulación")


LOG_FUNCTION(f"Luchadores: {Slyme_Clone.nombre} vs {Omni.nombre}")
criatura1 = Slyme_Clone
criatura2 = Omni


criatura2.energia = 30
LOG_FUNCTION(f"\n[Sistema] {criatura2.nombre} empieza con energía reducida: {criatura2.energia}")


turno = 0
while criatura1.estado != "KO" and criatura2.estado != "KO" and turno < 5:
    turno += 1
    LOG_FUNCTION(f"\n--- TURNO {turno} ---")
    criatura1.atacar(criatura2)
    if criatura2.estado == "KO":
        LOG_FUNCTION(f"\n[Resultado] {criatura2.nombre} en KO.")
        break
    criatura2.atacar(criatura1)



ganador_final = arena._determinar_ganador(criatura1, criatura2)

LOG_FUNCTION("\n--- FIN DEL COMBATE CON CLON ---")
if isinstance(ganador_final, (DragonSolar, BabosaToxica, RobotOmega)):
    LOG_FUNCTION(f"[Arena] GANADOR FINAL: {ganador_final.nombre}")
else:
    LOG_FUNCTION(f"[Arena] Resultado: {ganador_final}")




separator("F. ESTADISTICAS FINALES DEL SISTEMA")

Drago.mostrar_stats()
Slyme.mostrar_stats()
Omni.mostrar_stats()
Slyme_Clone.mostrar_stats()