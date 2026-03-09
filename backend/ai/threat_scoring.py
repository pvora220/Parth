import random


def threat_score(accounts: dict, entities: dict):
    score = 0
    score += len([a for a in accounts.values() if a]) * 10
    score += len(entities.get("emails", [])) * 20
    score += random.randint(0, 10)
    return min(score, 100)
