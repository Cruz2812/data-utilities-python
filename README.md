# Data Utilities (Python)

A collection of small, production-friendly Python scripts for working with CSV, Excel, JSON, and email-derived data.

## Scripts
- `parse_email_domains.py` — reads an `emails.csv` file and extracts email → domain mappings into a clean DataFrame.
- `compare_csv_changes.py` — compares two CSV snapshots and reports added/removed/increased/decreased rows.
- `combine_csv_files.py` — walks a directory and concatenates all CSVs into one file.
- `split-excel-rows.py` — takes an Excel workbook and exports each data row into its own file (great for label recommendation testing).
- `json-to-excel-report-builder.py` — converts exported JSON reports into multi-sheet, formatted Excel workbooks.
- `regex-data-generation.py` — generates sample data from regexes to test Sensitive Information Types (SITs).
- `jupyter_env_troubleshooting.py` — helper to print Python executable, installed packages, and environment info.

## Requirements
```bash
pip install pandas openpyxl chardet
