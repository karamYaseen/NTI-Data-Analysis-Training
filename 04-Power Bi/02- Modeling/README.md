# E‑Commerce modeling — my Power BI lab

**My NTI coursework** — **Karam Yaseen.** **What I set out to do:** import **`Sales.xlsx`**, build **my** star schema, write **my** DAX measures, and ship a sales dashboard **my** way.

---

## Quick start (how I built it)

1. Power BI Desktop → **Get Data** → Excel → `Sales.xlsx`.
2. **Model view:** relate fact ↔ dimensions (many-to-one from fact) **as I defined them**.
3. **Date table** when the lab called for time intelligence — **I** mark it as a date table.
4. Measures (sales, quantity, profit, margin — **my** formulas) on `assets/ecommerce_canvas_*.png` backgrounds.

**What I produced:** `E-Commerce Sales.pbix`, plus optional PNGs (e.g. `E-Commerce Sales - main.png`, `E-Commerce Sales - Details.png`) for **my** portfolio.

**Charts I aimed for:** KPI cards, sales over time, category/segment breakdowns, matrix or table for top products — **my** layout choices.

**Assets**

- **Canvas:** `assets/ecommerce_canvas_main.png`, `assets/ecommerce_canvas_detail.png`  
- **Optional mockups:** `ecommerce_EXPECTED_main.png`, `ecommerce_EXPECTED_detail.png` (not required)  
- **Icons:** `assets/icons/*.png`

---

## What this lab was about (for me)

**I** practiced dimensional modeling: fact at line/order grain, product + customer dimensions, DAX for KPIs and margins — **my** interpretation of the brief.

---

## Dataset

| File | Description |
|------|-------------|
| `Sales.xlsx` | Orders / lines, customers, products (exact sheets vary by export) |

**Model focus:** facts (amounts, quantities, dates) vs dimensions (product hierarchy, customer segment); **DAX** for totals, counts, and profit.

---

## What I walked through

| Phase | What I delivered |
|-------|------------------|
| **Load** | Import Excel; **Transform Data** **my** way; fix paths when **I** cloned on a new PC |
| **Model** | **My** star schema, relationships, hierarchies where **I** wanted them |
| **DAX & report** | **My** measure table; cards, trends, breakdowns, slicers |
| **QA** | **I** checked visuals vs measures; titles and colors **I** liked |

**Previous:** [`../01-Basic-Dashboard/README.md`](../01-Basic-Dashboard/README.md) · **Next:** [`../03- Direct Query/README.md`](../03-%20Direct%20Query/README.md)

**Author:** Karam Yaseen — **my** lab, **my** report.

**Parent:** [`../README.md`](../README.md)
