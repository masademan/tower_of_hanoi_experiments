import os
import sys
import shutil
import subprocess
from typing import Any
from solver import (
    is_solved,
    move_ring,
    get_num_rings,
    is_valid_ring_pos,
    is_valid_instruction,
)


def clear_console():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def do_string_padding(in_str: str, full_len: int, padding_char: str = " ") -> str:
    if len(in_str) >= full_len:
        return in_str

    total_padding = full_len - len(in_str)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding

    return "".join([padding_char * left_padding, in_str, padding_char * right_padding])


def print_rings_in_pos(
    rings_in_pos: list[list[int]],
    peg_extra_height: int = 1,
    padding_between_pegs: int = 2,
    padding_on_edges: int = 1,
    do_base: bool = False,
    ring_char: str = "@",
    base_char: str = "=",
    padding_char: str = " ",
    do_pause: bool = False,
    do_clear: bool = True,
) -> None:
    num_rings = get_num_rings(rings_in_pos)
    terminal_size = shutil.get_terminal_size()

    if terminal_size.lines < num_rings + peg_extra_height + int(do_base) + 1:
        print("Terminal size is too short for the requested number of rings in the tower of Hanoi", file=sys.stderr)
        print("Either increase the height of the terminal or use less rings", file=sys.stderr)
        sys.exit(-1)

    if terminal_size.columns < 2 * padding_between_pegs + 3 * num_rings + 2 * padding_on_edges:
        print("Terminal size is too narrow for the requested number of rings in the tower of Hanoi", file=sys.stderr)
        print("Either increase the width of the terminal or use less rings", file=sys.stderr)
        sys.exit(-1)

    if do_clear:
        clear_console()

    full_line_len = 2 * num_rings + 1
    list_str_lines_per_peg: list[list[str]] = []
    for ring_pos_idx in range(3):
        str_lines: list[str] = [do_string_padding("|", full_line_len, padding_char)] * (
            peg_extra_height + num_rings - len(rings_in_pos[ring_pos_idx])
        )

        for ring_idx in range(len(rings_in_pos[ring_pos_idx]) - 1, -1, -1):
            str_lines.append(
                do_string_padding(ring_char * (2 * rings_in_pos[ring_pos_idx][ring_idx] + 1), full_line_len, padding_char)
            )

        list_str_lines_per_peg.append(str_lines)

    for peg_a, peg_b, peg_c in zip(*list_str_lines_per_peg):
        print(
            "".join(
                [
                    padding_char * padding_on_edges,
                    peg_a,
                    padding_char * padding_between_pegs,
                    peg_b,
                    padding_char * padding_between_pegs,
                    peg_c,
                    padding_char * padding_on_edges,
                ]
            )
        )

    if do_base:
        print(base_char * (3 * full_line_len + 2 * padding_between_pegs + 2 * padding_on_edges))

    print()
    if do_pause:
        input()


def do_instructions_and_display(
    instruction_list: list[tuple[int, int]],
    rings_in_pos: list[list[int]],
    print_rings_kwargs: dict[str, Any] = {"do_base": True, "padding_on_edges": 3},
) -> bool:
    """
    Follow the instructions from the hanoi_solver function
    Returns true if the puzzle was solved and all the instructions were valid, otherwise return false
    """
    if not is_valid_ring_pos(rings_in_pos):
        print("The starting ring configuration was invalid", file=sys.stderr)
        return False

    print_rings_in_pos(rings_in_pos, **print_rings_kwargs)

    for instruction in instruction_list:
        if not is_valid_instruction(instruction, rings_in_pos):
            print(f"Instruction '{instruction}' is invalid", file=sys.stderr)
            return False
        if not is_valid_ring_pos(rings_in_pos):
            print(f"Ring configuration '{rings_in_pos}' is invalid", file=sys.stderr)
            return False

        move_ring(rings_in_pos, instruction[0], instruction[1])

        print_rings_in_pos(rings_in_pos, **print_rings_kwargs)

    if not is_solved(rings_in_pos):
        print("The end was not solved", file=sys.stderr)
        return False

    return True


if __name__ == "__main__":
    from solver import create_starting_rings_in_pos, hanoi_solver

    instructions = []
    num_rings = 3
    rings = create_starting_rings_in_pos(num_rings)

    hanoi_solver(instructions, num_rings)

    success = do_instructions_and_display(instructions, rings, {"do_base": True, "padding_on_edges": 3, "do_pause": True})

    if success:
        print("Solved!")
