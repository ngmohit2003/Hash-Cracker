from modules import report_writer
from modules.cracker import crack_hash
from tabulate import tabulate
from termcolor import colored
from flask import Flask, render_template, request, redirect, url_for, cuurrent_app
import os, traceback
import sys

app = Flask(__name__)

# ---------------- Original CLI main() ----------------
def main():
    print("🔐 CrackSuite - Password Auditor\n")

    with open("samples/hashes.txt", "r") as f:
        hashes = [line.strip() for line in f]

    wordlist = "wordlists/rockyou1.txt"
    report = []
    cracked_passwords = []

    for h in hashes:
        result = crack_hash(h, wordlist)
        status = colored("✅ Cracked: " + result, "green") if result else colored("❌ Not Found", "red")

        report.append([h, status])
        if result:
            cracked_passwords.append(result)

    print(tabulate(report, headers=["Hash", "Status"]))
    report_writer.write_report(report)

    if cracked_passwords:
        print("\n📊 Cracked Password Stats:")
        lengths = [len(p) for p in cracked_passwords]
        print(f"Total Cracked: {len(cracked_passwords)}")
        print(f"Average Length: {sum(lengths) / len(lengths):.2f}")
        print(f"Shortest Password: {min(cracked_passwords, key=len)}")
        print(f"Longest Password: {max(cracked_passwords, key=len)}")


# ---------------- Flask Backend ----------------
@app.route("/")
def index():
    return render_template("index.html")
# @app.route("/", methods=["GET"])
# def home():
#     return render_template("index.html")

@app.route("/crack", methods=["POST"])
def crack():
    with open("samples/hashes.txt", "r") as f:
        hashes = [line.strip() for line in f]

    wordlist = "wordlists/rockyou1.txt"
    report = []
    cracked_passwords = []

    for h in hashes:
        result = crack_hash(h, wordlist)
        status = "✅ " + result if result else "❌ Not Found"
        report.append([h, status])
        if result:
            cracked_passwords.append(result)

    shortest = min(cracked_passwords, key=len) if cracked_passwords else None
    longest = max(cracked_passwords, key=len) if cracked_passwords else None
    avg_len = sum(len(p) for p in cracked_passwords) / len(cracked_passwords) if cracked_passwords else 0

    return render_template(
        "results.html",
        report=report,
        cracked=cracked_passwords,
        shortest=shortest,
        longest=longest,
        avg_len=avg_len,
        total=len(cracked_passwords)
    )


# ---------------- Entry Point ----------------
#if __name__ == "__main__":
 #   if len(sys.argv) > 1 and sys.argv[1] == "flask":
  #      app.run(host="0.0.0.0", port=5000, debug=True)
   # else:
    #    main()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "flask":
        import os
        port = int(os.environ.get("PORT", 5000))  # use Render's port, default 5000 locally
        app.run(host="0.0.0.0", port=port, debug=True)
    else:
        main()


