import json
import sys

def extract_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    for i, cell in enumerate(nb.get("cells", [])):
        print(f"\n# ====== Cell {i+1} ({cell['cell_type']}) ======")
        print("".join(cell.get("source", [])))

if __name__ == "__main__":
    extract_notebook(sys.argv[1])
