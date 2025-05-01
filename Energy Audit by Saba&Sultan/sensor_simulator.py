
import random
import time
import pandas as pd

def simulate_sensor_data(num_samples=10):
    temp_unit = "°C"
    pressure_unit = "kPa"

    data = {
        "Timestamp": [],
        f"Temperature ({temp_unit})": [],
        f"Pressure ({pressure_unit})": []
    }

    for i in range(num_samples):
        data["Timestamp"].append(time.strftime("%Y-%m-%d %H:%M:%S"))
        data[f"Temperature ({temp_unit})"].append(round(random.uniform(20.0, 100.0), 2))
        data[f"Pressure ({pressure_unit})"].append(round(random.uniform(90.0, 110.0), 2))
        time.sleep(0.5)

    df = pd.DataFrame(data)
    df.to_csv("simulated_sensor_data.csv", index=False)
    print("Simulated data saved to 'simulated_sensor_data.csv'")
    print(df)

if __name__ == "__main__":
    simulate_sensor_data()
