from display import do_instructions_and_display
from solver import hanoi_solver, create_starting_rings_in_pos

if __name__ == "__main__":
    NUM_RINGS = 3

    instructions = []
    rings = create_starting_rings_in_pos(NUM_RINGS)

    hanoi_solver(instructions, NUM_RINGS)

    success = do_instructions_and_display(instructions, rings, {"do_base": True, "padding_on_edges": 3, "do_pause": True})

    if success:
        print("Solved!")
