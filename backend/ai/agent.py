from backend.ai.correlation import correlate_identities
from backend.ai.entity_extractor import extract_entities
from backend.ai.planner import InvestigationPlanner
from backend.ai.threat_scoring import threat_score
from backend.graph.graph_engine import build_graph
from backend.scanners.username_scanner import scan_username


class AIAgent:
    def __init__(self):
        self.planner = InvestigationPlanner()

    async def investigate(self, target: str):
        plan = self.planner.plan(target)

        accounts = {}
        if "username_scan" in plan:
            accounts = await scan_username(target)

        entities = extract_entities(str(accounts))
        identities = correlate_identities(target, accounts)
        graph = build_graph(target, identities)
        score = threat_score(accounts, entities)

        return {
            "target": target,
            "plan": plan,
            "accounts_found": [site for site, found in accounts.items() if found],
            "identities": identities,
            "entities": entities,
            "threat_score": score,
            "graph": graph,
        }
