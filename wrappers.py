import time
from typing import Callable, Any


def timed_method(method: Callable[..., Any]):
    """
    Wrapper that adds a timer to the wrapped function.
    """
    def interval_ns_to_str(start_time: float, end_time: float) -> str:
        interval = end_time - start_time

        if interval < 1e3:
            return f"{round(interval)}ns"
        elif interval < 1e6:
            return f"{round(interval/1e3)}µs"
        elif interval < 1e9:
            return f"{round(interval/1e6)}ms"
        else:
            return f"{round(interval/1e9)}s"

    def wrapper(*args, **kw):
        start_time = time.perf_counter_ns()
        result = method(*args, **kw)
        end_time = time.perf_counter_ns()

        print(f"Calling {method.__name__} took {interval_ns_to_str(start_time, end_time)}\n")
        return result

    return wrapper