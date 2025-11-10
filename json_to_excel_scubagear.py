"""Convert all JSON exports in a folder to formatted Excel workbooks."""
import os
import json
import chardet
import pandas as pd
from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo


def detect_encoding(file_path: str) -> str:
    with open(file_path, "rb") as f:
        raw = f.read()
    result = chardet.detect(raw)
    return result["encoding"] or "utf-8"


def json_to_excel(folder_path: str):
    for filename in os.listdir(folder_path):
        if not filename.endswith(".json"):
            continue
        json_path = os.path.join(folder_path, filename)
        encoding = detect_encoding(json_path)
        with open(json_path, "r", encoding=encoding) as f:
            data = json.load(f)

        sheet_name = filename.replace(".json", "")
        excel_path = os.path.join(folder_path, f"{sheet_name}.xlsx")

        with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
            startrow = 0
            report_summary = data[0].get("ReportSummary", {})
            if report_summary:
                summary_df = pd.DataFrame([report_summary])
                summary_df.to_excel(writer, sheet_name=sheet_name, startrow=startrow, index=False)
                startrow += len(summary_df) + 2

            for group in data[0].get("Results", []):
                group_name = group.get("GroupName", "Group")
                controls = group.get("Controls", [])
                controls_df = pd.DataFrame(controls)
                controls_df.to_excel(writer, sheet_name=sheet_name, startrow=startrow, index=False)
                # merge title row via openpyxl after save
                startrow += len(controls_df) + 2

        # optional: post-formatting can be added here


if __name__ == "__main__":
    json_to_excel("<input_folder_path>")
