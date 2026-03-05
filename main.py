import flet as ft
def main(page: ft.Page):
    page.title = "Registro De Participantes"
    txt_nombre = ft.TextField(
        label="Nombre Participante",
        width=400
    )
    txt_correo = ft.TextField(
        label="correo electronico",
        width=400
    )
    dropdown_tipo = ft.Dropdown(
        label="Taller de intereses",
        width=300,
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ]
    )
    radio_modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Pago Completo", label="Pago Completo"),
            ft.Radio(value="Pago con cuotas", label="Pago con cuotas"),
        ])
    )
    check_requerimiento = ft.Checkbox(
        label="Requiere computadora portátil"
        )
    slider_experiencia = ft.Slider(
        min=1,
        max=5,
        divisions=4,
        label="{value} Nivel de Experiencia",
        value=1
    )
    txt_resumen = ft.Text(
        value="Resumen",
        size=16
    )
    def mostrar_resumen(e):
    
        nombre = txt_nombre.value
        correo =  txt_correo.vaule
        tipo = dropdown_tipo.value
        modalidad = radio_modalidad.value
        requerimiento = "Sí" if check_requerimiento.value else "No"
        experiencia = slider_experiencia.value
        resumen = f"""
        Nombre: {nombre}
        correo: {correo}
        Tipo: {tipo}
        Modalidad: {modalidad}
        computadora portatil: {requerimiento}
        Nivel de experiencia: {experiencia} 
        """
        txt_resumen.value = resumen
        page.update()
    btn_resumen = ft.ElevatedButton(
        content=ft.Text("Mostrar resumen"),
        on_click=mostrar_resumen
)
    page.add(
        ft.Text("Registro de Participantes", size=24, weight="bold"),
        txt_nombre,
        txt_correo,
        dropdown_tipo,
        ft.Text(""),
        radio_modalidad,
        check_requerimiento,
        ft.Text(""),
        slider_experiencia,
        btn_resumen,
        ft.Divider(),
        txt_resumen
    )

ft.app(target=main)