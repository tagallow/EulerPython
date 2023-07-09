import problem14 as currentProblem
import time

def main():
    start_time = time.time()
    currentProblem.solve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()