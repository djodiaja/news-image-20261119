"""Entry program: copy the rendered 19 November 2026 front page to /output/entry.png."""
import shutil
from pathlib import Path

if __name__ == "__main__":
    out = Path("/output/entry.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path(__file__).resolve().parent / "assets" / "entry.png", out)
