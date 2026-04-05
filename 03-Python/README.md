# Python — my NTI track

**My personal coursework** — **Karam Yaseen.** This is **my** Python path: **basics → NumPy/Pandas/plots → recap** (SQL from Python, scraping, automation). I drive most of the narrative from **`tutorial.py`**; the day folders are **my** exercises and notes.

I came here after [`../01-Database-Design/`](../01-Database-Design/) and [`../02-SQL/`](../02-SQL/) in **my** order. **After this folder**, **my** next step was [`../04-Power Bi/`](../04-Power%20Bi/README.md).

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
- Practice-style checkpoints and ideas for **my** side mini-projects  

---

## Generated files (optional)

When **I** ran those sections, **I** sometimes saw files like:

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

**Capstone (after the Python track):** [`../06-Final-Project/README.md`](../06-Final-Project/README.md) — script + notebook.

**Parent:** [`../README.md`](../README.md)

**Author:** Karam Yaseen
