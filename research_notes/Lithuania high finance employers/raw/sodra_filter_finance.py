"""Filter Sodra open per-employer monthly data for finance EVRK codes.

The download was NOT possible from the research sandbox: the egress proxy
refused atvira.sodra.lt, data.gov.lt and rekvizitai.vz.lt (403). Run this script
locally. The URL pattern below is UNVERIFIED. If it fails, open
https://atvira.sodra.lt/imones/rinkiniai/index.html and copy the current link
for the monthly CSV/ZIP.

Usage: python -I sodra_filter_finance.py monthly-2026.csv.zip [min_avg_wage]
"""
import csv, io, sys, zipfile

URL_HINT = "https://atvira.sodra.lt/imones/downloads/2026/monthly-2026.csv.zip"  # unverified
PREFIXES = ("64", "65", "66", "70.22", "702200", "46.12", "461200", "35.14", "351400")

def main(path, min_wage=5000.0):
    zf = zipfile.ZipFile(path)
    name = zf.namelist()[0]
    raw = zf.read(name).decode("utf-8-sig", errors="replace")
    delim = ";" if raw[:2000].count(";") > raw[:2000].count(",") else ","
    rows = list(csv.DictReader(io.StringIO(raw), delimiter=delim))
    cols = rows[0].keys()
    print("columns:", list(cols))
    # Sodra columns typically include an activity code (ecoActCode), avgWage, numInsured, month.
    code_col = next(c for c in cols if "ecoact" in c.lower() and "code" in c.lower())
    wage_col = next(c for c in cols if c.lower().startswith("avgwage"))
    num_col = next(c for c in cols if c.lower().startswith("numinsured"))
    out = []
    for r in rows:
        code = (r[code_col] or "").strip()
        if not code.startswith(PREFIXES):
            continue
        try:
            w = float((r[wage_col] or "0").replace(",", "."))
        except ValueError:
            continue
        if w >= min_wage:
            out.append((w, r))
    out.sort(key=lambda x: -x[0])
    w = csv.writer(sys.stdout)
    w.writerow(list(cols))
    for _, r in out:
        w.writerow([r[c] for c in cols])

if __name__ == "__main__":
    main(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 5000.0)
