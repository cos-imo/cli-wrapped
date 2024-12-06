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



if __name__=="__main__":
    cliwrapped = CliWrapped()
