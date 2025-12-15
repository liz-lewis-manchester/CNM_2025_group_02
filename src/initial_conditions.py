import numpy as np
import pandas as pd

def load_and_interpolate_initial_conditions (csv_path, x_grid):
      # Read initial conditions from CSV and interpolate onto the model grid.

df = pd.read_csv(csv_path)

x_col = "Distance (m)"
c_col = "Concentration (µg/m_ )"

df = df[[x_col, c_col]].copy()
df[x_col] = pd.to_numeric(df[x_col], errors="coerce")
df[c_col] = pd.to_numeric(df[c_col], errors="coerce")
df = df.dropna().sort_values(x_col)

x_data = df[x_col].to_numpy()
c_data = df[c_col].to_numpy()

theta0 = np.interp(
  x_grid,
  x_data,
  c_data,
  left=c_data[0],
  right=c_data[-1],
)

return theta0
