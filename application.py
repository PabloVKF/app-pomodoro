import ttkbootstrap as ttk
from ttkbootstrap.constants import *


from header import HeaderFrame
from body import BodyFrame


class Application(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        self.header_frame = HeaderFrame(
            master=self,
            padding=20
        )

        self.body_frame = BodyFrame(
            master=self
        )
