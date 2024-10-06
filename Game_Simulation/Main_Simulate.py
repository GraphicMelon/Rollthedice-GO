import random
import pandas as pd

# Function to simulate the game
def simulate_game(throws, simulations_per_throw):
    # Circle points (A-H)
    points = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    # Result list to store simulation results
    results = []

    # Run simulations for each throw count from 1 to the specified limit
    for throw_count in range(1, throws + 1):
        for sim_num in range(1, simulations_per_throw + 1):
            # Start at point A
            current_position = 0
            dice_rolls = []
            positions = ['A']  # Start at A

            for throw in range(throw_count):
                # Roll a dice (1 to 6)
                dice_roll = random.randint(1, 6)
                dice_rolls.append(dice_roll)

                # Move the piece forward by the dice roll value
                current_position = (current_position + dice_roll) % len(points)
                positions.append(points[current_position])

            # Calculate the final distance to A in clockwise direction
            final_position = current_position
            distance_to_A = (len(points) - final_position) % len(points)

            # Log result for this simulation
            results.append({
                "Throw_Count": throw_count,
                "Simulation_Number": sim_num,
                "Dice_Rolls": dice_rolls,
                "Positions": positions[1:],  # Exclude initial 'A'
                "Final_Position": points[final_position],
                "Distance_to_A": distance_to_A
            })

    # Convert results to DataFrame for easy viewing
    df = pd.DataFrame(results)
    return df

# Simulate the game with 1-10 throws and 1000 simulations per throw
throws = 10
simulations_per_throw = 1000
simulation_results = simulate_game(throws, simulations_per_throw)

# Save the simulation results to a CSV file
simulation_results.to_csv('simulation_results.csv', index=False)
