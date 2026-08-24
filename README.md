
## ⚙️ Configuración del entorno

1. Clonar el repositorio:
```bash
   git clone git@github.com:gustavomendoza1237-web/qa-project-Urban-Routes-es.git
   cd qa-project-Urban-Routes-es
```

2. Crear y activar entorno virtual (PowerShell):
```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
```

3. Instalar dependencias:
```bash
   pip install -r requirements.txt
```

4. **Importante:** antes de cada ejecución, regenerar la URL del servidor en `data.py`. Las URLs de los servidores de prueba de TripleTen expiran; si el test falla en el primer paso (`click_order_taxi_button`), la causa casi siempre es una sesión de servidor expirada, no un error de código.

## ▶️ Ejecución de las pruebas

Los tests no se descubren automáticamente por nombre de archivo, así que se deben correr explícitamente:

```bash
pytest -v main.py
```

Para correr una prueba específica:

```bash
pytest -v main.py -k test_request_taxi_search
```

## ✅ Casos de prueba cubiertos

- Configuración de direcciones de origen y destino
- Selección de tarifa Comfort
- Ingreso de número de teléfono
- Agregado de tarjeta de pago
- Ingreso de mensaje para el conductor
- Activación de manta y pañuelos
- Solicitud de helados
- Búsqueda y asignación del conductor (flujo completo encadenado)

## 🐞 Problemas conocidos / soluciones aplicadas

- **Overlay bloqueando clics:** resuelto con espera explícita `invisibility_of_element_located` antes de interactuar con elementos cubiertos.
- **Switch de manta y pañuelos:** el target correcto del clic es `span.slider.round`, no el contenedor `div.switch`.
- **Botón de helado:** requiere `presence_of_element_located` (20s) + clic mediante `execute_script` por comportamiento inconsistente del elemento en el DOM.
- **Modal de pago:** el botón de cierre se selecciona dinámicamente con `find_elements` + verificación `is_displayed()`, ya que su presencia en el DOM varía.
- **Asignación del conductor:** se implementó una espera activa (polling) sobre el texto del encabezado hasta confirmar la asignación.

## 👤 Autor

**Gustavo Mendoza**
Junior QA Tester en formación — TripleTen QA Engineering Bootcamp
[LinkedIn](https://www.linkedin.com/in/gustavo-6a4778402/)