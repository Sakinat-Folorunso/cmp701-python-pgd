# CMP 701 – Computer Programming I (Python)

**Programme:** Postgraduate Diploma (PGD) in Computer Science  
**Department of Computer Sciences, Olabisi Onabanjo University, Ago-Iwoye, Nigeria**  
**Course unit:** 3 (LH 30, PH 45) · **Language:** Python 3.10+ · **Platform:** Google Colab (or any Jupyter environment)

Hands-on lab notebooks for the 14-week course, one notebook per week, plus the student mini-project workbook.
Each notebook follows the same pattern: *concept recap → short labs → dry-run/trace → guided practice → class task →
assignment → reflection questions.*

Course lead: Dr. Sakinat Folorunso · sakinat.folorunso@oouagoiwoye.edu.ng

## Notebooks

Click a badge to open the notebook in Google Colab.

| Week | Topic | Open |
|---|---|---|
| 01 | Introduction to programming; how Python runs code | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week01_Introduction_to_Python.ipynb) |
| 02 | Problem solving, pseudocode and flowcharts | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week02_Algorithms_and_Problem_Solving.ipynb) |
| 03 | Variables, data types, input/output, f-strings | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week03_Python_Basics.ipynb) |
| 04 | Operators, precedence, expressions | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week04_Operators_and_Expressions.ipynb) |
| 05 | Decision making (`if`, `elif`, `else`) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week05_Decision_Making.ipynb) |
| 06 | Iteration I – `while`, input-validation loop | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week06_Iteration_While_Loop.ipynb) |
| 07 | Iteration II – `for`, `range`, `break`/`continue`, simulation | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week07_Iteration_For_Loop.ipynb) |
| 08 | Lists and tuples | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week08_Lists_and_Tuples.ipynb) |
| 09 | Dictionaries and sets; frequency counting | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week09_Dictionaries_and_Sets.ipynb) |
| 10 | Functions and modular programming | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week10_Functions_and_Modular_Programming.ipynb) |
| 11 | Strings, text processing, Unicode (Yorùbá example) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week11_Strings_and_Text_Processing.ipynb) |
| 12 | File handling and CSV | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week12_File_Handling.ipynb) |
| 13 | Error handling and debugging | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week13_Error_Handling_and_Debugging.ipynb) |
| 14 | Object-oriented programming and mini-project | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Week14_Intro_to_OOP_and_Mini_Project.ipynb) |
| Project | Mini-project workbook (student) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sakinat-Folorunso/cmp701-python-pgd/blob/main/notebooks/CMP701_Mini_Project_Student_Notebook.ipynb) |

See [`docs/COURSE_ALIGNMENT.md`](docs/COURSE_ALIGNMENT.md) for how each week maps to the course outline, assignments and learning outcomes.

## Working in Google Colab

* Files you create (`students.txt`, `scores.csv`, …) live on a **temporary** virtual machine. Mount Google Drive or download them if you need to keep them (Week 12 shows how).
* Run cells **top to bottom**; later cells depend on earlier ones.
* Several labs call `input()`; type your answer in the box that appears under the cell.

## Running the notebooks locally

```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install jupyterlab
jupyter lab notebooks/
```

## Automated check

`tests/check_notebooks.py` runs every code cell of every notebook with scripted input and fails if any cell raises an
uncaught exception. GitHub Actions runs it on each push (`.github/workflows/check-notebooks.yml`).

```bash
python tests/check_notebooks.py notebooks
```

## Academic integrity

Assignments and the mini-project are assessed individually. Use of AI assistants must be **declared** in the mini-project
(see the declaration cell at the end of the workbook). You must be able to explain every line you submit.

## Licence

*Add a `LICENSE` file before publishing.* Typical choices for course materials: **CC BY-NC-SA 4.0** for the notebooks'
text and **MIT** for the code. The choice is yours.
