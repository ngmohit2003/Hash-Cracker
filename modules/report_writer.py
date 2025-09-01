import os

def write_report(report_data, path="reports/report.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write("🔐 CrackSuite - Password Cracking Report\n")
        f.write("========================================\n\n")
        for row in report_data:
            f.write(f"Hash: {row[0]}\nStatus: {row[1]}\n\n")
    print(f"\n📄 Report saved to: {path}")
