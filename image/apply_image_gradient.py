import argparse
from PIL import Image

def apply_gradient(image_path, output):
    if not image_path:
        raise Exception('No se informó la ruta a la imagen')

    img = Image.open(image_path).convert("RGBA")

    # Crea una capa de degradado (transparente a blanco)
    width, height = img.size
    gradient = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    
    # Crear el degradado con más blanco al principio y transparencia al final
    for x in range(width):
        # Definir el punto donde comienza la transparencia (70% del ancho)
        alpha = 255 if x < width * 0.3 else int(255 * (1 - (x - width * 0.3) / (width * 0.7)))
        
        # Aplicar el valor de alpha calculado (más blanco al principio, más transparente al final)
        for y in range(height):
            gradient.putpixel((x, y), (255, 255, 255, alpha))
    
    img = Image.alpha_composite(img, gradient)

    img.save(output if output else "output_image.png")

def main():
    parser = argparse.ArgumentParser(description="Aplica un degradado de blanco a transparente en la imagen.")
    parser.add_argument('--image', type=str, required=True, help="Ruta a la imagen")
    parser.add_argument('--output', type=str, required=False, help="Nombre del archivo de salida")
    args = parser.parse_args()

    apply_gradient(args.image, args.output)

main()
