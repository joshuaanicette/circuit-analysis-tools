# circuit-analysis-tools
Circuit Analyzer is a Python-based project designed to analyze electrical circuits with resistors in parallel. The tool provides a user-friendly way to calculate equivalent resistance, current, and power dissipation for each resistor. Additionally, it includes a graphical representation of power dissipation to enhance understanding and visualization.

This project features calculations of equivalent resistance for resistors in parallel, computation of total current using Ohm's Law, and detailed power dissipation analysis for individual resistors. A built-in visualization function plots the power dissipation, making it easy to interpret the results.

To use Circuit Analyzer, you'll need Python 3.7 or higher along with the libraries NumPy and Matplotlib. Installation is simple: clone the repository and install the required libraries using pip. Once installed, users can customize the resistor values and voltage in the __main__ block of the code to analyze their specific circuit configuration. Running the program generates outputs that include the equivalent resistance, total current, and power dissipation, as well as a graphical bar plot of the power dissipation for each resistor.

For example, with resistors set to [100, 200, 300] ohms and a voltage of 10 volts, the program calculates an equivalent resistance of 54.55 ohms, a total current of 0.18 A, and power dissipations of 3.33 W, 6.67 W, and 10.00 W for each resistor respectively. The output also includes a clear, visually appealing plot of the power dissipation data.

This project is distributed under the MIT License, allowing users to freely use, modify, and distribute the software. Contributions are welcome, and users are encouraged to fork the repository and submit pull requests to enhance the functionality or fix issues.
