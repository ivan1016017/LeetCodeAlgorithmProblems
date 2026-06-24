def compute_leaf_scores(domain_scores: dict[str, int]) -> dict[str, int]:
    """
    Given a dict of {domain: score}, return a dict of {leaf_domain: total_score}.

    A domain is a "leaf" if no other domain in the input is a direct or indirect
    subdomain of it.  A leaf's total score is the sum of its own score plus the
    scores of every ancestor that also appears in the input.
    """

    # ── 1. Identify leaves ───────────────────────────────────────────────────
    # Domain A is an ancestor of domain B if B ends with ".<A>".
    # A domain is a leaf if no other domain has it as an ancestor.
    def is_ancestor(ancestor: str, domain: str) -> bool:
        return domain.endswith('.' + ancestor)
    
    all_domains = set(domain_scores)

    leaves = {
        d for d in all_domains
        if not any(is_ancestor(d, other) for other in all_domains)
    }

    def ancestors_in_input(domain: str) -> list[str]: 
        parts = domain.split('.')
        return [
            '.'.join(parts[i:])
            for i in range(1, len(parts))
            if '.'.join(parts[i:]) in all_domains
        ]

    result = {}
    for leaf in sorted(leaves):
        total = domain_scores[leaf] + sum(
            domain_scores[anc] for anc in ancestors_in_input(leaf)
        )
        result[leaf] = total

    return result

# ── Example from the problem statement ───────────────────────────────────────
if __name__ == "__main__":
    input_domains = {
        "test.mydomain.com":      10,
        "mail.test.mydomain.com": 15,
        "test.com":              -10,
        "com":                    20,
        "mydomain.com":            5,
        "www.mydomain.com":       10,
        "mail.test.com":          10,
        "www.test.com":           -5,
    }

    scores = compute_leaf_scores(input_domains)

    print(f"{'Domain':<30} {'Total Score':>12}  Breakdown")
    print("-" * 60)
    for domain, total in scores.items():
        parts = domain.split(".")
        breakdown = " + ".join(
            str(input_domains[".".join(parts[i:])]) 
            for i in range(len(parts))
            if ".".join(parts[i:]) in input_domains
        )
        print(f"{domain:<30} {total:>12}  ({breakdown})")