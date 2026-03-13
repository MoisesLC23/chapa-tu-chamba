import requests
from bs4 import BeautifulSoup
import pandas as pd

print("¡Iniciando Chapa tu Chamba V4.0 (Datos limpios y Enlaces)!\n")

url = "https://pe.computrabajo.com/trabajo-de-ingenieria-de-sistemas"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.content, "html.parser")
    tarjetas = soup.find_all("article")
    lista_empleos = []
    
    for tarjeta in tarjetas:
        # 1. EL ENLACE Y EL TÍTULO LIMPIO
        # Buscamos la etiqueta <a> que tiene la clase 'js-o-link' (donde está el texto real)
        enlace_tag = tarjeta.find("a", class_="js-o-link")
        
        if not enlace_tag:
            continue # Si es publicidad y no tiene este enlace, pasamos de largo
            
        # El truco de limpieza: " ".join(texto.split()) borra todos los espacios gigantes y saltos de línea
        titulo = " ".join(enlace_tag.text.split())
        
        # Extraemos el 'href' y le pegamos el dominio para que el link funcione
        enlace_parcial = enlace_tag.get("href", "")
        url_empleo = f"https://pe.computrabajo.com{enlace_parcial}"
        
        # 2. LA EMPRESA Y LA UBICACIÓN
        # Vamos a buscar todos los párrafos de la tarjeta para ubicarnos mejor
        parrafos = tarjeta.find_all("p")
        empresa = "Confidencial"
        ubicacion = "No especificada"
        
        if len(parrafos) > 0:
            # El primer párrafo suele tener a la empresa
            empresa = " ".join(parrafos[0].text.split())
            
        if len(parrafos) > 1:
            # El segundo párrafo suele tener la ubicación real
            ubicacion = " ".join(parrafos[1].text.split())
            
        lista_empleos.append({
            "Puesto": titulo,
            "Empresa": empresa,
            "Ubicación": ubicacion,
            "Enlace": url_empleo
        })
        
    print(f"¡Se encontraron {len(lista_empleos)} ofertas!")
    
    if len(lista_empleos) > 0:
        tabla_datos = pd.DataFrame(lista_empleos)
        tabla_datos.to_excel("computrabajo_limpio.xlsx", index=False)
        print("\n✅ ¡Magia pura! Revisa tu nuevo archivo 'computrabajo_limpio.xlsx'.")
    else:
        print("\n⚠️ No se extrajeron datos.")

else:
    print(f"Error al conectar. Código: {respuesta.status_code}")