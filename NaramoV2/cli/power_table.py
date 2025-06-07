import sys
from findHeatV2 import ReactorCalculator

def generate_lookup_table(increment):
    calculator = ReactorCalculator()
    
    # Define range
    start_excess = 15000
    end_excess = 23000
    
    # Prepare output
    header = "Heat | Total | Excess"
    separator = "-" * len(header)
    
    lines = [header, separator]
    
    # Generate table
    current_excess = start_excess
    while current_excess <= end_excess:
        try:
            required_temp, _ = calculator.calculate_temperature_for_excess(current_excess)
            total_generation = current_excess + 25000
            
            line = f"{required_temp:.0f} | {total_generation:.0f} | {current_excess:.0f}"
            lines.append(line)
            
        except Exception as e:
            print(f"Error calculating for {current_excess}: {e}")
            
        current_excess += increment
    
    # Output to terminal
    print("\nPower Order Lookup Table:")
    for line in lines:
        print(line)
    
    # Ask user about saving to file
    try:
        save_to_file = input("\nSave to file? (y/n): ").lower().strip()
        if save_to_file in ['y', 'yes']:
            filename = f"power_lookup_{increment}.txt"
            try:
                with open(filename, 'w') as f:
                    f.write("Power Order Lookup Table\n")
                    f.write(f"Increment: {increment}\n\n")
                    for line in lines:
                        f.write(line + "\n")
                print(f"Table saved to: {filename}")
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            print("Table not saved.")
    except KeyboardInterrupt:
        print("\nTable not saved.")

def main():
    # Get increment from command line or user input
    if len(sys.argv) > 1:
        try:
            increment = int(sys.argv[1])
        except ValueError:
            print("Error: Increment must be a number")
            sys.exit(1)
    else:
        try:
            increment = int(input("Enter increment size: "))
        except ValueError:
            print("Error: Please enter a valid number")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit(0)
    
    if increment <= 0:
        print("Error: Increment must be positive")
        sys.exit(1)
    
    generate_lookup_table(increment)

if __name__ == "__main__":
    main()