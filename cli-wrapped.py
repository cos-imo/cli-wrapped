import os
import subprocess
import pyfiglet
from collections import Counter
from pathlib import Path

class CliWrapped:
    
    def __init__(self):
        self.home_directory = os.path.expanduser("~")
        self.commands = []
        self.open_file()
        self.parse_file()
        self.print_results()


    def select_file(self, founds):
        for i in range(len(founds)):
            print(f"\t[{i}] {founds[i]}")
        print(f"\t[{len(founds)}] Quit")
        entry = input(">>> ")
        try:
            entry = int(entry)
        except:
            print("Error: Please enter a correct file number")
            self.select_file()
        if entry in range(len(founds)):
            self.load_file(founds[entry])
        elif entry == (len(founds)):
            exit()
        else:
            print("Error: Please enter a correct file number")
            self.select_file()


    def open_file(self):
        result = subprocess.run(["ls", "-al", self.home_directory], capture_output=True, text=True)
        if result.returncode == 0:
            ls_results = [line.split(" ")[-1] for line in result.stdout.splitlines()]
        else:
            raise RuntimeError(f"Could not access your home directory. Error message:\n {result.stderr}")


        founds = []
        
        for file in ls_results:
            if "history" in file:
                founds.append(file)

        if len(founds) == 1:
            self.load_file(founds[0])
            exit(0)

        if len(founds) > 1:
            self.start_print()
            print("Multiples 'history' files have been found. Please select one:")
            self.select_file(founds)

        if len(founds) == 0:
            print("Error: no history file founds")
            exit(1)

    def load_file(self, file):
        try:
            file_path = self.home_directory  + "/" + file
            with open(file_path, 'r', encoding='utf-8', errors="ignore") as file:
                self.data = file.readlines()
        except:
            print("Error opening file.\nAborting")


    def parse_file(self):
        for line in self.data:
            if ";" in line:
                self.commands.append(line.split(";")[1].split(" ")[0])

if __name__=="__main__":
    cliwrapped = CliWrapped()
