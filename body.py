from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import datetime


from timer import CountdownTimer, CountdownTimerError
from settings import Settings
from data_manager import DataManager


class BodyFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(bootstyle=DANGER, *args, **kwargs)
        self.pack(fill=BOTH, expand=YES)
        self._is_study_time = True
        self.data_manager = DataManager()
        self.study_seconds = self.data_manager.study_seconds
        self.break_seconds = self.data_manager.break_seconds

        self.countdown = CountdownTimer(self.study_seconds)
        self.running = ttk.BooleanVar(value=False)
        self.after_id = ttk.StringVar()
        self.elapsed = ttk.IntVar(value=self.study_seconds)
        self.stopwatch_text = ttk.StringVar(value=self.countdown.time_left())
        self.completed_rounds = 0
        self.tomato_counter = []

        self.images = [
            ttk.PhotoImage(
                name="tomato_counter_BW",
                file="images/tomate_BW_32px.png"
            ),
            ttk.PhotoImage(
                name="tomato_counter",
                file="images/tomate_32px.png"
            )
        ]

        self.build_mode_field()
        self.build_stopwatch_field()
        self.build_tomato_counter_field()

    def build_mode_field(self):
        container = ttk.Frame(master=self, bootstyle=DANGER)
        container.pack(fill=BOTH, expand=YES)

        self.mode_label = ttk.Label(
            master=container,
            text="Study time",
            font="-size 32",
            anchor=CENTER,
            bootstyle=(INVERSE, WARNING)
        )
        self.mode_label.pack(pady=(50, 20), ipadx=20)

    def build_stopwatch_field(self):
        container = ttk.Frame(master=self, bootstyle=DANGER)
        container.pack(fill=BOTH, expand=YES)

        self.stopwatch_label = ttk.Label(
            master=self,
            font="-size 64",
            anchor=CENTER,
            bootstyle=(INVERSE, DANGER),
            textvariable=self.stopwatch_text
        )
        self.stopwatch_label.pack(in_=container, side=TOP, fill=X, padx=20, pady=(0, 30))

        self.start_pause_button = ttk.Button(
            master=self,
            text="Start",
            command=self._start_pause_stopwatch,
            bootstyle=WARNING
        )
        self.start_pause_button.pack(in_=container, side=LEFT, expand=YES, fill=X, padx=10, pady=10)

        self.reset_button = ttk.Button(
            master=self,
            text="Reset",
            command=self.reset_step,
            bootstyle=SECONDARY
        )
        self.reset_button.pack(in_=container, side=LEFT, expand=YES, fill=X, padx=10, pady=10)

        self.config_button = ttk.Button(
            master=self,
            text="Config",
            command=self._open_config_window,
            bootstyle=SECONDARY
        )
        self.config_button.pack(in_=container, side=LEFT, expand=YES, fill=X, padx=10, pady=10)

    def build_tomato_counter_field(self):
        container = ttk.Frame(master=self, bootstyle=SECONDARY)
        container.pack(fill=BOTH, expand=YES, padx=10, pady=(0, 10))

        self.counter_label = ttk.Label(
            master=self,
            text="Counter:",
            font="-size 24",
            anchor=CENTER,
            bootstyle=(INVERSE, SECONDARY)
        )
        self.counter_label.pack(in_=container, side=LEFT, ipadx=10, ipady=10)

        for tomato in range(4):
            if tomato < self.completed_rounds:
                image_name = "tomato_counter"
            else:
                image_name = "tomato_counter_BW"

            self.tomato_counter.append(
                ttk.Label(
                    master=self,
                    image=image_name,
                    bootstyle=(INVERSE, SECONDARY)
                )
            )

        for tomato_intance in self.tomato_counter:
            tomato_intance.pack(in_=container, side=LEFT, expand=YES)

    def _start_pause_stopwatch(self):
        if self.countdown.is_running:
            self.pause()
        else:
            self.start()

    def start(self):
        self.countdown.start()
        self.reset_button.configure(state=DISABLED)
        self.start_pause_button.configure(bootstyle=SECONDARY, text="Pause")

        self.after_id.set(self.after(1, self.increment))

    def pause(self):
        self.countdown.pause()
        self.reset_button.configure(state=NORMAL)
        self.start_pause_button.configure(bootstyle=WARNING, text="Start")

        self.after_cancel(self.after_id.get())

    def increment(self):
        try:
            time_left = self.countdown.time_left()
            self.stopwatch_text.set(time_left)
            self.after_id.set(self.after(1000, self.increment))
        except CountdownTimerError:
            self._times_up()

    def _times_up(self):
        if self._is_study_time:
            self._study_time_is_up()
        else:
            self._break_time_is_up()

    def _study_time_is_up(self):
        self.completed_rounds += 1
        tomato_instance: ttk.Label = self.tomato_counter[self.completed_rounds - 1]
        tomato_instance.configure(image="tomato_counter")
        if self.completed_rounds == 4:
            self._study_is_complete()
        else:
            self.start_pause_button.configure(bootstyle=WARNING, state=NORMAL, text="Start")
            self.reset_button.configure(state=NORMAL)
            self.mode_label.configure(bootstyle=(INVERSE, PRIMARY), text="Break time")
            self._is_study_time = False
            self.reset_step()
            messagebox.showinfo("Parabéns!!!", "Você completou o tempo de estudo, aproveite para descansar!")

    def _break_time_is_up(self):
        self.start_pause_button.configure(bootstyle=WARNING, state=NORMAL, text="Start")
        self.reset_button.configure(state=NORMAL)
        self.mode_label.configure(bootstyle=(INVERSE, WARNING), text="Study time")
        self._is_study_time = True
        self.reset_step()
        messagebox.showinfo("Bora focar de novo?", "O tempo de descanso acabou! Siga no foco, você consegue!")

    def reset_step(self):
        if self._is_study_time:
            self.countdown = CountdownTimer(init_seconds=self.study_seconds)
        else:
            self.countdown = CountdownTimer(init_seconds=self.break_seconds)
        self.stopwatch_text.set(value=self.countdown.time_left())

    def _study_is_complete(self):
        self.start_pause_button.configure(state=DISABLED)
        self.reset_button.configure(state=DISABLED)
        self.config_button.configure(state=DISABLED)
        self.mode_label.configure(bootstyle=(INVERSE, SUCCESS), text="Complete!")
        messagebox.showinfo("Estudos concluídos!!!", "Parabéns por completar seus estudos. Agora descanse para que possa absorvê-los melhor!")

    def _open_config_window(self):
        self.settings = Settings(mother=self)
        self.settings.place_window_center()
        self.settings.iconbitmap("images/tomate_icon.ico")
