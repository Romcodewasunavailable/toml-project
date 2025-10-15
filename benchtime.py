"""Module for keeping track of function execution times

Created on 2025.10.01
Contributors:
    Romain
"""

from __future__ import annotations
from copy import deepcopy
from functools import wraps
from time import time
from typing import Callable


def create_bench() -> tuple[Callable, ...]:
    """Closure for managing stored execution times"""
    cache = {}

    def get_cache() -> dict[str, list[float]]:
        return deepcopy(cache)

    def add_value(name: str, time: float) -> None:
        if name in cache:
            cache[name].append(time)
        else:
            cache[name] = [time]

    def clear_cache() -> None:
        cache.clear()

    def print_cache() -> None:
        if cache:
            print("\n".join(f"{name} - {sum(times) / len(times)} s" for name, times in cache.items()))
        else:
            print("Bench is empty")

    return get_cache, add_value, clear_cache, print_cache


def benchtime(name: str) -> Callable:
    """Decorator that stores the average execution time of a function

    Uses "name" as key in cached execution times dict.
    """
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def wrapper(*args, **kwargs):
            start_time = time()
            return_value = f(*args, **kwargs)
            add_bench(name, time() - start_time)
            return return_value
        return wrapper
    return decorator


def test() -> None:
    add_bench("simple test", 0.5)
    add_bench("simple test", 1.0)

    @benchtime("decorator test")
    def time_waster() -> None:
        dumpster = [1]
        for i in range(2000):
            dumpster.append(sum(dumpster))

    for i in range(10):
        time_waster()

    print_bench()


get_bench, add_bench, clear_bench, print_bench = create_bench()

if __name__ == "__main__":
    test()
