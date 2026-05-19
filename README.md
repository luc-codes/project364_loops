# Project 364 - Insurance Costs using Python loops.

A beginner Python project focused on practicing loops, list comprehensions, CSV file handling, and project organization.

## Project Overview

This project analyses fictional insurance cost data stored in CSV files.

The script:

- Loads data from CSV files
- Calculates total insurance cost
- Calculates average insurance cost
- Compares each individual's insurance cost against the average
- Determines how far above or below average a cost is
- Uses loops (`for` and `while`)
- Uses list comprehensions

## Technologies Used

- Python 3
- pandas
- CSV files
- Jupyter Notebook
- VS Code

## Project Structure

project364_loops/

├── data/
│   ├── actual_insurance_costs.csv
│   ├── estimated_insurance_costs.csv
│   └── names.csv
│
├── notebooks/
│   └── explore.ipynb
│
├── src/
│   └── project364_loops.py
│
├── venv/
├── .gitignore
└── README.md

## Example Dataset

### names.csv

```csv
name
Judith
Abel
Tyson
Martha
Beverley
David
Anabel
```

### actual_insurance_costs.csv

```csv
act_costs
1100.0
2200.0
3300.0
4400.0
5500.0
6600.0
7700.0
```

## Skills Practiced

- Variables
- Lists
- `for` loops
- `while` loops
- `range()`
- Conditional statements (`if`, `elif`, `else`)
- List comprehensions
- Reading CSV files
- Relative file paths
- Project folder organization
- Version control with Git

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install pandas
```

4. Run the project

```bash
python src/project364_loops.py
```

## Learning Notes

This project was created as part of learning Python programming fundamentals and exploring a more professional workflow using:

- Jupyter Notebook for experimentation
- VS Code for scripting and project organization
- Git and GitHub for version control