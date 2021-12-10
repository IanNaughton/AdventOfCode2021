
def main():
    part_one_answer = part_one()
    print(f"Part one answer: {part_one_answer}")
    part_two_answer = part_two()
    print(f"Part two answer: {part_two_answer}")


def read_inputs():
    input = open("input.txt")
    raw_binary_lines = input.readlines()
    binary_lines = [
        [character for character in line[:-1]]
        for line in raw_binary_lines
    ]
    return binary_lines


# This looks weird because we're doing a pivot
# without actually reordering the data to keep
# the time/space complexity down.
# If readability were the goal, I would pivot
# the data before counting the columns.
def part_one():
    binary_lines = read_inputs()
    gamma_list = []
    epsilon_list = []

    for column in range(0, len(binary_lines[0])):
        zeroes = 0
        ones = 0

        for row in range(0, len(binary_lines)):
            if binary_lines[row][column] == "0":
                zeroes += 1
            else:
                ones += 1

        if zeroes > ones:
            gamma_list.append("0")
            epsilon_list.append("1")
        else:
            gamma_list.append("1")
            epsilon_list.append("0")

    binary_gamma = ''.join(gamma_list)
    binary_epsilon = ''.join(epsilon_list)
    gamma = int(binary_gamma, 2)
    epsilon = int(binary_epsilon, 2)
    print(f"Gamma: {gamma}")
    print(f"Epsilon: {epsilon}")
    return gamma * epsilon


# P A R T  2
# R E C U R S I V E  J O U R N E Y
def part_two():
    binary_lines = read_inputs()
    max_length = len(binary_lines[0]) - 1
    oxygen_binary_rating = find_rating(
        get_oxygen_generator_bit_to_keep, 0, binary_lines, max_length)
    oxygen_rating = int(oxygen_binary_rating, 2)
    print(f"Oxygen Generator Rating: {oxygen_rating}")
    scrubber_binary_rating = find_rating(
        get_scrubber_generator_bit_to_keep, 0, binary_lines, max_length)
    scrubber_rating = int(scrubber_binary_rating, 2)
    print(f"C02 Scrubber Rating: {scrubber_rating}")
    return oxygen_rating * scrubber_rating


def get_oxygen_generator_bit_to_keep(zeroes, ones):
    bit_to_keep = ""
    if zeroes > ones:
        bit_to_keep = "0"
    else:
        bit_to_keep = "1"
    return bit_to_keep


def get_scrubber_generator_bit_to_keep(zeroes, ones):
    bit_to_keep = ""
    if zeroes > ones:
        bit_to_keep = "1"
    else:
        bit_to_keep = "0"
    #print(f"Zeroes: {zeroes}, Ones: {ones}, Bit to keep: {bit_to_keep}")
    return bit_to_keep


def find_rating(find_bit_to_keep, column, binary_lines, max_length):
    zeroes = 0
    ones = 0
    bit_to_keep = ""

    # Handle an edge case where we are down to the last
    # item in the list--we just want to take the value
    # for that item as our bit to keep in that case.
    if len(binary_lines) == 1:
        bit_to_keep = binary_lines[0][column]
    else:
        for row in range(0, len(binary_lines)):
            if binary_lines[row][column] == "0":
                zeroes += 1
            else:
                ones += 1

        bit_to_keep = find_bit_to_keep(zeroes, ones)

    updated_binary_lines = []
    for row in range(0, len(binary_lines)):
        if binary_lines[row][column] == bit_to_keep:
            updated_binary_lines.append(binary_lines[row])

    if column == max_length:
        return bit_to_keep
    else:
        bits = find_rating(
            find_bit_to_keep,
            column + 1,
            updated_binary_lines,
            max_length
        )
        return bit_to_keep + bits


if __name__ == "__main__":
    main()
