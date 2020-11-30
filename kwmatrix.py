from itertools import product
import re


# Define test seeds and modifiers
SEEDS = [
    'dingles',
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
    combinations = []
    # 1. Replace placeholder in string with matching dict keys
    mods_product = product(*modifiers.values())
    # mods_product = zip([])
    print([i for i in mods_product])
    # 2. Append to `combinations` list

    return combinations


def matrix(seeds: list, modifiers: dict):
    """Combine several lists of modifiers with a list of seed keywords."""
    combined_kws = []
    for seed in seeds:
        seed_vars = re.findall(r'%([\w-]+)', seed)
        mods_subset = {k: modifiers[k] for k in seed_vars}
        if len(mods_subset) > 0:
            # combined_kws.extend(matrix(seed, modifiers))
            _combine(seed, modifiers)
            # combined_kws.append(seed)
        else:
            combined_kws.append(seed)

    return combined_kws


if __name__ == '__main__':
    print(matrix(SEEDS, MODIFIERS))