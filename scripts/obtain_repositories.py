import requests
import json
from datetime import datetime, timedelta, timezone

ORG = "openclaw"
BASE_PATH = "data/repos"
TODAY = datetime(2026, 4, 16, tzinfo=timezone.utc)
ONE_MONTH_AGO = TODAY - timedelta(days=30)


def get_active_repos():
    url = f"https://api.github.com/orgs/{ORG}/repos?per_page=100"

    headers = {"Accept": "application/vnd.github.v3+json"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error al conectar con la API: {response.status_code}")
        return []

    repos = response.json()
    active_repos = []

    for repo in repos:
        if not repo.get('pushed_at'):
            continue

        pushed_at = datetime.fromisoformat(
            repo['pushed_at'].replace("Z", "+00:00"))

        if pushed_at >= ONE_MONTH_AGO:
            active_repos.append({
                "url": repo['clone_url'],
                "path": f"{BASE_PATH}/{repo['name']}",
                "ref": repo.get('default_branch', 'main')
            })

    return active_repos


active_list = get_active_repos()
data = {"repositories": active_list}

with open("repos.json", "w") as f:
    json.dump(data, f, indent=4)

print(f"Se encontraron {len(active_list)} repositorios activos.")
print("Archivo 'repos.json' generado exitosamente.")
