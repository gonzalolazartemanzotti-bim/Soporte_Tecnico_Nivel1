# Chatbot IT - Soporte Técnico Nivel 1

Este proyecto es un Trabajo Práctico Integrador para la Tecnicatura Universitaria en Programación a Distancia (UTN). Consiste en la simulación de un chatbot de Soporte Técnico diseñado para automatizar la atención de Nivel 1.

## Objetivo del Proyecto
Automatizar el registro y seguimiento de solicitudes administrativas de IT (restablecimiento de contraseñas y desbloqueo de cuentas), conectando el modelo de procesos de negocio (BPMN 2.0) con estructuras de código lógicas.

## Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Persistencia de Datos:** Archivo local JSON (`tickets.json`) para simular la base de datos de los incidentes.
* **Interfaz:** Simulador de terminal (CLI) con máquina de estados.

## Características Principales
1. **Máquina de Estados:** El sistema recuerda el ciclo de vida del ticket (Pendiente / Resuelta).
2. **Robustez (Camino Infeliz):** Manejo de excepciones ante entradas de datos no válidas (ej. texto en lugar de números).
3. **Decisiones Dinámicas:** Uso de compuertas lógicas (Gateways) para definir si la resolución del ticket se ejecuta mediante un script automático o si escala a un técnico humano.

## Cómo desplegar y ejecutar el simulador
1. Clonar este repositorio en tu máquina local.
2. Asegúrate de tener instalado **Python 3.8 o superior**.
3. No requiere librerías externas (solo utiliza los módulos nativos `json`, `os` y `random`).
4. Abrí una terminal o consola de comandos en la carpeta del proyecto.
5. Ejecutá el script principal con el siguiente comando:
   ```bash
   python bot.py
