
"""
Nuclear Reactor Temperature Calculator

This script calculates the required temperature to achieve a target excess power
level for the Naramo Reactor. It uses linear regression models based on
the relationships between temperature-pressure and pressure-excess.

The script works with excess power (total generation - 25000 facility power requirement).

Usage:
    python findHeatV2.py [target_excess_power]
    
If no target is provided, the script will prompt for input.
"""

import numpy as np
import sys
from scipy import stats
import argparse

class ReactorCalculator:
    def __init__(self):
        # Observational data from Naramo (thanks, Dusky!)
        self.pressure = np.array([
            6033.7, 6483.0, 6677.6, 8074.5, 7345.0, 7169.6, 7318.3, 7618.4, 7737.1, 7854.7,
            6690.1, 6741.4, 7088.9, 6117.3, 6230.3, 6312.6, 6424.8
        ])

        self.temperature = np.array([
            1230.4, 1299.1, 1328.8, 1542.5, 1430.9, 1404.1, 1426.8, 1472.7, 1490.9, 1508.9,
            1330.8, 1338.6, 1391.8, 1243.1, 1260.4, 1273.0, 1290.2
        ])

        # Total generation data
        self.total_generation = np.array([
            40225, 43220, 44517, 53830, 48967, 47797, 48789, 50789, 51580, 52365,
            44601, 44943, 47260, 40782, 41535, 42084, 42832
        ])
        
        # Facility power requirement (constant)
        self.facility_power = 25000
        
        # Calculate excess power (generation - facility requirements)
        self.excess_power = self.total_generation - self.facility_power
        
        # Calculate regression models
        self._calculate_models()
    
    def _calculate_models(self):
        """Calculate linear regression models for the relationships"""
        # Temperature vs Pressure relationship
        self.temp_pressure_slope, self.temp_pressure_intercept, self.temp_pressure_r, _, _ = \
            stats.linregress(self.temperature, self.pressure)
        
        # Pressure vs Excess Power relationship
        self.pressure_excess_slope, self.pressure_excess_intercept, self.pressure_excess_r, _, _ = \
            stats.linregress(self.pressure, self.excess_power)
    
    def excess_to_pressure(self, target_excess):
        """Convert target excess power to required pressure"""
        required_pressure = (target_excess - self.pressure_excess_intercept) / self.pressure_excess_slope
        return required_pressure
    
    def pressure_to_temperature(self, target_pressure):
        """Convert target pressure to required temperature"""
        required_temperature = (target_pressure - self.temp_pressure_intercept) / self.temp_pressure_slope
        return required_temperature
    
    def calculate_temperature_for_excess(self, target_excess):
        """Calculate required temperature for target excess power"""
        # Step 1: Excess Power → Pressure
        required_pressure = self.excess_to_pressure(target_excess)
        
        # Step 2: Pressure → Temperature
        required_temperature = self.pressure_to_temperature(required_pressure)
        
        return required_temperature, required_pressure
    
    def validate_ranges(self, target_excess):
        """Check if target excess power is within reasonable bounds"""
        min_excess = np.min(self.excess_power)
        max_excess = np.max(self.excess_power)
        
        if target_excess < min_excess * 0.8 or target_excess > max_excess * 1.2:
            print(f"!!  WARNING: Target excess power ({target_excess:.0f}) is outside the typical range")
            print(f"   Observed range: {min_excess:.0f} - {max_excess:.0f}")
            print(f"   Extrapolation may be less accurate")
            print()
    
    def run_calculation(self, target_excess):
        """Run the main calculation and display results"""
        self.validate_ranges(target_excess)
        
        required_temp, required_pressure = self.calculate_temperature_for_excess(target_excess)
        
        # Calculate total generation needed
        total_generation_needed = target_excess + self.facility_power

        print(f"\n📊 Calculated Requirements:")
        print(f"   Total Generation Needed: \n   {total_generation_needed:.0f} (excess + {self.facility_power} facility)")
        print(f"\n   Required Pressure: \n   {required_pressure:.1f}")
        print(f"\n   Required Temperature: \n   {required_temp:.1f}")
        print()
        
        return required_temp, required_pressure

def main():
    parser = argparse.ArgumentParser(description='Calculate required temperature for target power generation')
    parser.add_argument('target', nargs='?', type=float, 
                       help='Target excess power level')
    
    args = parser.parse_args()
    
    calculator = ReactorCalculator()
    
    
    # Get target excess power
    if args.target is not None:
        target_excess = args.target
    else:
        try:
            # calculator.display_current_status()
            target_excess = float(input("Enter target excess power: "))
        except ValueError:
            print("Error: Please enter a valid number")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit(0)
    
    try:
        calculator.run_calculation(target_excess)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()