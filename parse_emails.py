"""Parse an email CSV and extract unique email-domain pairs."""
import csv
import pandas as pd


def parse_emails(input_file: str = "emails.csv") -> pd.DataFrame:
    domains_by_email = {}
    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            email_str = ";".join(
                filter(
                    None,
                    [
                        row.get("from"),
                        row.get("to"),
                        row.get("cc"),
                        row.get("bcc"),
                    ],
                )
            )
            emails = [e.strip() for e in email_str.split(";") if e.strip()]
            for email in emails:
                if "@" in email:
                    domain = email.split("@")[-1].lower()
                    domains_by_email[email] = domain

    df = pd.DataFrame([{"email": email, "domain": domain} for email, domain in domains_by_email.items()])
    return df


if __name__ == "__main__":
    df = parse_emails()
    print(df)
