#!/usr/bin/env python3
"""Package a skill folder as <name>.skill (a zip with the folder at its root).

Usage: python3 package_skill.py <skill-folder> [output-dir]

Runs check_skill.py first and refuses to package if any ERROR remains.
"""

import subprocess
import sys
import zipfile
from pathlib import Path

SKIP_PARTS = {"__pycache__", "node_modules", ".git"}
SKIP_NAMES = {".DS_Store", "Thumbs.db"}


def main():
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        sys.exit(2)
    root = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 else Path.cwd()
    checker = Path(__file__).with_name("check_skill.py")

    result = subprocess.run([sys.executable, str(checker), str(root)])
    if result.returncode != 0:
        print("\nNot packaged: fix the ERRORs above first.")
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{root.name}.skill"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob("*")):
            rel = p.relative_to(root)
            if not p.is_file() or p.name in SKIP_NAMES or SKIP_PARTS & set(rel.parts):
                continue
            if rel.parts[0] == "evals":
                continue
            z.write(p, Path(root.name) / rel)
    print(f"\nPackaged: {out}")


if __name__ == "__main__":
    main()
