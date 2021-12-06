
def main():
    part_one_answer = part_one()
    print(f"Part one answer: {part_one_answer}")
    part_two_answer = part_two()
    print(f"Part two answer: {part_two_answer}")


def part_one():
    inputs = read_inputs()
    return move_sub(inputs)


def part_two():
    inputs = read_inputs()
    return aim_sub(inputs)


def read_inputs():
    input = open("input.txt")
    raw_directions = input.readlines()
    text_directions = [
        direction[:-1].split(" ")
        for direction in raw_directions
    ]
    return [{"direction": direction[0],
             "distance": int(direction[1])} for direction in text_directions]


def move_sub(inputs):
    current_location = {"distance": 0, "depth": 0}

    for input in inputs:
        match input["direction"]:
            case "up":
                current_location["depth"] -= input["distance"]
            case "down":
                current_location["depth"] += input["distance"]
            case "forward":
                current_location["distance"] += input["distance"]
    return current_location["distance"] * current_location["depth"]


def aim_sub(inputs):
    current_location = {"distance": 0, "depth": 0, "aim": 0}

    for input in inputs:
        match input["direction"]:
            case "up":
                current_location["aim"] -= input["distance"]
            case "down":
                current_location["aim"] += input["distance"]
            case "forward":
                current_location["distance"] += input["distance"]
                current_location["depth"] = current_location["depth"] + (current_location["aim"]
                                                                         * input["distance"])
    return current_location["distance"] * current_location["depth"]


if __name__ == "__main__":
    main()
