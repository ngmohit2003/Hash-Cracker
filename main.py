from modules import report_writer
from modules.cracker import crack_hash
from tabulate import tabulate
from termcolor import colored  # ✅ moved here

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

if __name__ == "__main__":
    main()
