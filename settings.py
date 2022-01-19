import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


from data_manager import DataManager


class Settings(ttk.Toplevel):
    def __init__(self, mother, *args, **kwargs):
        super().__init__(master=mother, title="Settings", *args, **kwargs)
        self.mother = mother

        self.new_study_seconds = ttk.StringVar(value="0")
        self.new_study_seconds.set(self.mother.study_seconds)
        self.new_break_seconds = ttk.StringVar(value="0")
        self.new_break_seconds.set(self.mother.break_seconds)
        self.default_study_seconds = 1500
        self.default_break_seconds = 300
        self.data_manager = DataManager()

        container = ttk.Label(
            master=self,
            bootstyle=(INVERSE, DANGER)
        )
        container.pack(fill=BOTH, expand=YES)

        self._build_study_fild()
        self._build_break_fild()
        self._build_save_fild()

    def _build_study_fild(self) -> None:
        container = ttk.Label(
            master=self,
            bootstyle=(INVERSE, DANGER)
        )
        container.pack(fill=BOTH, expand=YES)

        self.study_time_label = ttk.Label(
            master=container,
            text="Study seconds:",
            anchor=CENTER,
            bootstyle=(INVERSE, DARK)
        )
        self.study_time_label.pack(side=LEFT, fill=BOTH, expand=YES, ipadx=10, padx=(10, 5), pady=10)

        self.study_time_spinbox = ttk.Spinbox(
            master=container,
            from_=1,
            to=90000,
            textvariable=self.new_study_seconds,
            bootstyle=DARK
        )
        self.study_time_spinbox.pack(side=LEFT, fill=X, expand=YES, padx=(10, 5), pady=10)

    def _build_break_fild(self) -> None:
        container = ttk.Label(
            master=self,
            bootstyle=(INVERSE, DANGER)
        )
        container.pack(fill=BOTH, expand=YES)

        self.break_time_label = ttk.Label(
            master=container,
            text="Break seconds:",
            anchor=CENTER,
            bootstyle=(INVERSE, DARK)
        )
        self.break_time_label.pack(side=LEFT, fill=BOTH, expand=YES, ipadx=10, padx=(10, 5), pady=10)

        self.break_time_spinbox = ttk.Spinbox(
            master=container,
            from_=1,
            to=90000,
            textvariable=self.new_break_seconds,
            bootstyle=DARK
        )
        self.break_time_spinbox.pack(side=LEFT, fill=X, expand=YES, padx=(10, 5), pady=10)

    def _build_save_fild(self) -> None:
        container = ttk.Label(
            master=self,
            bootstyle=(INVERSE, DANGER)
        )
        container.pack(fill=BOTH, expand=YES)

        self.reset_button = ttk.Button(
            master=container,
            text="Reset",
            command=self._reset_default_settings,
            bootstyle=SECONDARY
        )
        self.reset_button.pack(side=LEFT, fill=X, expand=YES, padx=(10, 5), pady=10)

        self.saves_button = ttk.Button(
            master=container,
            text="Save",
            command=self._save_data,
            bootstyle=WARNING
        )
        self.saves_button.pack(side=LEFT, fill=X, expand=YES, padx=(5, 10), pady=10)

    def _reset_default_settings(self) -> None:
        self.new_study_seconds.set(str(self.default_study_seconds))
        self.new_break_seconds.set(str(self.default_break_seconds))
        self._apply_changes()
        messagebox.showinfo("Configuração padrão salva!", "Os dados voltaram para a configuração padrão.")

    def _save_data(self) -> None:
        self._apply_changes()
        messagebox.showinfo("Dados salvos!", "Sua nova configuração foi salva!")

    def _apply_changes(self):
        study_seconds = int(self.new_study_seconds.get())
        break_seconds = int(self.new_break_seconds.get())
        self.mother.study_seconds = study_seconds
        self.mother.break_seconds = break_seconds
        new_data = {
            "study_seconds": study_seconds,
            "break_seconds": break_seconds
        }
        self.mother.reset_step()
        self.data_manager.save_data(new_data)

