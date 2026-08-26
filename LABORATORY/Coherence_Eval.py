s1 = set("the cat sits".split())
s2 = set("the cat sleeps".split())

# Jaccard overlap calculates baseline sentence-to-sentence continuity coherence
intersection_count = len(s1.intersection(s2))
union_count = len(s1.union(s2))

overlap = intersection_count / union_count
print(f"Jaccard Word-Overlap Coherence Score: {overlap:.2f}")