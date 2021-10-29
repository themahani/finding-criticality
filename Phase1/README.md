# Phase 1

## Directory Structure
- The `raw data` directory contains the raw data that we were given from the research conducted by Mr. Mahdi Naghiloo.
  - There is the `unbasket` folder containing the raw data we got from Mr. Mahdi Naghiloo
  - There is the `basket` folder containing the basketed data saved using the `log_basketing.py` script.
  - `read_files` contains a method for reading the data files and loading them.
  - `regions` contains matrix files that indicate the label of the data.
- `labeling.py` contains methods to extract the `criticality` label of our data.
- `features` contains methods to process the data and extract features.
- `gen_data.py` puts all of the above together to generate the dataframe and save it in `.csv` format.
- `main_data.csv` is the data file we will use in future phases of this project.
- `test data.ipynb` is a jupyter notebook containing some statistical analysis of the main data.
