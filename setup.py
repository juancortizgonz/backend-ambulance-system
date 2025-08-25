import os
import subprocess
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
VENV_DIR = BASE_DIR / "venv"

def run_command(command, env=None):
    """Ejecuta un comando en la shell y muestra salida en tiempo real."""
    if isinstance(command, str):
        command = command.split()
    result = subprocess.run(command, env=env)
    if result.returncode != 0:
        print(f"Error ejecutando: {' '.join(command)}")
        sys.exit(result.returncode)

def main():
    print("Iniciando configuración del proyecto Django\n")

    # Create .env file if it doesn't exist
    if not VENV_DIR.exists():
        print("Creando entorno virtual...")
        run_command([sys.executable, "-m", "venv", str(VENV_DIR)])

    # Activate venv
    if os.name == "nt":  # Windows
        activate = VENV_DIR / "Scripts" / "activate"
    else:  # Linux / Mac
        activate = VENV_DIR / "bin" / "activate"

    env = os.environ.copy()
    env["VIRTUAL_ENV"] = str(VENV_DIR)
    env["PATH"] = f"{VENV_DIR}/bin:{env['PATH']}"

    print("Instalando dependencias...")
    run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], env=env)

    # Create migrations
    print("Creando migraciones...")
    run_command("python manage.py makemigrations", env=env)

    # Migrate database
    print("Aplicando migraciones...")
    run_command("python manage.py migrate", env=env)

    print("Creando o actualizando superusuario...")
    dj_user = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
    dj_email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    dj_pass = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin")

    superuser_script = """
    from django.contrib.auth import get_user_model
    User = get_user_model()
    u, created = User.objects.get_or_create(username="{username}", defaults={{"email": "{email}"}})
    u.is_superuser = True
    u.is_staff = True
    u.set_password("{password}")
    u.email = "{email}"
    u.save()
    print("Superuser", "created" if created else "updated", ":", u.username)
    """.format(
        username=dj_user,
        email=dj_email,
        password=dj_pass
    )

    run_command(f'echo "{superuser_script}" | python manage.py shell', env=env)


    # Load fixtures
    print("Cargando fixtures...")
    fixtures = [str(f) for f in Path("api/fixtures").glob("*.json")]
    if fixtures:
        run_command([sys.executable, "manage.py", "loaddata", *fixtures], env=env)
    else:
        print("No se encontraron fixtures en api/fixtures/")

    # Create groups
    print("Creando grupos...")
    run_command("python manage.py create_groups", env=env)

    print("\nConfiguración completada con éxito.")

if __name__ == "__main__":
    main()