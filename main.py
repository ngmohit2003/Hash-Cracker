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

from flask import Flask, render_template, request, redirect, url_for, current_app
import os, traceback

# ... your existing imports and app definition ...

@app.route("/crack", methods=["POST"])
def crack():
    try:
        # If an uploaded file is present, save it; else use samples/hashes.txt
        uploaded = request.files.get("hashfile")
        if uploaded and uploaded.filename:
            save_path = os.path.join("samples", "uploaded_hashes.txt")
            uploaded.save(save_path)
            hashes_path = save_path
        else:
            hashes_path = os.path.join("samples", "hashes.txt")

        # Ensure the hashes file exists
        if not os.path.exists(hashes_path):
            error_msg = f"Hashes file not found: {hashes_path}"
            current_app.logger.error(error_msg)
            return render_template("results.html", error=error_msg, report=[], cracked=[])

        # Wordlist selection: use default local wordlist (change if you support remote URLs)
        wordlist = os.path.join("wordlists", "rockyou1.txt")
        if not os.path.exists(wordlist):
            current_app.logger.warning(f"Wordlist not found: {wordlist} (using simple fallback)")
            # fallback: create a tiny temporary wordlist to avoid crashing
            wordlist = None

        # Read hashes
        with open(hashes_path, "r", encoding="utf-8", errors="ignore") as f:
            hashes = [line.strip() for line in f if line.strip()]

        report = []
        cracked_passwords = []

        for h in hashes:
            # If you want remote streaming, call crack_hash(h, remote_url) instead
            if wordlist:
                result = crack_hash(h, wordlist)
            else:
                result = None  # no wordlist available

            status = "✅ " + result if result else "❌ Not Found"
            report.append([h, status])
            if result:
                cracked_passwords.append(result)

        # Save the report (your existing function expects report format)
        try:
            # If your report_writer.write_report expects a particular format, adapt below
            report_writer.write_report(report)
        except Exception as e:
            current_app.logger.warning("Failed to write report: " + repr(e))

        # compute stats in Python (avoid Jinja length errors)
        shortest = min(cracked_passwords, key=len) if cracked_passwords else None
        longest = max(cracked_passwords, key=len) if cracked_passwords else None
        avg_len = (sum(len(p) for p in cracked_passwords) / len(cracked_passwords)) if cracked_passwords else 0

        return render_template(
            "results.html",
            report=report,
            cracked=cracked_passwords,
            shortest=shortest,
            longest=longest,
            avg_len=avg_len,
            total=len(cracked_passwords),
            error=None
        )

    except Exception as e:
        # Log full traceback so Render logs show it
        current_app.logger.error("Exception in /crack: " + traceback.format_exc())
        return render_template("results.html", error=str(e), report=[], cracked=[])

# @app.route("/crack", methods=["POST"])
# def crack():
#     with open("samples/hashes.txt", "r") as f:
#         hashes = [line.strip() for line in f]

#     wordlist = "wordlists/rockyou1.txt"
#     report = []
#     cracked_passwords = []

#     for h in hashes:
#         result = crack_hash(h, wordlist)
#         status = "✅ " + result if result else "❌ Not Found"
#         report.append([h, status])
#         if result:
#             cracked_passwords.append(result)

#     shortest = min(cracked_passwords, key=len) if cracked_passwords else None
#     longest = max(cracked_passwords, key=len) if cracked_passwords else None
#     avg_len = sum(len(p) for p in cracked_passwords) / len(cracked_passwords) if cracked_passwords else 0

    # return render_template(
    #     "results.html",
    #     report=report,
    #     cracked=cracked_passwords,
    #     shortest=shortest,
    #     longest=longest,
    #     avg_len=avg_len,
    #     total=len(cracked_passwords)
    # )


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


