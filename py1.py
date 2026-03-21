class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.sequence = []

    def generate(self):
        for i in range(self.n):
            self.sequence.append(self._fib(i))
        return self.sequence

    def _fib(self, k):
        if k <= 1:
            return k
        return self._fib(k - 1) + self._fib(k - 2)


class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers

    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        sorted_nums = sorted(self.numbers)
        mid = len(sorted_nums) // 2
        if len(sorted_nums) % 2 == 0:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        else:
            return sorted_nums[mid]

    def variance(self):
        m = self.mean()
        return sum((x - m) ** 2 for x in self.numbers) / len(self.numbers)


if __name__ == "__main__":
    # Generate Fibonacci sequence of length 10
    fib = Fibonacci(10)
    sequence = fib.generate()
    print("Fibonacci sequence:", sequence)

    # Compute statistics on the sequence
    stats = Statistics(sequence)
    print("Mean:", stats.mean())
    print("Median:", stats.median())
    print("Variance:", stats.variance())

