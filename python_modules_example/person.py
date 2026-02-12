import argparse


parser = argparse.ArgumentParser(description="Display personal information")

parser.add_argument("nume", help="Last name")
parser.add_argument("prenume", help="First name")
parser.add_argument("varsta", type=int, help="Age")

args = parser.parse_args()

print(f"Nume: {args.nume}")
print(f"Prenume: {args.prenume}")
print(f"Varsta: {args.varsta} ani")
