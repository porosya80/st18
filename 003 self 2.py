def scan_sort(*numbers):
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError
    return sorted(numbers)


print(scan_sort(1,2,3,4.3,5,7,5,3))