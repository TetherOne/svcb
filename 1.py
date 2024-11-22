def calculate_percentages(input_file: str) -> None:
    with open(input_file, "r") as file:
        input_data = file.read().strip().split()

    shares = list(map(float, input_data[1:]))

    total = sum(shares)
    percentages = [(share / total) for share in shares]

    for percentage in percentages:
        print(f"{percentage:.3f}")


calculate_percentages(input_file="input_1.txt")
