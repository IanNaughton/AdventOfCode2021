
def main():
    part_one_answer = part_one()
    print(f"Total inecreases: {part_one_answer}")
    part_two_answer = part_two()
    print(f"Total sliding window increases: {part_two_answer}")


def read_depths():
    input = open("input.txt")
    depths = input.readlines()
    return [int(depth[:-1]) for depth in depths]


def part_one():
    depths = read_depths()
    lastDepth = None
    depth_increases = 0

    for depth in depths:

        # Deal with the first iteration
        if lastDepth == None:
            lastDepth = depth
            continue

        if depth > lastDepth:
            depth_increases += 1
        lastDepth = depth
    return depth_increases


def part_two():
    depths = read_depths()
    sum_of_last_window = None
    depth_increases = 0

    for depth in range(0, len(depths) - 1):

        # Deal with the end of the list
        if depth + 3 > len(depths):
            break

        sum_of_current_window = depths[depth] + \
            depths[depth + 1] + depths[depth + 2]

        # Deal with the first iteration
        if sum_of_last_window == None:
            sum_of_last_window = sum_of_current_window
            continue

        if sum_of_current_window > sum_of_last_window:
            depth_increases += 1
        sum_of_last_window = sum_of_current_window
    return depth_increases


if __name__ == "__main__":
    main()
