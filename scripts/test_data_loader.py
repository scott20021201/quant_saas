import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.data.data_loader import DataLoader


loader = DataLoader()

df = loader.load(
    "2330.TW",
    "2020-01-01",
    "2024-01-01"
)

print(df.head())
print(df.tail())