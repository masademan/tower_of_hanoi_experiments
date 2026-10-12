import os
import sys
import shutil
import subprocess
from solver import (
    is_solved,
    move_ring,
    get_num_rings,
    is_valid_ring_pos,
    is_valid_instruction,
)


def print_rings_in_pos(rings_in_pos: list[list[int]]) -> None:
    num_rings = get_num_rings(rings_in_pos)


def do_instructions_and_display(
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

    print_rings_in_pos(rings_in_pos)

    for instruction in instruction_list:
        if not is_valid_instruction(instruction, rings_in_pos):
            print(f"Instruction '{instruction}' is invalid", file=sys.stderr)
            return False
        if not is_valid_ring_pos(rings_in_pos):
            print(f"Ring configuration '{rings_in_pos}' is invalid", file=sys.stderr)
            return False

        move_ring(rings_in_pos, instruction[0], instruction[1])

        print_rings_in_pos(rings_in_pos)

    if not is_solved(rings_in_pos):
        print("The end was not solved", file=sys.stderr)
        return False

    return True


def clear_console():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


if __name__ == "__main__":
    from solver import create_starting_rings_in_pos

    print_rings_in_pos(create_starting_rings_in_pos(num_rings=3))

    print(shutil.get_terminal_size())