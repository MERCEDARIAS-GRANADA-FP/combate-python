# app_evaristo/views.py
import requests
import json
from django.http import JsonResponse
from random import randint  # Para simular un estado de tareas dinámico

# --- DATOS LOCALES DE EVARISTO ---
# En un entorno real, esto vendría de una base de datos.
TAREAS_PENDIENTES = randint(1, 15)

# URLs de los compañeros (Basadas en el ejemplo del enunciado)
URL_MANU_STATUS = "http://manu.local:5001/status"
URL_MARTINA_STATUS = "http://martina.local:5003/status"


## 🟢 Endpoint 1: /status
def status_endpoint(request):
    """Devuelve la información local de Evaristo (Tareas Pendientes)."""

    # 📝 Nota: TAREAS_PENDIENTES se recalcula en cada ejecución del servidor
    # o si se ejecuta esta línea en lugar de la global:
    # TAREAS_ACTUALES = randint(1, 15)

    data = {
        "tareas": TAREAS_PENDIENTES,
    }
    return JsonResponse(data)


## 🟣 Endpoint 2: /decision
def decision_endpoint(request):
    """
    Consulta a Manu y Martina, toma una decisión y la devuelve.
    """

    datos_recogidos = {}

    # 1. 📞 Llamar a Manu (Clima)
    try:
        response_manu = requests.get(URL_MANU_STATUS, timeout=2)  # Añadido timeout (Reto Extra)
        response_manu.raise_for_status()  # Lanza excepción para códigos 4xx/5xx
        datos_manu = response_manu.json()
        datos_recogidos.update(datos_manu)
    except requests.exceptions.RequestException as e:
        # Manejo de errores si Manu está caído (Reto Extra)
        datos_recogidos["clima"] = "ERROR: Manu no responde"
        print(f"Error al conectar con Manu: {e}")

    # 2. 📞 Llamar a Martina (Estado del Servidor)
    try:
        response_martina = requests.get(URL_MARTINA_STATUS, timeout=2)
        response_martina.raise_for_status()
        datos_martina = response_martina.json()
        datos_recogidos.update(datos_martina)
    except requests.exceptions.RequestException as e:
        # Manejo de errores si Martina está caída (Reto Extra)
        datos_recogidos["servidor_ok"] = "ERROR: Martina no responde"
        print(f"Error al conectar con Martina: {e}")

    # 3. 🧠 Tomar la Decisión Final (Lógica de Evaristo)
    decision = Evaristo_toma_decision(datos_recogidos)

    # 4. 📤 Devolver la respuesta
    final_response = {
        "servicio_propio": "Evaristo - Tareas Pendientes",
        "decision": decision,
        "datos_recogidos": datos_recogidos,
    }

    return JsonResponse(final_response, json_dumps_params={'indent': 4})


def Evaristo_toma_decision(datos):
    """Lógica personalizada de Evaristo."""

    # Variables de estado
    clima = datos.get("clima", "desconocido")
    servidor_ok = datos.get("servidor_ok", False)
    tareas = TAREAS_PENDIENTES  # Evaristo usa su propio estado de tareas

    # --- Lógica de Decisión ---

    # 1. Prioridad: ¿El servidor está caído?
    if servidor_ok != True:
        return f"¡Alerta! Martina reporta un fallo de servidor. Con {tareas} tareas pendientes, el equipo debe enfocarse **SÓLO** en corregir el problema. ¡Todo lo demás, PAUSA! 🚨"

    # 2. Prioridad: ¿Muchas tareas?
    if tareas > 10:
        return f"¡Tenemos {tareas} tareas acumuladas! No importa el clima, la orden es: **Máxima concentración y cero distracciones**. Café y a trabajar duro. ☕️"

    # 3. Lógica normal (Servidor OK y Tareas manejables)
    if clima == "soleado" and tareas <= 5:
        return f"Día perfecto: Sol y solo {tareas} tareas. ¡Decisión: **Trabajo flexible o fuera de la oficina**! La productividad va a tope. 😎"
    elif clima == "lluvia" and tareas <= 5:
        return f"El clima está para quedarse en casa ({clima}). Con solo {tareas} tareas, es un día ideal para **trabajo remoto tranquilo y creativo**. 🌧️"
    elif clima == "viento" or tareas > 5:
        return f"El viento (o las {tareas} tareas) no dan tregua. Decisión: **Presencial obligatorio** para coordinación rápida y evitar malentendidos. A trabajar. 💻"
    else:
        # Para el resto de casos (nublado, desconocido, etc.)
        return f"Situación neutra ({clima}, {tareas} tareas). Decisión: Mantenemos el **protocolo estándar de oficina** y monitoreamos el clima y el progreso. ⚖️"