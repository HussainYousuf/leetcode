# the class is b/c to avoid mutable default argument, reinitialize the object whenever u want to reuse the method


class AllBinary:
    def __init__(self) -> None:
        self.res = []

    def genBin(self, n, bs=[]):
        if len(bs) == n:
            self.res.append(bs)
        else:
            self.genBin(n, bs + [0])
            self.genBin(n, bs + [1])
        return self.res


if __name__ == "__main__":
    print(AllBinary().genBin(5))
