import tkinter as tk
from tkinter import PhotoImage
import pygame
import time
import customtkinter as ctk
import sys
from save import load_state, save_state

class GameState:
    def __init__(self):
        state = load_state()
        self.counter = state['counter']
        self.multiplier = state['multiplier']
        self.upgrade_cost = state['upgrade_cost']
        self.click_time = 0

    def save(self):
        save_state(self.counter, self.multiplier, self.upgrade_cost)

pygame.mixer.init()
click_sound = pygame.mixer.Sound('resource/click.mp3')

def update_counter(game_state):
    counter_label.config(text=f"апельсинов: {game_state.counter}")
    upgrade_button.configure(
        state="normal" if game_state.counter >= game_state.upgrade_cost else "disabled"
    )
    game_state.save()

def increment_counter(game_state):
    current_time = time.time()
    if current_time - game_state.click_time < 0.4:
        return

    game_state.click_time = current_time
    click_sound.play()

    game_state.counter += game_state.multiplier
    update_counter(game_state)

def upgrade(game_state):
    game_state.counter -= game_state.upgrade_cost
    game_state.multiplier *= 2
    game_state.upgrade_cost *= 2
    update_counter(game_state)

game_state = GameState()

root = tk.Tk()
root.title("Orange Click")
root.geometry('600x800')
root.iconbitmap(default=sys.executable)
root.resizable(False, False)
root.configure(bg='#AEC09A')

image = PhotoImage(file="resource/orange.png")
click_button = tk.Button(
    root,
    image=image,
    command=lambda: increment_counter(game_state),
    borderwidth=0,
    bg='#AEC09A',
    activebackground='#AEC09A'
)
click_button.pack(pady=20)

counter_label = tk.Label(
    root,
    text="апельсинов: 0",
    font=("Roboto", 50, "bold"),
    bg='#AEC09A',
    fg='white'
)
counter_label.pack(pady=20)

upgrade_button = ctk.CTkButton(
    root,
    text="Улучшить клик",
    command=lambda: upgrade(game_state),
    fg_color='#ffaf47',
    hover_color='#f7a943',
    text_color='white',
    font=("Roboto", 40, "bold"),
    width=360,
    height=100,
    state="disabled"
)
upgrade_button.pack(pady=25)

root.mainloop()