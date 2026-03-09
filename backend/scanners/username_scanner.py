import asyncio
import json
from pathlib import Path
from urllib import error, request

SITES_PATH = Path(__file__).resolve().parent.parent / "datasets" / "sites.json"
with SITES_PATH.open("r", encoding="utf-8") as f:
    SITES = json.load(f)


def _sync_check(url: str):
    req = request.Request(url, method="GET")
    try:
        with request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except (error.URLError, TimeoutError, ValueError):
        return False


async def check_site(site: str, url: str, username: str):
    target = url.format(username)
    ok = await asyncio.to_thread(_sync_check, target)
    return site, ok


async def scan_username(username: str):
    tasks = [check_site(site, url, username) for site, url in SITES.items()]
    data = await asyncio.gather(*tasks)
    return dict(data)
