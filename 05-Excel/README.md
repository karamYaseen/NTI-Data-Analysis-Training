# Excel — my NTI track

**My personal coursework** — **Karam Yaseen.** This folder is **my** space for **Microsoft Excel** work that sits alongside the rest of the program: I use it for **imports**, **cleaning**, **pivot tables**, **charts**, and **short reports** when the brief asks for spreadsheets instead of (or before) SQL, Python, or Power BI.

It is **not** a full Excel course in a box — it is **how I** parked exercises, starter CSVs, and finished `.xlsx` files so **I** (and anyone browsing this repo) can see what I practiced and how I named things.

**Where I put this in my order:** I treat Excel as **parallel or in-between** material — often **after** I am comfortable opening data from [`../02-SQL/`](../02-SQL/) or alongside [`../03-Python/`](../03-Python/README.md) when I want a **quick pivot** without code. **After** spreadsheets, **my** main analytics path continued to [`../04-Power Bi/`](../04-Power%20Bi/README.md) and the capstone [`../06-Final-Project/`](../06-Final-Project/README.md).

---

## What lives in this folder

| Path / pattern | What it is for |
|----------------|----------------|
| **`README.md`** | This guide — how I use `05-Excel/`. |
| **`*.csv`** | Starter or practice data (e.g. imports, cleaning drills). |
| **`*.xlsx`** (if you add them) | **My** workbooks — solutions, dashboards-in-Excel, class submissions. |

Right now you may only see sample CSVs here; **I** add `.xlsx` files locally when the course asks for them and only commit them if they are small and worth sharing.

---

## How I work through an Excel task (guided checklist)

1. **Get the data** — CSV export from SQL, download from the LMS, or copy from a lab brief. Save it under **`05-Excel/`** with a **clear name** (see below).
2. **Import** — **Data** → **From Text/CSV** (or **Get Data**). Check **delimiter**, **encoding**, and **column types** in the preview.
3. **Clean** — Remove blanks, trim text, fix dates, split columns, remove duplicates. I often keep a **raw** sheet and a **clean** sheet so I can compare.
4. **Explore** — **PivotTable**: rows, columns, values (Sum / Average / Count). Slicers for filters.
5. **Visualize** — Insert **charts** that match the question (bar for categories, line for time, pie only when it really helps).
6. **Document** — Short note on the first sheet: **source**, **date**, **what I changed** — future me thanks me.

---

## Naming and repo hygiene

| Tip | Why |
|-----|-----|
| Use **`Topic_short_description.xlsx`** | Easier to find than `Book1.xlsx`. |
| Avoid spaces if you can | Fewer path issues in scripts and git. |
| Large files | If a workbook is **huge**, I keep a **sample** in git and note where the full file lives (OneDrive, local only). |
| Secrets | **Never** commit passwords, real customer IDs, or internal server names. |

---

## Skills I practice here (map to typical NTI-style labs)

| Skill | What I actually do in Excel |
|-------|-----------------------------|
| **Data → Get & transform** | Power Query: filter rows, change types, unpivot, merge queries. |
| **PivotTables** | Dimensions on rows/columns, measures as values, % of grand total. |
| **Functions** | `SUMIFS`, `COUNTIFS`, `XLOOKUP` / `VLOOKUP`, `IF`, dates with `TEXT` / `EOMONTH` where needed. |
| **Charts** | Axis titles, data labels only where readable, consistent colors. |
| **Conditional formatting** | Highlight top/bottom values, data bars for quick scans. |

---

## Linking to the rest of this repo

| If I… | I also look at… |
|-------|-----------------|
| Clean data here then analyze in Python | [`../03-Python/`](../03-Python/README.md) — same ideas, different tool. |
| Export aggregates for a report | [`../04-Power Bi/`](../04-Power%20Bi/README.md) — BI-grade visuals. |
| Need the full analytics capstone | [`../06-Final-Project/`](../06-Final-Project/README.md) — Python + notebook + Power BI story. |

---

## Quick reference — useful Excel shortcuts (Windows)

| Action | Shortcut |
|--------|----------|
| Create PivotTable from selection | `Alt` → `N` → `V` (varies by version) or **Insert** → **PivotTable** |
| Open Power Query Editor | **Data** → **Get Data** → **Launch Power Query Editor** |
| Fill down | Select range → `Ctrl` + `D` |

*(Exact keys depend on your Excel version and language; use **Tell me** search if unsure.)*

---

## If you are not me

You are welcome to copy the **folder idea**: one place for spreadsheet coursework, predictable names, and a short README so **you** remember what each file was for. This stays **my** archive — not official NTI curriculum.

---

**Parent:** [`../README.md`](../README.md)

**Author:** Karam Yaseen
