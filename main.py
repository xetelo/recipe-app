# main.py
from ui import recipe_app
from doc_generator import create_recipe_docx

def main():
    data = recipe_app()
    if data:
        create_recipe_docx(data['title'], data['ingredients'], data['preparation'])
        print("El archivo 'receta.docx' ha sido creado exitosamente.")

if __name__ == "__main__":
    main()
