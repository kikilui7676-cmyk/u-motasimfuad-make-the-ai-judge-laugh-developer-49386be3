import os
from pathlib import Path

LINE = "It worked on my machine — unfortunately, my machine is a 2019 laptop held together by stickers, and production is not."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
