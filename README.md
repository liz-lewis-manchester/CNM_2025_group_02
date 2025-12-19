# CNM_2025_group_02
Modelling Pollutant Transport in a River

## Overview
This repository contains coursework for the Computational Numerical Methods (CNM) module.
The aim of the project is to model the one-dimensional transport of a pollutant in a river
using the advection equation. A finite difference numerical method is used to simulate how
pollutant concentration evolves in space and time.

The project was developed collaboratively using GitHub, with branches, commits and pull
requests used to manage contributions from all group members.

---

## Governing Equation
The pollutant transport is modelled using the 1D advection equation:

∂θ/∂t = −U ∂θ/∂x

where:
- θ is the pollutant concentration (μg/m³)
- t is time (s)
- x is distance along the river (m)
- U is the river velocity (m/s)

---
## code libraries
The pollutant model that we have designed is run on google colab. we use the following pyhton libraries to assist us:

- numpy
- pandas
- matplotlib

---

## Repository Structure

CNM_2025_group_02/
- src/             # Source code and modelling notebooks
- test case/       # test case and results
- README.md        # Project documentation
- notebook/        # Codes

## How to Run
Clone the repository: git clone https://github.com/liz-lewis-manchester/CNM_2025_group_02.git
   cd CNM_2025_group_02


Open and run the notebooks or scripts in the `src/` directory using Jupyter Notebook or
JupyterLab.

You will need to open the file initialconditions.csv which can be found in the src folder in the main branch. From here you can download this file and open it using the code. 
---

## Collaboration and Version Control
- Development was carried out using feature and development branches
- Pull requests were used to merge work into the main branch
- Code reviews and commit history document individual contributions

---

## Contributors
All group members contributed to the project through:
- Numerical modelling
- Data handling and interpolation
- Testing and validation
- Visualisation
- Documentation and GitHub management

Individual contributions are visible through GitHub commit history and pull requests.
