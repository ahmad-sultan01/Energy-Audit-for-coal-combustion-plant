
# Module 1: Data Acquisition & Input Validation

This module is part of the **Comprehensive Energy Audit for Coal-Fired Power Plants** project. It includes tools for acquiring, validating, and processing energy-related data from CSV files or simulated sensors.

## 📦 Contents

- `module1_cli.py`: CLI for loading and validating data from `auxiliary_energy.csv`
- `module1_gui.py`: GUI version using Tkinter
- `sensor_simulator.py`: Simulates sensor readings and saves to `simulated_sensor_data.csv`
- `auxiliary_energy.csv`: Sample input data for validation

---

## 🛠️ Requirements

Ensure you have Python 3 installed. Then install the required package:

```bash
pip install pandas
```

For the GUI version, `tkinter` is required (usually bundled with standard Python installs).

---

## ▶️ How to Use

### CLI Input Handler

```bash
python module1_cli.py
```

### GUI Input Validator

```bash
python module1_gui.py
```

### Sensor Data Simulation

```bash
python sensor_simulator.py
```

---

## ✅ Output

- Input data summary and validation shown in terminal or GUI
- CSV file: `simulated_sensor_data.csv` (from simulator)

---

## 🌐 Deployment

To publish this module:
1. Push these files to a GitHub or Hugging Face repo.
2. Include this README.md in the root directory.
3. Optional: Link with a Streamlit or web dashboard in future modules.

---

## 👥 Contributors

- Ahmad Sultan  
- Saba Amir

