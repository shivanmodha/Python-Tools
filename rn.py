import argparse
import ConColors
import os

parser = argparse.ArgumentParser(description="Batch file renamer")
parser.add_argument("--dir", type=str, help="Directory to find files", required=True)
parser.add_argument("--rein", type=str, help="Regex of files to match", required=True)
parser.add_argument("--reout", type=str, help="Regex of files to ")
parser.add_argument("--duplicate", help="Copy and rename (saving the original), rather than simply rename", action='store_true')
args = parser.parse_args()
DIRECTORY = args.dir if args.dir is not None else "."
DUPLICATE = args.duplicate if args.duplicate is not None else False

def main():
    if not os.path.isdir(DIRECTORY):
        return {"success": False, "message": "Directory doesn't exist"}
    return {"success": True, "message": "Successfully renamed files"}

if __name__ == "__main__":
    val = main()
    if val["success"]:
        print(ConColors.GREEN + val["message"] + ConColors.BLACK)
    else:
        print(ConColors.RED + val["message"] + ConColors.BLACK)
os.listdir()
