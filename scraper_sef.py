import requests
from bs4 import BeautifulSoup
import json

def rastrear_sef():
    print("Iniciando el radar del SEF...")
    
    # URL del buscador de empleo del SEF (Búsqueda general de toda la Región)
    url = "http://www.sef.carm.es/web/pagina?IDCONTENIDO=36&IDTIPO=100&RASTRO=c$m22849"
    
    # Nos disfrazamos de navegador normal para que el SEF no nos bloquee
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        respuesta = requests.get(url, headers=headers)
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        ofertas = []
        
        # --- AQUÍ VA LA BÚSQUEDA EXACTA EN EL HTML DEL SEF ---
        # (Dependerá de cómo estructuren ellos su web, por ahora buscamos div.oferta)
        lista_ofertas = soup.find_all('div', class_='oferta')
        
        for item in lista_ofertas:
            enlace_tag = item.find('a')
            if enlace_tag:
                titulo = enlace_tag.text.strip()
                enlace = "http://www.sef.carm.es" + enlace_tag['href']
                
                # En un caso real, aquí buscaríamos también la etiqueta HTML donde ponga el pueblo
                # municipio_tag = item.find('span', class_='localidad') ...
                
                ofertas.append({
                    "titulo": titulo,
                    "enlace": enlace,
                    "municipio": "Murcia" # Placeholder temporal en el scrap real
                })
                
    except Exception as e:
        print(f"Error al conectar con el SEF: {e}")
        ofertas = []

    # --- SALVAVIDAS PARA NUESTRO PROTOTIPO ---
    # Al no conectar todavía con la estructura real del SEF, inyectamos estas 
    # ofertas falsas preparadas con los nombres de las ciudades para que 
    # puedas probar que el menú desplegable de tu web funciona a la perfección.
    if len(ofertas) == 0:
        print("Aviso: No se pudo raspar el HTML exacto. Generando datos de prueba para el filtro...")
        ofertas = [
            {
                "titulo": "Camarero/a para restaurante en Murcia Centro", 
                "enlace": "http://www.sef.carm.es/",
                "municipio": "Murcia"
            },
            {
                "titulo": "Programador Junior Web", 
                "enlace": "http://www.sef.carm.es/",
                "municipio": "Cartagena"
            },
            {
                "titulo": "Mozo/a de almacén - Turno de noche en Lorca", 
                "enlace": "http://www.sef.carm.es/",
                "municipio": "Lorca"
            },
            {
                "titulo": "Profesor/a de inglés para academia", 
                "enlace": "http://www.sef.carm.es/",
                "municipio": "Molina"
            },
            {
                "titulo": "Administrativo/a con idiomas", 
                "enlace": "http://www.sef.carm.es/",
                "municipio": "Murcia"
            }
        ]

    # Guardamos todo en un archivo JSON (Este es el archivo que leerá tu web)
    with open('empleos.json', 'w', encoding='utf-8') as archivo:
        json.dump(ofertas, archivo, ensure_ascii=False, indent=4)
        
    print("¡Rastreo finalizado! Se ha creado el archivo empleos.json con éxito.")

# Ejecutamos el motor
rastrear_sef()