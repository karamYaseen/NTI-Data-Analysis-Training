# Power BI — Data Visualization & Modeling

This section contains Power BI Desktop projects: a starter dashboard built on Kickstarter crowdfunding data, and a modeled sales report for e‑commerce-style analytics.

## Topics Covered

### 1. Basic Dashboard (Kickstarter)
- Connecting to CSV data and shaping it for reporting
- Building visuals: KPIs, trends, categories, and filters
- Publishing-style layout: one page “Kickstarter Analytics” story

### 2. Data Modeling (E‑Commerce Sales)
- Relating sales tables and measures (star/snowflake-style thinking in Power BI)
- DAX-friendly model: facts, dimensions, and business metrics
- Dashboard focused on sales performance (E‑Commerce Sales report)

## Projects in This Folder

### 01 — Basic Dashboard (`01-Basic-Dashboard/`)

| Item | Description |
|------|-------------|
| `Kickstarter Analytics Dashboard.pbix` | Main Power BI report file — open with **Power BI Desktop** |
| `Kickstarter Analytics Dashboard.png` | **Screenshot** of the dashboard (export from Power BI or place your own image here) |
| `Kickstarter-Projects-Data/` | Source CSVs: `ks-projects-201612.csv`, `ks-projects-201801.csv` |

**What you practiced:** loading real-world Kickstarter project data, cleaning/filtering in Power Query, and building a readable analytics dashboard.

**Dashboard preview**

![Kickstarter Analytics Dashboard](01-Basic-Dashboard/Kickstarter%20Analytics%20Dashboard.png)

---

### 02 — Modeling (`02- Modeling/`)

> **Rename tip:** Close Power BI if this folder is locked, then rename `02- Modeling` → `02-Modeling` for consistency with `01-Basic-Dashboard`.

| Item | Description |
|------|-------------|
| `E-Commerce Sales.pbix` | Main Power BI report — sales / e‑commerce modeling |
| `E-Commerce Sales.png` | **Screenshot** of the dashboard |
| `Sales.xlsx` | Excel source used in the model (as configured in the PBIX) |

**What you practiced:** data model relationships, measures, and a sales-focused dashboard.

**Dashboard preview**

![E-Commerce Sales](02-%20Modeling/E-Commerce%20Sales.png)

---

## Adding or Updating Screenshots

1. In Power BI Desktop: **File → Export → Export to PDF** or use **Snipping Tool** / **Win+Shift+S** for a PNG.
2. Save next to the matching `.pbix` with a clear name, e.g. `Kickstarter Analytics Dashboard.png`.
3. If you rename image files, update the `![alt](path)` lines above so the path matches (use `%20` for spaces in GitHub Markdown).

## Requirements

- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Windows)
- For refresh: same relative paths as in the PBIX, or **Transform data → Data source settings** after moving files

### Note (data folder name)

The Kickstarter CSV folder was renamed to `Kickstarter-Projects-Data` (was `Ks_Projects Data`). If **Refresh** fails, open the PBIX → **Transform data** → **Data source settings** → point to `01-Basic-Dashboard/Kickstarter-Projects-Data/` and the correct CSV files.

## Files in This Folder (overview)

- `README.md` — This documentation
- `01-Basic-Dashboard/` — Kickstarter analytics PBIX, PNG, and `Kickstarter-Projects-Data/` CSVs
- `02- Modeling/` — E‑Commerce Sales PBIX, PNG, and `Sales.xlsx`

## Learning Objectives

After working through these projects, you should be able to:

- Import and transform CSV/Excel data in Power Query
- Build interactive dashboards with filters and visuals
- Structure a simple data model and connect it to business questions
- Export and document work using PBIX files and dashboard screenshots

## Author

Karam Yaseen
