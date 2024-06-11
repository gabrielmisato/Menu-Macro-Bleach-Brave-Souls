import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import threading
from macros.story import start_macro as story
from macros.evento_pontos import start_macro as ep

def run_macro(macro_function):
    thread = threading.Thread(target=macro_function)
    thread.daemon = True
    thread.start()

root = ttk.Window(themename='darkly')
root.geometry("500x350")


storyButton = ttk.Button(root, text='Story', command=lambda: run_macro(story), bootstyle=SUCCESS)
eventoPontosButton = ttk.Button(root, text='Evento de Pontos', command=lambda: run_macro(ep), bootstyle=SUCCESS)
sairButton = ttk.Button(root, text='Sair', command=root.quit, bootstyle=DANGER)

storyButton.pack(pady=20)
eventoPontosButton.pack()
sairButton.pack(pady=20)

root.mainloop()
