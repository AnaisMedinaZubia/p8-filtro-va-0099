# Medina Anais NC 0099 
import cv2
from pathlib import Path

# Ubicación de este archivo Python
BASE_DIR = Path(__file__).resolve().parent

# Ubicación de la imagen
ruta_imagen = BASE_DIR.parent / "imagenes" / "tucan.jpg"

# Cargar la imagen
imagen = cv2.imread(str(ruta_imagen))

# Comprobar que la imagen fue cargada
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    print("Ruta buscada:", ruta_imagen)
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes
bordes = cv2.Canny(gris, 100, 200)

# Mostrar resultados
cv2.imshow("Imagen original Medina Anais 0099", imagen)
cv2.imshow("Imagen en escala de grises Medina Anais 0099", gris)
cv2.imshow("Bordes Canny Medina Anais 0099", bordes)

# Guardar resultado
ruta_resultado = BASE_DIR.parent / "resultados" / "ejemplo_canny.jpg"
cv2.imwrite(str(ruta_resultado), bordes)

print("Detección de bordes completada.")
print("Resultado guardado en:", ruta_resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Medina Anais NC 0099")