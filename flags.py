import flet as ft


title = ft.Text(
        "",
        size=36,
        weight=ft.FontWeight.BOLD,
    )

rus = ft.Image(
    src="https://flagcdn.com/w40/ru.png",
    width=30,
    height=20,
)

us = ft.Image(
    src="https://flagcdn.com/w40/us.png",
    width=30,
    height=20,
)

progress_bar = ft.ProgressBar(width=300, color=ft.Colors.BLUE, visible=False, opacity = 1)
status_text = ft.Text("", size=14, color=ft.Colors.RED)

username_field = ft.TextField(
        label="Введите никнейм в Dota/Steam",
        width=300,
)

search_button = ft.Button(
        "Найти",
        width=200,
        height=50,
        opacity = 0,
    )

kd_button = ft.Button(
    "Hi!!",
    width=200,
    height=50,
    opacity = 1
)

pldhero_button = ft.Button(
    "Hi!! There!",
    width=200,
    height=50,
    opacity = 1
)


flag_us = ft.Container(
    content=us,
)

flag_ru = ft.Container(
    content=rus,
)

back_button = ft.IconButton(
    icon=ft.Icons.ARROW_BACK,
    icon_size=30,
)

copy_button = ft.IconButton(
    icon=ft.Icons.COPY,
    icon_size=30,
)





