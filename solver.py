# make recursive hanoi solver (for turing complete)

# pseudocode:
"""
def solver(source, dest, n_rings)
if n_rings == 1
   move top ring from source to dest

unused = place that's not source and not dest, the last third one
solver(source, unused, n_rings - 1)
move top ring from source to dest
solver(unused, dest, n_rings - 1)
"""

# instructions are in the form tuple[int, int], where the first number is where the ring is coming from, and the second number is where the ring is going
# when moving a ring, the one on top is being moved
import sys


def hanoi_solver(instruction_list: list[tuple[int, int]], src_num: int, dest_num: int, n_rings: int) -> None:
    """
    Makes a list of instructions to solve the tower of hanoi
    """
    if not (0 <= src_num < 3):
        print("src_num has to be between 0 and 2 inclusive", file=sys.stderr)
        sys.exit(-1)
    if not (0 <= dest_num < 3):
        print("dest_num has to be between 0 and 2 inclusive", file=sys.stderr)
        sys.exit(-1)
    if src_num == dest_num:
        print("src_num and dest_num can't be the same", file=sys.stderr)
        sys.exit(-1)

    if n_rings == 1:
        instruction_list.append((src_num, dest_num))
        return

    other_pos = 2 + 1 + 0 - (src_num + dest_num)
    hanoi_solver(instruction_list, src_num, other_pos, n_rings - 1)
    instruction_list.append((src_num, dest_num))
    hanoi_solver(instruction_list, other_pos, dest_num, n_rings - 1)


def move_ring(rings_in_pos: list[list[int]], src_num: int, dest_num: int) -> None:
    """
    Move ring from src (source) to dest (destination)
    """
    if src_num == dest_num:
        return

    ring_taken = rings_in_pos[src_num].pop()
    rings_in_pos[dest_num].append(ring_taken)


def is_valid_instruction(instruction: tuple[int, int], rings_in_pos: list[list[int]]) -> bool:
    for instruction_part in instruction:
        if not (0 <= instruction_part < 3):
            return False

    if len(rings_in_pos[instruction[0]]) == 0:
        return False

    return True


def is_valid_ring_pos(rings_in_pos: list[list[int]]) -> bool:
    for ring_pos in rings_in_pos:
        for idx in range(1, len(ring_pos)):
            if ring_pos[idx - 1] <= ring_pos[idx]:
                return False

    return True


def get_num_rings(rings_in_pos: list[list[int]]) -> int:
    return sum([len(ring_pos) for ring_pos in rings_in_pos])


def is_solved(rings_in_pos: list[list[int]]) -> bool:
    num_rings = get_num_rings()

    return rings_in_pos == [[], [], list(range(num_rings, 0, -1))]


def create_starting_rings_in_pos(num_rings: int) -> list[list[int]]:
    if num_rings <= 0:
        print("The number of rings has to be positive", file=sys.stderr)
        sys.exit(-1)

    return [list(range(num_rings, 0, -1)), [], []]


def do_instructions(
    instruction_list: list[tuple[int, int]], rings_in_pos: list[list[int]], src_num: int, dest_num: int
) -> bool:
    """
    Follow the instructions from the hanoi_solver function
    Returns true if the puzzle was solved and all the instructions were valid, otherwise return false
    """
    if not (0 <= src_num < 3):
        print("src_num has to be between 0 and 2 inclusive", file=sys.stderr)
        sys.exit(-1)
    if not (0 <= dest_num < 3):
        print("dest_num has to be between 0 and 2 inclusive", file=sys.stderr)
        sys.exit(-1)
    if src_num == dest_num:
        print("src_num and dest_num can't be the same", file=sys.stderr)
        sys.exit(-1)

    if not is_valid_ring_pos(rings_in_pos):
        print("The starting ring configuration was invalid", file=sys.stderr)
        return False

    for instruction in instruction_list:
        if not is_valid_instruction(instruction, rings_in_pos):
            print(f"Instruction '{instruction}' is invalid", file=sys.stderr)
            return False
        if not is_valid_ring_pos(rings_in_pos):
            print(f"Ring configuration '{rings_in_pos}' is invalid", file=sys.stderr)
            return False

        move_ring(rings_in_pos, instruction[0], instruction[1])

    if not is_solved(rings_in_pos):
        print("The end was not solved", file=sys.stderr)
        return False

    return True


if __name__ == "__main__":
    NUM_RINGS = 3

    instruction_list = []
    hanoi_solver(instruction_list, 0, 2, NUM_RINGS)

    print("\n".join([str(item) for item in instruction_list]))

    rings_in_pos = create_starting_rings_in_pos(NUM_RINGS)

    print(do_instructions(instruction_list, rings_in_pos, 0, 2))
