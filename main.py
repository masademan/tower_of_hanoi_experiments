import sys
import solver
import display

if __name__ == "__main__":
    NUM_RINGS = 3

    instruction_list = []
    solver.hanoi_solver(instruction_list, 0, 2, NUM_RINGS)

    print("\n".join([str(item) for item in instruction_list]))

    rings_in_pos = solver.create_starting_rings_in_pos(NUM_RINGS)

    display.do_instructions_and_display(instruction_list, rings_in_pos, 0, 2)
