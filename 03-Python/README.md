# Python — NTI Data Analysis Training

This folder is the **Python track**: basics through NumPy/Pandas/plots and a final recap (SQL, scraping, automation). The main narrative lives in one script.

---

## Run the full tutorial

From the **`03-Python`** directory (so outputs land next to the script):

```bash
cd 03-Python
pip install -r ../requirements.txt
python tutorial.py
```

`tutorial.py` walks through the course with comments and examples. It may write plots, CSVs, Excel files, and reports in this folder (see below).

---

## Course map

| Block | Folder | Topics |
|-------|--------|--------|
| Day 1 | [`01-Python-Basics/`](01-Python-Basics/) | Types, strings, lists, tuples, exercises |
| Day 2 | [`02-Sequences/`](02-Sequences/) | Sets, dicts, control flow, exceptions, exercises |
| Day 3 | [`03-Functions-OOP/`](03-Functions-OOP/) | Functions, lambdas, classes, exercises |
| Day 4 | [`04-NumPy-Pandas-Plotting/`](04-NumPy-Pandas-Plotting/) | NumPy, Pandas, Matplotlib, automation samples |
| Recap | [`05-Recap-Task/`](05-Recap-Task/) | SQL + Pandas, scraping, regex, assignment |

---

## What `tutorial.py` includes

- Step-by-step explanations and runnable samples  
- Progressive difficulty (basics → automation)  
- Optional outputs: charts, CSV/Excel, text reports (see next section)  
- Practice-style checkpoints and ideas for your own mini-projects  

---

## Generated files (optional)

If the script reaches those sections, you may see files such as:

| File pattern | Role |
|--------------|------|
| `tutorial_advanced_plots.png` | Matplotlib figures |
| `tutorial_scraped_quotes.csv` | Scraping demo |
| `tutorial_products.xlsx` | Excel read/write demo |
| `tutorial_employee_data.csv`, `tutorial_department_summary.xlsx` | Pipeline / pivot demos |
| `tutorial_compensation_report.txt` | Text report |
| `tutorial_quotes_<timestamp>.csv`, `tutorial_employee_report_<timestamp>.xlsx` | Timestamped exports |

The repo root **`.gitignore`** ignores these patterns so generated files are not committed by mistake. Re-run `tutorial.py` anytime to regenerate.

---

**Author:** Karam Yaseen
