# Ciberseguridad 2026

## Integrantes
- Camilo Cifuentes
- Lucas Colomera
- Daniela Diaz
- Gustavo Pérez

Proyecto para analizar repositorios open source mediante:

- SBOMs con `Syft`
- análisis estático con `CodeQL`
- escaneo de dependencias con `Grype`

El flujo está pensado para ejecutarse dentro de un `Dev Container` en Visual Studio Code.

## Requisitos

Antes de comenzar, instala lo siguiente:

- `Docker Desktop`
- `Visual Studio Code`
- extensión `Dev Containers` de VS Code

Enlaces útiles:

- Docker: <https://www.docker.com/get-started>
- Visual Studio Code: <https://code.visualstudio.com/>
- Dev Containers: <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers>

## Clonar el repositorio

```bash
git clone https://github.com/Gape-mol/CiberSeg-T3
cd CiberSeg-T3
```

## Abrir el proyecto en Dev Container

1. Abre el proyecto en VS Code.
2. Presiona `Ctrl + Shift + P`.
3. Ejecuta `Dev Containers: Rebuild and Reopen in Container`.

La primera construcción puede tardar varios minutos porque instala Python, `uv`, `Syft`, `Grype`, `CodeQL` y Node.js.

## Estructura principal

```text
ciberseguridad_2026/
|- data/
|  |- repos/          # repositorios a analizar
|  |- results/        # resultados generados
|  `- repos.json      # lista de repositorios seleccionados
|- nbs/               # notebooks
|- scripts/           # automatización
`- README.md
```

## Seleccionar repositorios

La lista de repositorios se guarda en `data/repos.json`.

Si quieres generar esa lista automáticamente para una organización, usa:

```bash
uv run python scripts/obtain_repositories.py
```

Luego revisa que `data/repos.json` contenga los repositorios correctos y que la cantidad sea viable para el análisis.

## Agregar o sincronizar repositorios

Con la lista definida en `data/repos.json`, agrega o sincroniza los submódulos con:

```bash
uv run python scripts/add_submodules.py
git submodule update --init --recursive
```

Eso dejará los repositorios descargados dentro de `data/repos/`.

## Diagnóstico del entorno

Antes de ejecutar los análisis, conviene verificar que las herramientas estén disponibles.

```bash
uv run python scripts/generate_codeql.py --diagnose
uv run python scripts/generate_grype.py --diagnose
```

## Ejecutar análisis

### 1. Generar SBOMs

```bash
uv run python scripts/generate_sboms.py
```

Salida esperada en `data/results/`:

- `{repo}-sbom.json`

### 2. Ejecutar análisis estático con CodeQL

```bash
uv run python scripts/generate_codeql.py
```

Salida esperada en `data/results/`:

- `{repo}-codeql.json`

### 3. Escanear dependencias con Grype

```bash
uv run python scripts/generate_grype.py
```

Salida esperada en `data/results/`:

- `{repo}-grype.json`
- `{repo}-grype-raw.json`

## Flujo completo recomendado

Si quieres ejecutar el proyecto de principio a fin:

```bash
uv run python scripts/obtain_repositories.py
uv run python scripts/add_submodules.py
git submodule update --init --recursive
uv run python scripts/generate_sboms.py
uv run python scripts/generate_codeql.py
uv run python scripts/generate_grype.py
```

## Análisis en notebooks

Los notebooks están en `nbs/` y permiten revisar y analizar cuantitativamente los resultados generados.

Archivos relevantes:

- `nbs/sbom/generacion_sbom.ipynb`
- `nbs/vuln/generacion_codeql.ipynb`
- `nbs/vuln/generacion_grype.ipynb`

## Solución de problemas

### Docker no está corriendo

Abre Docker Desktop antes de reconstruir el contenedor.

### VS Code no detecta Dev Containers

Verifica que la extensión `Dev Containers` esté instalada.

### CodeQL o Grype no funcionan

Ejecuta primero:

```bash
uv run python scripts/generate_codeql.py --diagnose
uv run python scripts/generate_grype.py --diagnose
```
