import argparse
import ConColors
import os
import re
import json
from shutil import copyfile, move

parser = argparse.ArgumentParser(description="Batch file renamer")
parser.add_argument("--dir", type=str, help="Directory to find files", nargs="+", required=True)
parser.add_argument("--rein", type=str, help="Regex of files to match", nargs="+", required=True)
parser.add_argument("--reout", type=str, help="Name of the output file", nargs="+", required=True)
parser.add_argument("--delim", type=str, help="Split input string delim", nargs="+")
parser.add_argument("--duplicate", help="Copy and rename (saving the original), rather than simply rename", action="store_true")
parser.add_argument("--preview", help="Test your inputs without actually renaming any files", action="store_true")
args = parser.parse_args()

directory = args.dir if args.dir is not None else []
DIRECTORY = ""
for i in directory:
    DIRECTORY += i + " "
DIRECTORY = DIRECTORY[:-1]
args.dir = DIRECTORY

DUPLICATE = args.duplicate if args.duplicate is not None else False

rein = args.rein
REIN = ""
for i in rein:
    REIN += i + " "
REIN = REIN[:-1]
args.rein = REIN

reout = args.reout
REOUT = ""
for i in reout:
    REOUT += i + " "
REOUT = REOUT[:-1]
args.reout = REOUT

delim = args.delim
DELIM = ""
for i in delim:
    DELIM += i + " "
DELIM = DELIM[:-1]
args.delim = DELIM

PREVIEW = args.preview
def main():
    if PREVIEW:
        print(ConColors.BLUE + "Executing script in preview mode" + ConColors.BLACK)
    renameDict = {}
    if not os.path.isdir(DIRECTORY):
        return {"success": False, "message": "Directory doesn't exist"}
    dirListing = os.listdir(DIRECTORY)
    for file in dirListing:
        if re.match(REIN, file):
            parse = [file]
            if DELIM is not None:
                parse = re.split(DELIM, file)
            for i in range(0, len(parse)):
                try:
                    parse[i] = int(parse[i])
                except:
                    pass
            newName = REOUT.format(*parse)
            renameDict[file] = newName
            print("    " + ConColors.YELLOW + file + ConColors.BLACK + ": " + ConColors.GREEN + newName + ConColors.BLACK)
    if not PREVIEW:
        for key in renameDict:
            value = renameDict[key]
            oldPath = DIRECTORY + key
            newPath = DIRECTORY + value
            if DUPLICATE:
                copyfile(oldPath, newPath)
            else:
                move(oldPath, newPath)
            
    return {"success": True, "message": "Successfully renamed files"}

if __name__ == "__main__":
    val = main()
    if val["success"]:
        print(ConColors.GREEN + val["message"] + ConColors.BLACK)
    else:
        print(ConColors.RED + val["message"] + ConColors.BLACK)
os.listdir()
