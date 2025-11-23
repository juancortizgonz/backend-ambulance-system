#!/bin/bash

set -euo pipefail

# Actualizar e Instalar Paquetes Base
echo "## Actualizando lista de paquetes e instalando actualizaciones..."
sudo apt update
sudo apt upgrade -y
echo "-----"

# Instalar dependencias necesarias (git, redis, postgres, python venv)
echo "## Instalando Git, Redis-server y PostgreSQL..."
sudo apt install -y git redis-server postgresql postgresql-contrib python3.12-venv
echo "-----"

# Clonar Repositorio Git
echo "## Clonando el repositorio Git"
REPO_URL="https://github.com/juancortizgonz/backend-ambulance-system.git"
REPO_DIR="backend-ambulance-system"

if [ -d "$REPO_DIR" ]; then
    echo "Directorio $REPO_DIR ya existe. Saltando la clonación. Por favor, elimínelo si desea clonar de nuevo."
else
    # Se requiere que la clave SSH para GitHub esté configurada en el sistema
    git clone "$REPO_URL"
    if [ $? -eq 0 ]; then
        echo "Repositorio clonado exitosamente."
    else
        echo "Error al clonar el repositorio."
    fi
fi
echo "-----"

# Configurar e Iniciar Redis
echo "## Configurando e iniciando Redis-server..."
# Verificamos el estado para confirmar
REDIS_STATUS=$(sudo systemctl is-active redis-server)
if [ "$REDIS_STATUS" = "active" ]; then
    echo "✅ Redis-server ya está activo."
else
    echo "Iniciando Redis-server..."
    sudo systemctl start redis-server
    sudo systemctl enable redis-server
    if [ $? -eq 0 ]; then
        echo "Redis-server iniciado y habilitado."
    else
        echo "Error al iniciar Redis-server."
    fi
fi
echo "-----"

# Configurar e Iniciar PostgreSQL
echo "## Configurando e iniciando PostgreSQL..."
# Verificamos el estado para confirmar
POSTGRES_STATUS=$(sudo systemctl is-active postgresql)
if [ "$POSTGRES_STATUS" = "active" ]; then
    echo "PostgreSQL ya está activo."
else
    echo "Iniciando PostgreSQL..."
    sudo systemctl start postgresql
    sudo systemctl enable postgresql
    if [ $? -eq 0 ]; then
        echo "PostgreSQL iniciado y habilitado."
    else
        echo "Error al iniciar PostgreSQL."
    fi
fi

# Preguntar por la contraseña del usuario 'postgres'
echo "-----"
echo "## Configurando la contraseña del usuario 'postgres' en PostgreSQL..."
read -s -p "Introduce la NUEVA contraseña para el usuario 'postgres' de la base de datos: " POSTGRES_PASS
echo ""

# Cambiar la contraseña del usuario 'postgres'
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD '$POSTGRES_PASS';"

if [ $? -eq 0 ]; then
    echo "Contraseña del usuario 'postgres' actualizada exitosamente."
else
    echo "Error al actualizar la contraseña del usuario 'postgres'. Asegúrate de que el servicio está activo."
fi
echo "-----"

echo "🎉 **Configuración inicial completada.**"
echo "🎉 **Por favor ejecuta 'python3 setup.py' para configurar el ambiente en python**"