import re
import csv

# Función para cargar el archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

# Extraer nombres de productos y URLs de imágenes
def extraer_productos(html):
    productos = []

    # Expresión regular para los nombres de productos
    regex_nombre = re.compile(r'<span class="a-size-base-plus[^"]*">(.*?)</span>')
    # Expresión regular para las imágenes (URLs)
    regex_imagen = re.compile(r'<img[^>]+src="(https://[^"]+)"[^>]+class="[^"]*_cDEzb_image_[^"]*"')

    nombres = regex_nombre.findall(html)
    imagenes = regex_imagen.findall(html)

    # Emparejar nombres con imágenes (asumiendo que están en el mismo orden en el HTML)
    for nombre, imagen in zip(nombres, imagenes):
        productos.append((nombre.strip(), imagen))

    return productos

# Exportar resultados a CSV
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del Producto", "URL de la Imagen"])
        writer.writerows(productos)

# Ejecutar el script
archivo_html = "amazon.html"
archivo_salida = "productos_amazon.csv"

html = cargar_html(archivo_html)
productos = extraer_productos(html)
exportar_csv(productos, archivo_salida)

print(f"Se han exportado {len(productos)} productos a {archivo_salida}")
