def sort_key(lot: tuple[int, str, float, int, float, float]) -> tuple[int, float, float]:
    return lot[0], -lot[5], lot[4]


def calculate_max_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        n, m, s = map(int, file.readline().strip().split())

        lots: list[tuple[int, str, float, int, float, float]] = []
        """
        day, bond_name, price, quantity, cost, total_profit
        """
        for line in file:
            if not line.strip():
                break
            day, bond_name, price, quantity = line.strip().split()
            day = int(day)
            price = float(price)
            quantity = int(quantity)

            cost = price * 10 * quantity
            profit_per_bond = 30 + 1000 - (price * 10)
            total_profit = profit_per_bond * quantity

            lots.append((day, bond_name, price, quantity, cost, total_profit))

    lots.sort(key=sort_key)

    total_profit: float = 0.0
    purchased_lots: list[tuple[int, str, float, int]] = (
        []
    )
    """
    day, bond_name, price, quantity
    """
    for lot in lots:
        day, bond_name, price, quantity, cost, profit = lot
        if s >= cost:
            s -= cost
            total_profit += profit
            purchased_lots.append((day, bond_name, price, quantity))

    print(int(total_profit))
    for lot in purchased_lots:
        print(f"{lot[0]} {lot[1]} {lot[2]} {lot[3]}")


calculate_max_profit(file_path="input_2.txt")
