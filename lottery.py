from qrng import generate_quantum_number


def generate_unique_lottery_numbers(count: int = 6, min_num: int = 1, max_num: int = 49) -> list:
    numbers = set()

    while len(numbers) < count:
        quantum_number = generate_quantum_number(8)
        lottery_number = (quantum_number % max_num) + min_num

        numbers.add(lottery_number)

    return sorted(numbers)


def get_lottery_mode(mode: str):
    modes = {
        "Classic 6/49": {
            "count": 6,
            "min_num": 1,
            "max_num": 49
        },
        "Powerball Style": {
            "count": 5,
            "min_num": 1,
            "max_num": 69
        },
        "EuroMillions Style": {
            "count": 5,
            "min_num": 1,
            "max_num": 50
        }
    }

    return modes.get(mode)