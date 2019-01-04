from fire import Fire
from random import randint
from time import time
from yaspin import yaspin


@yaspin(text="Calculating!!!")
def time_to(length=5):
    default = list(range(length))
    # print(default)
    generated = set()
    start = time()
    loop_count = 0
    while default != list(generated):
        loop_count += 1
        rand = randint(0, length - 1)
        # print("Generated number is ", rand)
        generated.add(rand)
        # print(generated)
    print("\n", time() - start, "seconds")
    print("Total numbers generated = ", loop_count)


if __name__ == "__main__":
    Fire(time_to)
