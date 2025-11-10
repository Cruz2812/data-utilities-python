"""Compare two CSV snapshots by ID and report adds/removes/changes."""
import csv


def compare_csv_files(file1: str, file2: str, output_file: str):
    with open(file1, newline="", encoding="utf-8") as f1:
        reader1 = csv.reader(f1)
        headers1 = next(reader1)
        data1 = {row[1]: row for row in reader1}

    with open(file2, newline="", encoding="utf-8") as f2:
        reader2 = csv.reader(f2)
        headers2 = next(reader2)
        data2 = {row[1]: row for row in reader2}

    with open(output_file, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["id", "change"])

        for row_id in data2:
            if row_id not in data1:
                writer.writerow([row_id, "Added"])
            else:
                # assume count is in index 2
                c1 = int(data1[row_id][2])
                c2 = int(data2[row_id][2])
                if c2 > c1:
                    writer.writerow([row_id, f"Increased by {c2 - c1}"])
                elif c2 < c1:
                    writer.writerow([row_id, f"Decreased by {c1 - c2}"])

        for row_id in data1:
            if row_id not in data2:
                writer.writerow([row_id, "Removed"])


if __name__ == "__main__":
    compare_csv_files("snapshot1.csv", "snapshot2.csv", "comparison_results.csv")
