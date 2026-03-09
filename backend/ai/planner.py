class InvestigationPlanner:
    def plan(self, target: str):
        steps = []
        if "@" in target:
            steps.append("email_lookup")
        else:
            steps.append("username_scan")

        steps.extend([
            "entity_extraction",
            "identity_correlation",
            "graph_analysis",
            "threat_score",
        ])
        return steps
