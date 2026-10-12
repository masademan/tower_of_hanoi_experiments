from display import do_instructions_and_display
from solver import hanoi_solver, create_starting_rings_in_pos

if __name__ == "__main__":
    NUM_RINGS = 5

    instructions = []
    rings = create_starting_rings_in_pos(NUM_RINGS)

    hanoi_solver(instructions, NUM_RINGS)

    # success = do_instructions_and_display(instructions, rings, {"do_pause": True, "do_clear": True})  # Manual next step
    success = do_instructions_and_display(instructions, rings, {"do_pause": True, "do_clear": True, "secs_per_step": 0.1})  # Animated steps
    # success = do_instructions_and_display(instructions, rings)  # See all steps at once

    if success:
        print(f"Solved! Took {len(instructions)} moves")
