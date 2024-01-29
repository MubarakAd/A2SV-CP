class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        out = Counter()
        for i in cpdomains:
            freq,dom = i.split()
            dm = dom.split(".")
            for i in range(len(dm)):
                out[".".join(dm[i:])]+=int(freq)
        out2 = []
        for dom,freq in out.items():
            out2.append(f"{freq} {dom}")
        return out2