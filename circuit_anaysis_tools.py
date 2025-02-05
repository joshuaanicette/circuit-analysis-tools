import numpy as np
import matplotlib.pyplot as plt

class CircuitAnalyzer:
    def __init__(self, resistors, voltage):
        """
        Initialize the CircuitAnalyzer.

        Parameters:
            resistors (list of float): List of resistances in ohms.
            voltage (float): Voltage of the power source in volts.
        """
        self.resistors = resistors
        self.voltage = voltage

    def calculate_equivalent_resistance(self):
        """Calculate the equivalent resistance for resistors in parallel."""
        if len(self.resistors) == 0:
            return 0
        return 1 / sum(1 / r for r in self.resistors)

    def calculate_current(self):
        """Calculate the current using Ohm's Law."""
        R_eq = self.calculate_equivalent_resistance()
        return self.voltage / R_eq

    def power_dissipation(self):
        """Calculate power dissipation for each resistor."""
        current = self.calculate_current()
        return [current**2 * r for r in self.resistors]

    def plot_power_dissipation(self):
        """Plot the power dissipation for each resistor."""
        power = self.power_dissipation()
        resistor_labels = [f"R{i+1}" for i in range(len(self.resistors))]
        
        plt.bar(resistor_labels, power, color="skyblue")
        plt.title("Power Dissipation in Each Resistor")
        plt.xlabel("Resistors")
        plt.ylabel("Power (W)")
        plt.show()

if __name__ == "__main__":
    # Example usage
    print("--- Circuit Analyzer ---")

    # Input: Resistances and voltage
    resistors = [100, 200, 300]  # Resistor values in ohms
    voltage = 10  # Voltage in volts

    analyzer = CircuitAnalyzer(resistors, voltage)

    print(f"Resistors: {resistors} ohms")
    print(f"Voltage: {voltage} volts")

    R_eq = analyzer.calculate_equivalent_resistance()
    print(f"Equivalent Resistance: {R_eq:.2f} ohms")

    current = analyzer.calculate_current()
    print(f"Total Current: {current:.2f} A")

    power = analyzer.power_dissipation()
    print(f"Power Dissipation: {[f'{p:.2f} W' for p in power]}")

    # Plot power dissipation
    analyzer.plot_power_dissipation()