def difference(numbers):
    if not numbers:
        return 0
    return round(max(numbers) - min(numbers), 2)
