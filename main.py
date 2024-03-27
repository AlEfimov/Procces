from multiprocessing import Process, Manager


def sqr(d, number):
    d.append(number * number)


def compute_squares(salaries):
    prots = []
    mng = Manager()
    d = mng.list()
    for number in salaries:
        proc = Process(target=sqr, args=(d, number,))
        prots.append(proc)
        proc.start()

    for proc in prots:
        proc.join()
    return d

if __name__ == '__main__':
    salaries = [2, 3, 1, 5, 7]
    salaries_sqr = compute_squares(salaries)
    print(salaries_sqr)