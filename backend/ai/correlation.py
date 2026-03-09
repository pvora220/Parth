from difflib import SequenceMatcher


def similarity(a: str, b: str):
    return SequenceMatcher(None, a, b).ratio()


def correlate_identities(username: str, accounts: dict):
    matches = []
    for site, found in accounts.items():
        if found:
            matches.append({"site": site, "confidence": round(similarity(username, site), 2)})
    return matches
