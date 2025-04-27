# Prompt 1 - Menysystem och tomma funktioner
import os

# Prompt 2 
import subprocess
import shutil

# Prompt 5 - integrera Prompt 4 i Prompt 1
def install_python():
    # Prompt 4 - Kontrollera om Python 3 finns
    if shutil.which("python3") is not None:
        print("Python 3 är redan installerat.")
        return

    print("Python 3 hittades inte. Försöker installera...")

    try:
        if os.name == "posix":
            if shutil.which("brew"):
                subprocess.run(["brew", "install", "python"], check=True)
            elif shutil.which("apt"):
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "python3"], check=True)
            else:
                print("Inget stödd installationsverktyg hittades. Installera Python manuellt.")
        else:
            print("Detta script stöder endast Linux/macOS för tillfället.")
    except subprocess.CalledProcessError:
        print("Ett fel inträffade vid installation av Python 3.")

# Prompt 3 - integrera Prompt 2 i Prompt 1
def install_vscode():
    # Prompt 2 - install_vscode-funktion
    if shutil.which("code") is not None:
        print("Visual Studio Code är redan installerat.")
        return

    print("Installerar Visual Studio Code...")

    try:
        # Kontrollera vilket OS som används
        if os.name == "posix":
            # macOS och de flesta Linux-distros
            if shutil.which("brew"):
                subprocess.run(["brew", "install", "--cask", "visual-studio-code"], check=True)
            else:
                print("Homebrew saknas. Installera Homebrew först för att fortsätta.")
        else:
            print("Detta script stöder endast Linux/macOS för tillfället.")
    except subprocess.CalledProcessError:
        print("Ett fel inträffade vid installation av Visual Studio Code.")

# Prompt 7 - integrera Prompt 6 i Prompt 1
def install_sqlite():
    # Prompt 6 - Kontrollera om SQLite är installerat
    if shutil.which("sqlite3") is not None:
        print("SQLite är redan installerat.")
        return

    print("SQLite hittades inte. Försöker installera...")

    try:
        if os.name == "posix":
            if shutil.which("brew"):
                subprocess.run(["brew", "install", "sqlite"], check=True)
            elif shutil.which("apt"):
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "sqlite3"], check=True)
            else:
                print("Inget stödd installationsverktyg hittades. Installera SQLite manuellt.")
        else:
            print("Detta script stöder endast Linux/macOS för tillfället.")
    except subprocess.CalledProcessError:
        print("Ett fel inträffade vid installation av SQLite.")

# Prompt 9 - integrera Prompt 8 i Prompt 1
def install_discord():
    # Prompt 8 - Kontrollera om Discord är installerat
    if shutil.which("discord") is not None:
        print("Discord är redan installerat.")
        return

    print("Discord hittades inte. Försöker installera...")

    try:
        if os.name == "posix":
            if shutil.which("brew"):
                # macOS med Homebrew
                subprocess.run(["brew", "install", "--cask", "discord"], check=True)
            elif shutil.which("apt"):
                # Linux med apt (installerar Discord via Snap eftersom Discord inte alltid finns i vanliga apt-källor)
                subprocess.run(["sudo", "snap", "install", "discord"], check=True)
            else:
                print("Inget stödd installationsverktyg hittades. Installera Discord manuellt.")
        else:
            print("Detta script stöder endast Linux/macOS för tillfället.")
    except subprocess.CalledProcessError:
        print("Ett fel inträffade vid installation av Discord.")

def create_project_structure():
    # Prompt 1 - create_project_structure-funktion
    home = os.path.expanduser("~")
    private_path = os.path.join(home, "Projects", "Privat")
    jobb_path = os.path.join(home, "Projects", "Jobb")
    os.makedirs(private_path, exist_ok=True)
    os.makedirs(jobb_path, exist_ok=True)
    print(f"Skapade mappar:\n{private_path}\n{jobb_path}")

def main_menu():
    # Prompt 1 - huvudmeny
    while True:
        print("\n--- Installationsmeny ---")
        print("1. Installera Python")
        print("2. Installera Visual Studio Code")
        print("3. Installera SQLite")
        print("4. Installera Discord")
        print("5. Skapa projektmappar")
        print("6. Installera ALLT")
        print("0. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            install_python()
        elif choice == "2":
            install_vscode()
        elif choice == "3":
            install_sqlite()
        elif choice == "4":
            install_discord()
        elif choice == "5":
            create_project_structure()
        elif choice == "6":
            install_python()
            install_vscode()
            install_sqlite()
            install_discord()
            create_project_structure()
        elif choice == "0":
            print("Avslutar...")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main_menu()
