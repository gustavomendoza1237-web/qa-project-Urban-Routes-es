# Urban Routes — Automatización de pruebas end-to-end (Selenium + pytest)

Suite de pruebas automatizadas que valida, de principio a fin, el flujo de pedir un taxi en **Urban Routes**, una aplicación web de planificación de rutas y solicitud de viajes. Proyecto desarrollado en el QA Engineering Bootcamp de TripleTen.

## 🎯 Contexto y objetivo

Pedir un taxi en Urban Routes implica varios pasos encadenados: definir la ruta, elegir la tarifa, confirmar el teléfono, agregar un método de pago y configurar el viaje. Si uno solo falla, el usuario no puede completar el pedido y la empresa pierde el viaje.

El objetivo fue automatizar ese recorrido para verificar, de forma repetible, que cada paso funciona y que el pedido termina con un conductor asignado.

## 👤 Mi contribución

Proyecto individual. Me encargué de:

- Analizar el flujo de la aplicación y definir qué validar en cada paso.
- Identificar los elementos de la interfaz y construir localizadores estables.
- Escribir las 8 pruebas y organizar el código con **Page Object Model**.
- Resolver los problemas de sincronización que hacían fallar las pruebas de forma intermitente.
- Refactorizar el código según la revisión de código por pares (separación en capas, esperas explícitas y `requirements.txt`).

## 🧪 Qué se valida y por qué importa

| # | Prueba | Riesgo que cubre |
|---|---|---|
| 1 | Configurar origen y destino | Sin una ruta correcta no existe un viaje válido |
| 2 | Seleccionar la tarifa Comfort | El precio y las opciones dependen de la tarifa elegida |
| 3 | Ingresar y confirmar el número de teléfono | El conductor necesita contactar al usuario |
| 4 | Agregar una tarjeta de pago | Sin método de pago el pedido no se puede cobrar |
| 5 | Escribir un mensaje para el conductor | Las indicaciones del usuario deben llegar al conductor |
| 6 | Activar manta y pañuelos | Los extras solicitados deben quedar registrados |
| 7 | Pedir dos helados | El contador de extras debe reflejar la cantidad correcta |
| 8 | Buscar y asignar conductor (flujo completo) | Confirma que todo el recorrido termina en un viaje real |

## ⚙️ Metodología y herramientas

- **Python + Selenium WebDriver** para interactuar con la aplicación como lo haría un usuario.
- **pytest** para organizar y ejecutar las pruebas.
- **Page Object Model:** los localizadores y las acciones de la página viven en `pages.py`, las funciones auxiliares en `helpers.py` y las pruebas en `main.py`. Así, si cambia la interfaz, solo se ajusta un lugar.
- **Esperas explícitas (`WebDriverWait`)** en lugar de pausas fijas, para que las pruebas sean estables y no dependan de la velocidad de carga.

## ✅ Resultados

- **8 de 8 pruebas superadas** en la versión final.
- Código refactorizado y aprobado tras la revisión de código.

Problemas técnicos que resolví durante la automatización:

- **Overlay que bloqueaba los clics:** esperar a que el overlay desaparezca (`invisibility_of_element_located`) antes de interactuar.
- **Switch de manta y pañuelos:** el clic correcto va sobre `span.slider.round`, no sobre el contenedor del switch.
- **Botón de helado inconsistente:** espera de presencia y clic mediante `execute_script`.
- **Modal de pago variable:** el botón de cierre se localiza dinámicamente y se verifica que esté visible antes de usarlo.
- **Asignación del conductor:** espera activa sobre el texto del encabezado hasta confirmar que el conductor fue asignado.

## 📎 Evidencias

- Código de las pruebas: [`main.py`](main.py)
- Page Object de la aplicación: [`pages.py`](pages.py)
- Historial de cambios tras la revisión de código: [commits del repositorio](../../commits)

## ▶️ Configuración y ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/gustavomendoza1237-web/qa-project-Urban-Routes-es.git
   cd qa-project-Urban-Routes-es
   ```
2. Crear y activar un entorno virtual (PowerShell):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Actualizar la URL del servidor en `data.py`. Los servidores de práctica de TripleTen expiran; si la primera prueba falla al pedir el taxi, la causa suele ser una sesión de servidor vencida, no un error del código.
5. Ejecutar todas las pruebas:
   ```bash
   pytest -v main.py
   ```
   O una prueba específica:
   ```bash
   pytest -v main.py -k test_request_taxi_search
   ```

## 👤 Autor

**Gustavo Buitrago Mendoza** — QA Tester
[LinkedIn](https://www.linkedin.com/in/gustavo1111/) · [Perfil de GitHub](https://github.com/gustavomendoza1237-web)
