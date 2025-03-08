# ui.py
from prompt_toolkit import Application
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import Button, Dialog, TextArea
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

# Definición de estilos para modo claro y oscuro
light_style = Style.from_dict({
    'dialog': 'bg:#ffffff #000000',
    'button': 'bg:#007fff #ffffff',
    'text-area': 'bg:#f0f0f0 #000000',
})
dark_style = Style.from_dict({
    'dialog': 'bg:#444444 #ffffff',
    'button': 'bg:#005f87 #ffffff',
    'text-area': 'bg:#333333 #ffffff',
})

def recipe_app():
    # Campos de entrada
    title_field = TextArea(height=1, prompt='Título: ')
    ingredients_field = TextArea(height=5, prompt='Ingredientes (una por línea): ')
    preparation_field = TextArea(height=5, prompt='Preparación: ')

    output = {}

    def accept():
        output['title'] = title_field.text.strip()
        output['ingredients'] = ingredients_field.text.strip()
        output['preparation'] = preparation_field.text.strip()
        app.exit(result=output)

    submit_button = Button(text="Crear receta", handler=accept)
    
    dialog = Dialog(
        title="Editor de Recetas",
        body=HSplit([
            title_field,
            ingredients_field,
            preparation_field,
        ]),
        buttons=[submit_button],
        with_background=True
    )

    kb = KeyBindings()
    current_style = [light_style]  # Contenedor mutable para el estilo actual

    @kb.add("f2")
    def _(event):
        # Alterna entre modo claro y oscuro
        if current_style[0] == light_style:
            current_style[0] = dark_style
        else:
            current_style[0] = light_style
        app.style = current_style[0]

    app = Application(layout=Layout(dialog),
                      key_bindings=kb,
                      style=current_style[0],
                      full_screen=True)
    result = app.run()
    return result