from pathlib import Path

ROOT = Path(__file__).parent.parent
PROCESSED = ROOT / "processed"
ANALYSIS = ROOT / "analysis"
OUTPUTS = ROOT / "outputs"

VIDEOS_CSV = PROCESSED / "videos.csv"
CHANNELS_CSV = PROCESSED / "channels.csv"

INSTITUTIONAL = {"Stanford", "MIT", "EPFL", "ETH Zürich"}
INDEPENDENT = {"Kurzgesagt", "3Blue1Brown", "minutephysics", "Veritasium"}

PERSON2_DIR = ANALYSIS / "person2_titles_thumbnails"
THUMBNAILS_DIR = PERSON2_DIR / "thumbnails"
THUMBNAILS_DIR.mkdir(parents=True, exist_ok=True)
