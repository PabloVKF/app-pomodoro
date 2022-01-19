import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class HeaderFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(bootstyle=SECONDARY, *args, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        self.images = ttk.PhotoImage(
            name="logo",
            file="images/tomate_64px.png"
        )

        self.logo_image = ttk.Label(
            master=self,
            image="logo",
            bootstyle=(INVERSE, SECONDARY)
        )
        self.logo_image.pack(side=LEFT, expand=YES, padx=10)

        self.logo_text = ttk.Label(
            master=self,
            text="POMODORO",
            font=('TkDefaultFixed', 30),
            anchor=CENTER,
            bootstyle=(INVERSE, DANGER)
        )
        self.logo_text.pack(side=LEFT, expand=YES, padx=10, ipadx=20, ipady=10, fill=X)

