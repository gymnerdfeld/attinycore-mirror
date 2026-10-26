# Mirror von ATTinyCore 1.5.2

Dieser Ordner wird als eigenes GitHub-Repository mit GitHub Pages veröffentlicht. Er stellt das Board-Paket ATTinyCore 1.5.2 für die Arduino IDE bereit, unabhängig von `drazzy.com` und `azduino.com`.

## Inhalt

| Datei | Inhalt |
|---|---|
| `package_attinycore-mirror_index.json` | Paketverzeichnis, das die Arduino IDE liest. Wird von `make_index.py` erzeugt. |
| `archive/` | Unveränderte Kopien von ATTinyCore 1.5.2 und dem Micronucleus-Werkzeug 2.5-azd1b für alle Plattformen |
| `original-eintrag.json` | Auszug aus `package_drazzy.com_index.json` mit den Original-Adressen und Prüfsummen |
| `make_index.py` | Erzeugt das Paketverzeichnis für eine bestimmte Adresse und prüft die Archive |

Compiler (`avr-gcc`) und `avrdude` sind nicht im Mirror. Die Arduino IDE lädt sie von Arduino.

## Einrichten

1. Auf GitHub ein öffentliches Repository anlegen, zum Beispiel `attinycore-mirror`.
2. Das Paketverzeichnis für die künftige Adresse erzeugen:

   ```
   python make_index.py https://<github-name>.github.io/attinycore-mirror
   ```
3. Den Inhalt dieses Ordners in das Repository hochladen.
4. Im Repository unter *Settings › Pages* als Quelle den Branch `main` und den Ordner `/ (root)` wählen.
5. Nach ein bis zwei Minuten prüfen, ob `https://<github-name>.github.io/attinycore-mirror/package_attinycore-mirror_index.json` im Browser erscheint.
6. Diese Adresse im Handout `03-basic-version/arduino-ide-einrichten.typ` und im Haupt-README eintragen.

## Testen

In der Arduino IDE die offizielle Adresse von drazzy.com aus den Einstellungen entfernen, ATTinyCore deinstallieren, die Mirror-Adresse eintragen und ATTinyCore neu installieren.

Ohne Arduino IDE geht es mit `arduino-cli` und einem leeren Datenordner:

```
set ARDUINO_DIRECTORIES_DATA=C:\temp\ac
set ARDUINO_BOARD_MANAGER_ADDITIONAL_URLS=https://<github-name>.github.io/attinycore-mirror/package_attinycore-mirror_index.json
arduino-cli core update-index
arduino-cli core install ATTinyCore:avr
```

Im Oktober 2026 wurde so eine Installation über einen lokalen Webserver getestet.

## Lizenzen

- ATTinyCore: LGPL 2.1, Quelle <https://github.com/SpenceKonde/ATTinyCore>
- Micronucleus: GPL 2, Quelle <https://github.com/micronucleus/micronucleus>, Build 2.5-azd1b von Spence Konde

Die Archive sind unverändert. Ihre Prüfsummen entsprechen dem offiziellen Paketverzeichnis.
