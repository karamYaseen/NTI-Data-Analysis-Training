# Basic Dashboard — Kickstarter (my lab)

**My NTI coursework** — **Karam Yaseen.** **What I set out to do:** connect to **CSV** data, **shape** it in Power Query, build **KPIs and charts**, and keep **my** layout **easy to filter** with slicers — **my** way, not a template answer.

---

## Quick start

1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/).
2. Open a new report and **Get Data** → Text/CSV → files in `Kickstarter-Projects-Data/`.
3. Apply transforms (types, filters), load, then build visuals on a canvas background from `assets/`.
4. Save `Kickstarter Analytics Dashboard.pbix` and optional PNG exports for **my** portfolio.

**Deliverables**

- `Kickstarter Analytics Dashboard.pbix`
- Optional PNG exports (examples): `Kickstarter Analytics Dashboard - main.png`, `Kickstarter Analytics Dashboard - Detail.png`, `Kickstarter Analytics Dashboard - LastVersion.png`

**Charts to aim for (typical):** KPI row (project count, success rate, total raised USD), trend by month, breakdown by `main_category`, share by `state`, slicers (`main_category`, `country`, `state`, `currency`), optional map by country.

**Assets**

- **Canvas:** `assets/kickstarter_canvas_main.png`, `assets/kickstarter_canvas_detail.png` (minimal backgrounds — place real visuals on top)  
- **Optional mockups:** `kickstarter_EXPECTED_main.png` / `kickstarter_EXPECTED_detail.png` if **I** draw layout-only previews (not required)  
- **Icons:** `assets/icons/*.png` (transparent PNGs)

---

## Scenario

Explore Kickstarter crowdfunding: success vs failure, funding over time, breakdowns by category and geography.

---

## Dataset

| File | Description |
|------|-------------|
| `ks-projects-201612.csv` | Sample of projects (2016 export) |
| `ks-projects-201801.csv` | Sample of projects (2018 export) |

**Columns to know:** `ID`, `name`, `category`, `main_category`, `currency`, `deadline`, `goal`, `launched`, `pledged`, `state`, `backers`, `country`, `usd_pledged_real`, `usd_goal_real`

**CSV size:** large files — **I** can keep CSVs local and gitignore `Kickstarter-Projects-Data/*.csv`, or use [Git LFS](https://git-lfs.com/) if **I** want them in git.

---

## What I walked through

| Phase | What I did |
|-------|------------|
| **Connect** | Import CSVs; fix paths on **my** machine after clone |
| **Power Query** | Types, filters, columns **I** cared about; optional success/pledge calcs |
| **Report** | KPI row, trend, category, state/outcome, slicers — **my** layout |
| **QA** | Sanity checks; slicers behave; PNG export when **I** wanted one |

**Next (for me):** [`../02- Modeling/README.md`](../02-%20Modeling/README.md)

**Author:** Karam Yaseen — **my** dashboard, **my** trip.

**Parent:** [`../README.md`](../README.md)
