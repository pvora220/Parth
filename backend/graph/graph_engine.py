def build_graph(target: str, identities: list[dict]):
    nodes = [{"id": target, "type": "target"}]
    edges = []

    for identity in identities:
        site = identity["site"]
        nodes.append(
            {
                "id": site,
                "type": "account",
                "confidence": identity["confidence"],
            }
        )
        edges.append({"source": target, "target": site})

    return {"nodes": nodes, "edges": edges}
