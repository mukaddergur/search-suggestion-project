from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.preprocess import build_search_data_csv


def main():
    output_path = build_search_data_csv("data", "search_data.csv")
    print(f"Dataset hazır: {output_path}")


if __name__ == "__main__":
    main()
