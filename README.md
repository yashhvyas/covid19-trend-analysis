 COVID-19 Data Cleaning Project

> My first real Data Analysis project | Python · Pandas

---

 What is this project?

This project takes a **raw messy COVID-19 CSV file** and cleans it step by step using Python — just like a real Data Analyst does at a company.

---

## 🗂️ Files in this project

| File | What it is |
|---|---|
| `covid19_raw.csv` | Original messy data — with all the problems |
| `covid19_cleaned.csv` | Final clean data — after fixing everything |
| `file.py` | Python script — every line has a comment explaining what it does |
| `README.md` | This file — explains the whole project |

---

## ❌ Problems found in the raw data

| Problem | Example |
|---|---|
| Duplicate rows | Same date and country appeared twice |
| Missing values | Blank cells in confirmed, deaths, recovered |
| Wrong date format | `2020/09/01` instead of `2020-09-01` |
| Inconsistent names | `india`, `INDIA`, `India` — all 3 in same file |

---

**Step 1 — Fixed country name spelling**
```python
df["country"] = df["country"].str.strip().str.title()
df["country"] = df["country"].replace("Usa", "USA")
```
`str.strip()` removes extra spaces. `str.title()` makes first letter capital.
So `india` → `India` and `INDIA` → `India`. Then fixed `Usa` → `USA`.

---

**Step 2 — Fixed date format**
```python
df["date"] = pd.to_datetime(df["date"], format="mixed")
```
Converts all dates to proper format so Python understands them as real dates, not just text.

---

**Step 3 — Removed duplicate rows**
```python
df = df.drop_duplicates()
```
Data went from **104 rows → 102 rows** after removing 2 duplicate rows.

---

**Step 4 — Filled empty cells**
```python
df[num_cols] = df[num_cols].fillna(0).astype(int)
```
All blank cells replaced with 0. No missing values left after this step.

---

**Step 5 — Added 2 new columns**
```python
df["mortality_rate"] = (df["deaths"] / df["confirmed"].replace(0, np.nan) * 100).round(2)
df["recovery_rate"]  = (df["recovered"] / df["confirmed"].replace(0, np.nan) * 100).round(2)
```
- **Mortality rate** = out of every 100 confirmed cases, how many died?
- **Recovery rate** = out of every 100 confirmed cases, how many recovered?

---

## Result after cleaning

| | Before | After |
|---|---|---|
| Rows | 104 | 102 |
| Null values | 13 | 0 |
| Columns | 6 | 8 |
| Duplicate rows | 2 | 0 |

---

##  Tools used

| Tool | Why I used it |
|---|---|
| Python 3 | Main programming language |
| Pandas | Loading, cleaning, and working with the data table |
| NumPy | Calculating mortality and recovery rate |

---

##  Biggest lesson

> Real data is never clean.
> The actual skill of a Data Analyst is finding hidden problems in raw data and fixing them.
> Anyone can make a chart. Not everyone can start from a broken file and make it analysis-ready.

---

##  About me

**Yash**
Aspiring Data Analyst | Python · Pandas · NumPy · Matplotlib
📍 Jamnagar, Gujarat, India
🔗 GitHub: www.linkedin.com/in/yash-vyas
🔗 LinkedIn:https://www.linkedin.com/in/yash-vyas
