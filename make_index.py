"""Erzeugt das Paketverzeichnis für den Mirror von ATTinyCore 1.5.2.

Aufruf:  python make_index.py https://<github-name>.github.io/<repo-name>

Liest original-eintrag.json (Auszug aus package_drazzy.com_index.json),
ersetzt die Download-Adressen durch Adressen im Ordner archive/ des Mirrors
und schreibt package_attinycore-mirror_index.json. Prüfsummen und Grössen
bleiben unverändert, sie werden gegen die Dateien in archive/ geprüft.
"""

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
SOURCE = HERE / "original-eintrag.json"
TARGET = HERE / "package_attinycore-mirror_index.json"
ARCHIVE = HERE / "archive"


def check(entry):
    path = ARCHIVE / entry["archiveFileName"]
    data = path.read_bytes()
    checksum = "SHA-256:" + hashlib.sha256(data).hexdigest()
    if checksum != entry["checksum"] or str(len(data)) != str(entry["size"]):
        sys.exit(f"Prüfsumme oder Grösse stimmt nicht: {path.name}")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    base = sys.argv[1].rstrip("/") + "/archive/"

    index = json.loads(SOURCE.read_text(encoding="utf-8"))
    for package in index["packages"]:
        for entry in package["platforms"]:
            check(entry)
            entry["url"] = base + entry["archiveFileName"]
        for tool in package["tools"]:
            for entry in tool["systems"]:
                check(entry)
                entry["url"] = base + entry["archiveFileName"]

    TARGET.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{TARGET.name} geschrieben.")


if __name__ == "__main__":
    main()
