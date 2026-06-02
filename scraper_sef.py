import requests
from bs4 import BeautifulSoup
import json

def rastrear_sef():
    print("Iniciando el radar del SEF...")
    
    # URL del buscador de empleo del SEF (Genérica)
    url = "http://www.sef.carm.es/web/pagina?IDCONTENIDO=36&IDTIPO=100&RASTRO=c$m22849"
    
    # Nos disfrazamos de navegador normal para que el SEF no nos bloquee
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        respuesta = requests.get(url, headers=headers)
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        ofertas = []
        
        # --- AQUÍ VA LA BÚSQUEDA EXACTA EN EL HTML DEL SEF ---
        # Supongamos que cada trabajo está en una etiqueta <div> con la clase 'oferta'
        lista_ofertas = soup.find_all('div', class_='oferta')
        
        for item in lista_ofertas:
            # Extraemos el texto del enlace y la URL
            enlace_tag = item.find('a')
            if enlace_tag:
                titulo = enlace_tag.text.strip()
                enlace = "http://www.sef.carm.es" + enlace_tag['href']
                
                ofertas.append({
                    "titulo": titulo,
                    "enlace": enlace
                })
                
    except Exception as e:
        print(f"Error al conectar con el SEF: {e}")
        ofertas = []

    # --- SALVAVIDAS PARA NUESTRO PROTOTIPO ---
    # Si la estructura del SEF es distinta y no cazamos nada hoy, metemos datos de prueba
    # para que puedas ver cómo queda tu web funcionando.
    if len(ofertas) == 0:
        print("Aviso: No se pudo raspar el HTML exacto. Generando datos de prueba...")
        ofertas = [
            {"titulo": "Camarero/a para restaurante en el centro", "enlace": "http://www.sef.carm.es/"},
            {"titulo": "Programador Junior Web (Teletrabajo)", "enlace": "http://www.sef.carm.es/"},
            {"titulo": "Mozo/a de almacén - Turno de noche", "enlace": "http://www.sef.carm.es/"},
            {"titulo": "Profesor/a de inglés para academia", "enlace": "http://www.sef.carm.es/"}
        ]

    # Guardamos todo en un archivo JSON (Este es el archivo que leerá tu web)
    with open('empleos.json', 'w', encoding='utf-8') as archivo:
        json.dump(ofertas, archivo, ensure_ascii=False, indent=4)
        
    print("¡Rastreo finalizado! Se ha creado el archivo empleos.json con éxito.")

# Ejecutamos el motor
rastrear_sef()