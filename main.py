import flet as ft
import asyncio
import requests
from flags import flag_ru, flag_us, username_field, status_text, progress_bar, back_button, copy_button, search_button
from localization import t, set_lang

def main(page: ft.Page):
    page.title = "Dota Stats"
    page.window_width = 800
    page.window_height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    search_button.on_click = lambda e: page.run_task(handle_search, username_field.value, status_text, progress_bar, search_button, title, username_field, t)

    def update_ui():
        username_field.label = t('username_field')
        title.value = t('title')
        search_button.content= t('search_button')
        page.update()
    

    def translate_us(e):     
        set_lang('en')
        update_ui()

    def translate_ru(e):
        set_lang('ru')
        update_ui()
        
    
    flag_ru.on_click = translate_ru
    flag_us.on_click = translate_us



    def clear():
        page.controls.clear()

    def show_search():
        clear()


        page.add(
            ft.Column(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                title,
                                ft.Container(height=30),
                                username_field,
                                ft.Container(height=10),
                                search_button,
                                status_text,
                                progress_bar
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        expand=True
                    ),
                    ft.Row(
                        [
                            flag_ru,
                            flag_us
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.END,
                        alignment=ft.MainAxisAlignment.END
                    )
                ],
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

        async def intro(search_button, title, username_field, status_text):
            for x in range(0, 98, 4):
                title.opacity = x / 100
                username_field.opacity = x / 100
                status_text.opacity = x / 100
                search_button.opacity = x / 100
                await asyncio.sleep(0.03)
                page.update()
        
        asyncio.create_task(intro(search_button, title, username_field, status_text))

    async def handle_search(username, status_text, progress_bar, search_button, title, username_field, t):
        if not username:
            status_text.value = t('status_text')
            page.update()
            return

        status_text.value = t('status_finding')

        progress_bar.visible = True
        page.update()

        async def outro(search_button, title, username_field, status_text, progress_bar):
            for x in range(100, -1, -4):
                title.opacity = x / 100
                username_field.opacity = x / 100
                status_text.opacity = x / 100
                search_button.opacity = x / 100
                progress_bar.opacity = x / 100

                await asyncio.sleep(0.03)
                page.update()



        try:
            search_response = await asyncio.to_thread(requests.get, f"https://api.opendota.com/api/search?q={username}")
            status_text.value = t("status_finish")
            search_data = search_response.json()
        except Exception as b:
            status_text.value = t("status_error_failed")
            progress_bar.visible = False
            page.update()
            await asyncio.sleep(8)
            status_text.value = ""
            page.update()
            return
        
        if not search_data:
            status_text.value = t("status_error_not_found")
            progress_bar.visible = False
            page.update()
            await asyncio.sleep(3)
            status_text.value = ""
            page.update()
            return

        account_id = search_data[0]['account_id']

        matches_response = requests.get(f"https://api.opendota.com/api/players/{account_id}/matches")
        matches_data = matches_response.json()

        if not matches_data:
            status_text.value = t("status_error_not_found_matches")
            progress_bar.visible = False
            page.update()
            await asyncio.sleep(3)
            status_text.value = ""
            page.update()
            return

        await outro(search_button, title, username_field, status_text, progress_bar)
        status_text.value = ""
        progress_bar.visible = False 
        show_stats(account_id, matches_data, search_data)

    def show_stats(account_id, matches_data, search_data):
        clear()


        async def set_clipboard(e):
            await ft.Clipboard().set(str(account_id))
        
        copy_button.on_click=set_clipboard

        icon = ft.Image(
            src=f"{search_data[0]['avatarfull']}",
            width=100,
            height=100,
        )

        matches_count = len(matches_data)
        
        txt_info = t('info').format(account_id=account_id, matches_data=matches_count)

        info = ft.Text(
            f"{txt_info}",
            size=20,
            text_align=ft.TextAlign.CENTER,
        )

        name_text = ft.Text(f"{search_data[0]['personaname']}", size=20)

        content = ft.Column(
            controls=[
                ft.Row(
                    controls=[back_button],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                icon,
                                ft.Container(width=15),
                                ft.Column(             
                                    controls=[
                                        name_text,
                                        ft.Container(height=15),
                                        info     
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=2
                                ),
                                ft.Container(width=10),
                                copy_button
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            opacity=0,
        )

        page.add(content)
        page.update()

        async def fade_in():
            for step in range(0, 101, 4):  
                content.opacity = step / 100
                await asyncio.sleep(0.02)
                page.update()

        asyncio.create_task(fade_in())


        async def handle_back():
            for step in range(100, -1, -4):
                content.opacity = step / 100
                await asyncio.sleep(0.02)
                page.update()
            show_search()

        back_button.on_click = lambda e: asyncio.create_task(handle_back())
    show_search()


ft.run(main)