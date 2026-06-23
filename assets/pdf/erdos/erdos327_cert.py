"""Focused Phi-bound at one moderate config. Streams progress live."""
import sys, pulp, time
from fractions import Fraction

def smooth_up_to(P, X):
    out = {1}
    Plist = sorted(P)
    def gen(n, idx):
        for i in range(idx, len(Plist)):
            m = n * Plist[i]
            if m <= X:
                out.add(m); gen(m, i)
    gen(1, 0)
    return sorted(out)

def edges_for_k(S, k):
    E = []
    for i, c in enumerate(S):
        for d in S[i+1:]:
            if (k*c*d) % (c+d) == 0:
                E.append((c, d))
    return E

def phi_bound(P, X, k, time_limit_ilp=20):
    t0 = time.time()
    S = smooth_up_to(P, X)
    E = edges_for_k(S, k)
    nbr = {c: set() for c in S}
    for a, b in E:
        nbr[a].add(b); nbr[b].add(a)
    rho = 1.0
    for p in P: rho *= (p-1)/p
    H = sum(1/c for c in S)
    s = len(S)
    print(f"[{time.time()-t0:.0f}s] |V|={s}, |E|={len(E)}, rho={rho:.5f}, H={H:.4f}", flush=True)

    betas = []
    cur_IS = set(); cur_b = 0
    solves = 0
    for j in range(1, s+1):
        v = S[j-1]
        if not (nbr[v] & cur_IS):
            cur_IS.add(v); cur_b = len(cur_IS)
        else:
            prefix = set(S[:j])
            prob = pulp.LpProblem("mis", pulp.LpMaximize)
            x = {u: pulp.LpVariable(f"y{u}", cat="Binary") for u in prefix}
            prob += pulp.lpSum(x[u] for u in prefix)
            for a, b in E:
                if a in prefix and b in prefix:
                    prob += x[a] + x[b] <= 1
            prob.solve(pulp.PULP_CBC_CMD(msg=0, timeLimit=time_limit_ilp))
            cur_b = sum(1 for u in prefix if x[u].value() and x[u].value() > 0.5)
            cur_IS = {u for u in prefix if x[u].value() and x[u].value() > 0.5}
            solves += 1
        betas.append(cur_b)
        if j % 50 == 0 or j == s:
            print(f"[{time.time()-t0:.0f}s] j={j}/{s}, c_j={v}, beta_j={cur_b}, solves={solves}", flush=True)

    Phi = betas[-1]/S[-1]
    for j in range(1, s):
        Phi += betas[j-1] * (1/S[j-1] - 1/S[j])
    bound = 1 - rho * (H - Phi)
    print(f"[{time.time()-t0:.0f}s] beta_s={betas[-1]}, Phi={Phi:.6f}, bound={bound:.5f}", flush=True)
    return bound

if __name__ == "__main__":
    # Take config from argv if provided, else default.
    P = {2, 3, 5, 7, 11, 13}
    X = 2000
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if len(sys.argv) > 2:
        X = int(sys.argv[2])
    if len(sys.argv) > 3:
        P = set(int(p) for p in sys.argv[3].split(","))
    print(f"=== P={sorted(P)}, X={X}, k={k} ===", flush=True)
    phi_bound(P, X, k)
