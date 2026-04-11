# 🔐 Ciberseguridad 2026 - Análisis de Seguridad

¡Bienvenido! Este proyecto automatiza la evaluación de repositorios mediante **SBOM** (Software Bill of Materials) y **CodeQL**.

💡 **Tip:** Presiona **Ctrl + Shift + V** (o **Cmd + Shift + V** en Mac) para leer este documento en modo vista previa.

Si todo ha salido bien entonces en este momento se esta realizando la construcción del contenedor, esto puede tardar unos minutos(5-10~), mientras tanto te invito a leer este documento para que comprendas la estructura del libro.

---

## 📋 Índice

- [🚀 Inicio Rápido](#inicio-rápido)
- [📊 Análisis Disponibles](#análisis-disponibles)
- [📁 Estructura del Proyecto](#estructura-del-proyecto)
- [🔧 Configuración](#configuración)
- [❓ Ayuda](#ayuda)

---

## 🚀 Inicio Rápido

### 1. Verificar el Entorno

Abre una terminal y ejecuta:

```bash
# Verificar que todo está instalado
uv run scripts/generate_codeql.py --diagnose
```

Deberías ver ✓ en: CodeQL CLI, Node.js, npm, query packs

### 2. Ejecutar Análisis

Idealmente puedes realizar el proceso a traves de los notebook para la mejor experiencia en `/nbs`, sin embargo, también puedes ejecutar los archivos de forma individual

**Para SBOM (Software Bill of Materials):**

```bash
uv run scripts/generate_sboms.py
```

**Para CodeQL (Análisis de Seguridad):**

```bash
uv run scripts/generate_codeql.py
```

### 3. Ver Resultados

Los resultados se guardan en `data/results/`:

- SBOMs: `{repo-name}-sbom.json`
- CodeQL: `{repo-name}-codeql.json`

---

## 📊 Análisis Disponibles

### Notebooks de Análisis

| Nombre                  | Ubicación                          | Descripción                                   |
| ----------------------- | ---------------------------------- | --------------------------------------------- |
| **Generación de SBOMs** | `nbs/sbom/generacion_sbom.ipynb`   | Genera Software Bill of Materials usando Syft |
| **Análisis CodeQL**     | `nbs/vuln/generacion_codeql.ipynb` | Análisis de seguridad estático con CodeQL     |

### Scripts

| Script               | Ubicación  | Descripción                             |
| -------------------- | ---------- | --------------------------------------- |
| `generate_sboms.py`  | `scripts/` | Automatiza generación de SBOMs          |
| `generate_codeql.py` | `scripts/` | Automatiza análisis CodeQL              |
| `add_submodules.py`  | `scripts/` | Agrega repositorios como submódulos Git |

---

## 📁 Estructura del Proyecto

```
ciberseguridad_2026/
├── data/
│   ├── repos/           # Repositorios a analizar
│   ├── results/         # Resultados de análisis (JSON)
│   └── repos.json       # Configuración de repos
├── nbs/                 # Notebooks Jupyter
│   ├── sbom/            # Análisis de SBOMs
│   └── vuln/            # Análisis CCCodeQL
├── scripts/             # Automatización
│   ├── generate_sboms.py
│   ├── generate_codeql.py
│   └── add_submodules.py
├── .devcontainer/       # Configuración DevContainer
└── WELCOME.md           # Este archivo
```

---

## 🔧 Configuración

### Agregar Nuevos Repositorios

1. **Edita `data/repos.json`:**

```json
{
    "repositories": [
        {
            "url": "https://github.com/owner/repo-name.git",
            "path": "data/repos/repo-name",
            "ref": "main"
        }
    ]
}
```

2. **Ejecuta:**

```bash
uv run scripts/add_submodules.py && git submodule update --init --recursive
```

3. **Corre los análisis nuevamente**

### Herramientas Instaladas

- **Python 3.11** con `uv` para gestión de dependencias
- **Syft** para generación de SBOMs
- **CodeQL CLI 2.25.1** para análisis de seguridad
- **Node.js 20** para análisis de JavaScript
- **Git** para control de versiones

---

## ❓ Ayuda

### Problemas Comunes

**Error: "CodeQL CLI not found"**

- Verificar: `codeql version`
- Reconstruir DevContainer: `Dev Containers: Rebuild Container`

**Error: "Query pack cannot be found"**

- Ejecutar: `codeql pack download codeql/python-queries`

**Node.js no disponible (para JavaScript)**

- Reconstruir DevContainer

### Diagnóstico Rápido

```bash
# Ver qué query packs están disponibles
codeql pack ls codeql/python-queries
codeql pack ls codeql/javascript-queries

# Ver versiones instaladas
node --version
npm --version
python --version
```

---

## 📚 Documentación Adicional

- [CodeQL Documentation](https://codeql.github.com/docs/)
- [Syft Documentation](https://github.com/anchore/syft)
- [Software Bill of Materials](https://www.ntia.gov/page/software-bill-materials)

---

**Última actualización**: Abril 2026

¿Necesitas ayuda? Revisa los notebooks en `nbs/` que tienen instrucciones paso a paso.
