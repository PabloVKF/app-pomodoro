from tkinter import messagebox
import ttkbootstrap as ttk

from application import Application


def on_closing():
    if messagebox.askyesno("Sair", "Você deseja sair?"):
        raise SystemExit


if __name__ == "__main__":
    root = ttk.Window(
        title="Pomodoro",
        themename="litera",
        resizable=(False, False)
    )
    root.iconbitmap("images/tomate_icon.ico")
    root.protocol("WM_DELETE_WINDOW", on_closing)

    Application(root)
    root.place_window_center()

    root.mainloop()
