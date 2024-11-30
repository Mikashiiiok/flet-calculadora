import flet
from flet import (
    Page,
    TextField,
    Row,
    Column,
    ElevatedButton,
    Text,
    MainAxisAlignment,
    CrossAxisAlignment,
    colors
)

def main(page: Page):
    page.title = "Calculadora"
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.window_width = 300
    page.window_height = 500
    page.update()

    expression = ""

    display = TextField(
        value="0",
        text_align="right",
        width=280,
        height=60,
        read_only=True,
        bgcolor=colors.WHITE,
        border_radius=10,
        color=colors.BLACK,
        text_size=24,  
    )

    def update_display():
        display.value = expression if expression else "0"
        page.update()

    def on_click(e):
        nonlocal expression
        button_text = e.control.data

        if button_text == "C":
            expression = ""
        elif button_text == "=":
            try:
                result = eval(expression)
                expression = str(result)
            except Exception as ex:
                expression = "Error"
        else:
            if expression == "Error":
                expression = ""
            expression += button_text

        update_display()

    # Define los botones
    buttons = [
        ["C", "/", "*"],
        ["7", "8", "9", "-"],
        ["4", "5", "6", "+"],
        ["1", "2", "3", "="],
        ["0", "."],
    ]

    button_rows = []
    for row in buttons:
        button_row = Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                ElevatedButton(
                    text=btn,
                    data=btn,
                    width=60,
                    height=60,
                    bgcolor=colors.BLUE_GREY_700,
                    color=colors.WHITE,
                    on_click=on_click,
                )
                for btn in row
            ],
            spacing=10,
        )
        button_rows.append(button_row)

    # Añade la columna con los controles
    page.add(
        Column(
            controls=[
                display,
                *button_rows,
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=10,
        )
    )

flet.app(target=main)
