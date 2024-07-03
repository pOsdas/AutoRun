import asyncio

import flet as ft
import subprocess
import json
import os
import sys
import pyautogui
import time
import pygetwindow as gw


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


config_file = 'config.json'


def load_config():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    else:
        return {'genshin': '', 'honkai': '', 'wait_time': 45}


def save_config(configs):
    with open(config_file, 'w') as f:
        json.dump(configs, f)


config = load_config()
path_genshin = config['genshin']
path_honkai = config['honkai']
wait_time = config['wait_time']


async def run_launcher_h(path):
    await asyncio.create_task(run_as_admin_honkai(path))


async def run_launcher_g(path):
    await asyncio.create_task(run_as_admin_genshin(path))


async def run_as_admin_genshin(path):
    if path:
        minimize_app_window()
        subprocess.Popen([path], shell=True)
    else:
        print("Путь к Genshin Impact не задан!")


async def run_as_admin_honkai(path):
    if path:
        minimize_app_window()
        subprocess.Popen([path], shell=True)
    else:
        print("Путь к Honkai Star Rail не задан!")


def minimize_app_window():
    current_window = gw.getWindowsWithTitle("Game Launcher")[0]
    current_window.minimize()


def main(page: ft.Page):
    """ UI (User Interface) """
    page.title = "Game Launcher"
    page.bgcolor = ft.colors.TRANSPARENT

    page.window_width = 450
    page.window_height = 800
    page.window_resizable = False
    page.window_maximizable = False

    page.window_top = 120
    page.window_left = 735

    colored_background = ft.Container(
        width=450,
        height=800,
        bgcolor=ft.colors.BLUE_GREY_600,
        padding=0,
        margin=0
    )

    genshin_path = ft.TextField(label="Путь к Genshin Impact", value=path_genshin, width=400)
    honkai_path = ft.TextField(label="Путь к Honkai Star Rail", value=path_honkai, width=400)
    wait_time_field = ft.TextField(label="Время ожидания (в секундах)", value=str(wait_time), width=200)

    def on_save(e):
        config['genshin'] = genshin_path.value
        config['honkai'] = honkai_path.value
        config['wait_time'] = int(wait_time_field.value)
        save_config(config)
        page.snack_bar = ft.SnackBar(ft.Text("Настройки сохранены"), open=True)
        page.update()

    def on_run_genshin(e):
        asyncio.run(run_launcher_g(genshin_path.value))
        x, y = pyautogui.size()
        wait = load_config()

        time.sleep(wait['wait_time'])
        pyautogui.click(x // 2, y // 2, 2, wait['wait_time'])
        page.update()

    def on_run_honkai(e):
        asyncio.run(run_launcher_h(honkai_path.value))
        x, y = pyautogui.size()
        wait = load_config()

        time.sleep(wait['wait_time'])
        pyautogui.click(x // 2, y // 2, 2, wait['wait_time'])
        page.update()

    save_button = ft.ElevatedButton(text="Сохранить настройки", on_click=on_save, width=220, style=ft.ButtonStyle(
        bgcolor=ft.colors.GREEN_600, color=ft.colors.WHITE))
    run_genshin_button = ft.ElevatedButton(text="Запустить Genshin", on_click=on_run_genshin, width=200, style=ft.ButtonStyle(
        bgcolor=ft.colors.YELLOW_800, color=ft.colors.WHITE))
    run_honkai_button = ft.ElevatedButton(text="Запустить Honkai", on_click=on_run_honkai, width=200, style=ft.ButtonStyle(
        bgcolor=ft.colors.INDIGO_700, color=ft.colors.WHITE))

    controls = ft.Column(
        [
            ft.Text("Настройки Launcher", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            genshin_path,
            honkai_path,
            wait_time_field,
            save_button,
            run_genshin_button,
            run_honkai_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50,
    )

    page.add(ft.Stack([colored_background, controls]))


ft.app(target=main, assets_dir="assets")


