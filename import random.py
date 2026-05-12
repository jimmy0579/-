import random
import time

N = 100000
MAX_VAL = 65535

arr = [random.randint(0, MAX_VAL) for _ in range(N)]

# -----------------------------
# Counting Sort
# -----------------------------
def counting_sort(a, k):
    count = [0] * (k + 1)

    for x in a:
        count[x] += 1

    result = []

    for value in range(k + 1):
        result.extend([value] * count[value])

    return result

# -----------------------------
# Radix Sort (base 256)
# -----------------------------
def radix_sort(a):
    output = list(a)

    for shift in [0, 8]:
        buckets = [[] for _ in range(256)]

        for num in output:
            digit = (num >> shift) & 255
            buckets[digit].append(num)

        output = []

        for bucket in buckets:
            output.extend(bucket)

    return output

# -----------------------------
# Python built-in sorted
# -----------------------------
start = time.time()
python_sorted = sorted(arr)
python_time = time.time() - start

# -----------------------------
# Counting Sort timing
# -----------------------------
start = time.time()
counting_sorted = counting_sort(arr, MAX_VAL)
counting_time = time.time() - start

# -----------------------------
# Radix Sort timing
# -----------------------------
start = time.time()
radix_sorted = radix_sort(arr)
radix_time = time.time() - start

# -----------------------------
# Verification
# -----------------------------
print("Correct:", python_sorted == counting_sorted == radix_sorted)

print(f"Python sorted(): {python_time:.4f} sec")
print(f"Counting Sort : {counting_time:.4f} sec")
print(f"Radix Sort    : {radix_time:.4f} sec")