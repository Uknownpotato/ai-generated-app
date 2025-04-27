# ai-generated-app

## Beskrivning
Detta projekt är ett experiment där en applikation skapades nästan helt genom AI-genererade prompts och kod.
Applikationen är ett installationsscript som hjälper dig att snabbt sätta upp en utvecklardator genom att installera viktiga verktyg och skapa en projektmappstruktur.

## Funktioner
- Installera Python 3 (om inte redan installerat)
- Installera Visual Studio Code (via Homebrew)
- Installera SQLite (via Homebrew eller apt)
- Installera Discord (via Homebrew eller Snap)
- Skapa projektmappar:
  - `~/Projects/Privat`
  - `~/Projects/Jobb`
- Textbaserad meny (TUI) för att välja installationer

## Systemkrav
- Linux eller macOS
- Python 3 installerat (krävs för att köra detta script)
- Homebrew (macOS) eller apt (Linux) installerat för programinstallationer
- Snap installerat (Linux) om du vill installera Discord

## Installation
1. Klona detta repo:
   ```bash
   git clone https://github.com/ditt-användarnamn/ai-generated-app.git
   cd ai-generated-app
2. Kör scriptet:
   ```bash
   python3 main.py

## Användning
- Installera varje verktyg individuellt
- Installera alla verktyg samtidigt
- Skapa projektmappar
- Avsluta scriptet

## Noteringar
- Om Homebrew eller Snap inte är installerade måste de installeras manuellt innan vissa program kan installeras
- Scriptet är utvecklat som ett utbildningsexperiment och vissa installationer kan kräva ytterligare manuell konfiguration beroende på ditt system

## Licens
MIT License - se LICENSE-filen för mer information.
