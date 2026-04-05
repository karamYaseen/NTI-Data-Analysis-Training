# Power BI — my NTI labs

This folder is **my personal Power BI coursework** for NTI — **not** a generic training bundle. The PBIX files, PNGs, assets, and notes here are **mine**: how **I** built each lab, **my** layouts, and **my** choices about what to commit.

---

## What I did here (in order)

| Folder | What I worked on |
|--------|------------------|
| [`01-Basic-Dashboard/`](01-Basic-Dashboard/) | My Kickstarter dashboard from CSV |
| [`02- Modeling/`](02-%20Modeling/) | My e‑commerce model + DAX (`Sales.xlsx`) |
| [`03- Direct Query/`](03-%20Direct%20Query/) | **My** Lab 3 — DirectQuery on AdventureWorks |
| [`04- Full Project/`](04-%20Full%20Project/) | **My** telecom churn BI project |

Folder names use a space after the number (e.g. `02- Modeling`); in links that’s `%20`.

**Note:** “Lab 3” for me lives under **`03- Direct Query/`**. The separate **[`06-Final-Project/`](../06-Final-Project/README.md)** at the repo root is **my Python capstone** — different track.

---

## What I used

| Tool | Where I used it |
|------|-----------------|
| [Power BI Desktop](https://powerbi.microsoft.com/desktop/) | All of my Power BI work here |
| SQL Server + [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) | My DirectQuery lab + churn SQL |
| AdventureWorks2019 OLTP | **My** Lab 3 — I restore it locally; I don’t depend on `.bak` in git (ignored) |

---

## Quick start (how I open these projects)

1. Install Power BI Desktop.  
2. For my labs 3–4: SQL Server + SSMS; I restore AdventureWorks using [Microsoft’s AdventureWorks docs](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms).  
3. Open each subfolder’s **README** — that’s **my** checklist for that lab.

**What I usually produce:** `.pbix` reports + optional PNGs for portfolio / LinkedIn.

---

## Icons & layout

I keep icons under each `assets/icons/` folder as **transparent** PNGs where possible. If Power BI shows a white box, I tweak **Format image → transparency** or swap the file.

Optional: add a `preview/` folder with a short README if you export a collage of module canvases for a portfolio.

---

**Parent:** [`../README.md`](../README.md)

**Author:** Karam Yaseen — **my** Power BI path through NTI, documented **my way**.
