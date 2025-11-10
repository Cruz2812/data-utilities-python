"""Generate sample data CSVs from regex definitions for SIT testing."""
import csv
import random
import os
import exrex  # make sure exrex is installed


def generate_data(regex: str, keywords: list[str]) -> str:
    sample = exrex.getone(regex)
    keyword = random.choice(keywords) if keywords else ""
    return f"{keyword} {sample}".strip()


def generate_csv(input_file: str, output_file: str, samples: int = 10):
    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    keywords = [r.get("Keyword", "") for r in rows if r.get("Keyword")]

    out_name = f"{output_file}_SampleData.csv"
    with open(out_name, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        headers = ["Regex"] + [f"Sample Data {i+1}" for i in range(samples)]
        writer.writerow(headers)

        for r in rows:
            regex = r["Regex"]
            samples_list = [generate_data(regex, keywords) for _ in range(samples)]
            writer.writerow([regex] + samples_list)


def generate_csv_no_keyword(input_file: str, output_file: str, samples: int = 50):
    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    out_name = f"{output_file}_SampleData.csv"
    with open(out_name, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        headers = ["Regex"] + [f"Sample Data {i+1}" for i in range(samples)]
        writer.writerow(headers)

        for r in rows:
            regex = r["Regex"]
            samples_list = [exrex.getone(regex) for _ in range(samples)]
            writer.writerow([regex] + samples_list)


if __name__ == "__main__":
    # Example usage
    # generate_csv("CreditCard_regex.csv", "CreditCardNumber")
    pass
