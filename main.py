import sys

def parse_set(s):
    s = s.strip()
    if s == '0' or not s:
        return set()
    if s.startswith('{') and s.endswith('}'):
        s = s[1:-1].strip()
    if not s:
        return set()
    return {int(x) for x in s.split()}

def read_case(lines, idx):
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines):
        return None, idx

    n = int(lines[idx].strip())
    idx += 1
    
    start = parse_set(lines[idx].strip())
    idx += 1
    
    alphabet = lines[idx].strip().split()
    idx += 1
    
    final = parse_set(lines[idx].strip())
    idx += 1
    
    transitions = {}
    for i in range(1, n + 1):
        line = lines[idx].strip()
        idx += 1
        
        parts = line.split(maxsplit=1)
        state_num = int(parts[0])
        rest = parts[1] if len(parts) > 1 else ""
        
        tokens = []
        curr = []
        in_brace = False
        for char in rest:
            if char == '{':
                in_brace = True
                curr.append(char)
            elif char == '}':
                in_brace = False
                curr.append(char)
            elif char == ' ' and not in_brace:
                if curr:
                    tokens.append("".join(curr))
                    curr = []
            else:
                curr.append(char)
        if curr:
            tokens.append("".join(curr))
            
        transitions[state_num] = {}
        for sym, tok in zip(alphabet, tokens):
            transitions[state_num][sym] = parse_set(tok)
            
    nfa = {
        'alphabet': alphabet,
        'start': start,
        'final': final,
        'transitions': transitions
    }
    return nfa, idx

def subset_construction(nfa):
    alphabet = nfa['alphabet']
    start_set = frozenset(nfa['start'])
    
    dfa_states = [start_set]
    queue = [start_set]
    dfa_trans = {}
    
    while queue:
        curr = queue.pop(0)
        dfa_trans[curr] = {}
        
        for sym in alphabet:
            nxt = set()
            for state in curr:
                nxt.update(nfa['transitions'].get(state, {}).get(sym, set()))
            
            nxt_frozen = frozenset(nxt)
            dfa_trans[curr][sym] = nxt_frozen
            
            if nxt_frozen not in dfa_states:
                dfa_states.append(nxt_frozen)
                queue.append(nxt_frozen)
                
    dfa_final = [s for s in dfa_states if any(q in nfa['final'] for q in s)]
    
    return {
        'alphabet': alphabet,
        'states': dfa_states,
        'start': start_set,
        'final': dfa_final,
        'transitions': dfa_trans
    }

def print_dfa(dfa):
    #mapeo de subconjuntos a id
    state_map = {s: i + 1 for i, s in enumerate(dfa['states'])}
    
    start_id = state_map[dfa['start']]
    final_ids = [state_map[s] for s in dfa['final']]
    
    print(f"Initial state: {start_id}")
    if final_ids:
        print("Final states:", " ".join(str(x) for x in sorted(final_ids)))
    else:
        print("Final states: 0")
        
    header = "State\t" + "\t".join(dfa['alphabet'])
    print(header)
    
    for s in dfa['states']:
        sid = state_map[s]
        row = [str(sid)]
        for sym in dfa['alphabet']:
            dest = dfa['transitions'][s][sym]
            row.append(str(state_map[dest]))
        print("\t".join(row))

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    num_cases = int(lines[0].strip())
    idx = 1
    
    for _ in range(num_cases):
        nfa, idx = read_case(lines, idx)
        if nfa is None:
            break
        dfa = subset_construction(nfa)
        print_dfa(dfa)

if __name__ == "__main__":
    main()