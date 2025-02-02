# TOPSIS Implementation by Arushi Gadodia

A Python package that implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method.

Submitted by: Arushi Gadodia
Roll Number: 102203683

## Installation

```bash
pip install Topsis-Arushi Gadodia-102203683
```

## Usage

From command line:
```bash
topsis input.csv "1,1,1,2" "+,+,-,+" output.csv
```

From Python:
```python
from topsis import calculate_topsis
calculate_topsis("input.csv", "1,1,1,2", "+,+,-,+", "output.csv")
```

## Input Format

1. Input file must be a CSV file with 3 or more columns
2. First column is the object/variable name
3. From 2nd column onwards should contain only numeric values
4. Weights should be comma-separated numbers (e.g. "1,1,1,2")
5. Impacts should be comma-separated +/- symbols (e.g. "+,+,-,+")

## Output

The program will create a result CSV file containing:
- All columns from input file
- Two additional columns: 'Topsis Score' and 'Rank'

## Error Handling

The program will check for:
- Correct number of parameters
- File existence
- Input file format
- Number of weights/impacts matching number of criteria
- Valid impact symbols (+/-)

## License

© 2024 Arushi Gadodia
This project is licensed under the MIT License - see the LICENSE file for details.#   T o p s i s 
 
 #   p y p a c k a g e  
 