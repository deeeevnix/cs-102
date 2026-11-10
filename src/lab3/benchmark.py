import multiprocessing
import threading
import time

from sudoku import read_sudoku, solve


def run_solve(filename):
    grid = read_sudoku(filename)
    start = time.perf_counter()
    solve(grid)
    elapsed = time.perf_counter() - start
    print(f"{filename}: {elapsed:.3f} с")


if __name__ == "__main__":
    filenames = ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]

    print("Последовательно")
    start = time.perf_counter()

    for filename in filenames:
        run_solve(filename)

    print(f"Общее время: {time.perf_counter() - start:.3f} с")

    for worker_type in (threading.Thread, multiprocessing.Process):
        print(worker_type.__name__)
        start = time.perf_counter()
        workers = []

        for filename in filenames:
            worker = worker_type(target=run_solve, args=(filename,))
            worker.start()
            workers.append(worker)

        for worker in workers:
            worker.join()

        print(f"Общее время: {time.perf_counter() - start:.3f} с")