import datetime
import time


class CountdownTimerError(Exception):
    """Custom exceptions"""


class CountdownTimer:
    def __init__(self, init_seconds: int):
        self._init_seconds: int = init_seconds
        self._times_left: int = self._init_seconds
        self._last_brak_time: float = float()
        self._is_running: bool = False

    @property
    def is_running(self):
        return self._is_running

    def time_left(self) -> str:
        self._drop_elapsed_time()
        return str(datetime.timedelta(seconds=self._times_left))

    def start(self) -> None:
        self._last_brak_time = int(time.perf_counter())
        self._is_running = True

    def pause(self) -> None:
        self._drop_elapsed_time()
        self._is_running = False

    def reset(self) -> None:
        self._times_left = self._init_seconds

    def _drop_elapsed_time(self) -> None:
        elepsed_time = self._elepsed_time()
        times_up: bool = elepsed_time > self._times_left
        if times_up:
            self._times_left = 0.0
            raise CountdownTimerError("Tempo esgotado!")
        else:
            self._times_left -= elepsed_time

    def _elepsed_time(self):
        if self._is_running:
            current_time = time.perf_counter()
            elepsed_time = int(current_time - self._last_brak_time)
            self._last_brak_time = current_time
        else:
            elepsed_time = 0

        return elepsed_time


if __name__ == "__main__":
    countdown = CountdownTimer(start_seconds=1500)
    print(countdown.time_left())
    countdown.start()
    countdown.stop()
    print(countdown.time_left())
    print(countdown.time_left())
    countdown.start()
    countdown.stop()
    print(countdown.time_left())

