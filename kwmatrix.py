from functools import reduce
from itertools import product
import re


# Define test seeds and modifiers
SEEDS = [
    'nothing to replace',
    '%color shoes',
    '%type shoes',
    '%audience %color shoes',
    '%audience %type shoes',
    '%audience %color %type shoes'
]
MODIFIERS = {
    'color': [
        'red',
        'blue',
        'green',
        'grey'
    ],
    'type': [
        'walking',
        'running',
        'comfy'
    ],
    'audience': [
        'womens',
        'mens',
        'kids'
    ]
}


def _combine(seed: str, modifiers: dict) -> list:
    """Generate combinations for a single keyword."""
    mods_product = [dict(zip(modifiers.keys(), p)) for p in product(*modifiers.values())]
    combined = []
    for combination in mods_product:
        new_kw = reduce(lambda kw, var: kw.replace(f'%{var}', combination[var]), combination, seed)
        combined.append(new_kw)

    return combined


def matrix(seeds: list, modifiers: dict):
    """Combine several lists of modifiers with a list of seed keywords."""
    combined_kws = []
    for seed in seeds:
        seed_vars = re.findall(r'%([\w-]+)', seed)
        mods_subset = {k: modifiers[k] for k in seed_vars}
        if len(mods_subset) > 0:
            combined_kws.extend(_combine(seed, mods_subset))
        else:
            combined_kws.append(seed)

    return combined_kws


if __name__ == '__main__':
    print(matrix(SEEDS, MODIFIERS))
    # matrix(SEEDS, MODIFIERS)
