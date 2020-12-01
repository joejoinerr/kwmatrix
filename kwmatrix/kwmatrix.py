from functools import reduce
from itertools import product
import re


def _subset_modifiers(seed: str, modifiers: dict, var_char: str) -> dict:
    lookup = var_char + r'([\w-]+)'
    seed_vars = re.findall(lookup, seed)

    # Create a new subset dictionary where each modifier list is de-duplicated
    mods_subset = {k: list(set(modifiers.get(k, []))) for k in seed_vars}

    return mods_subset


def _combine(seed: str, modifiers: dict, var_char: str):
    mods_product = [dict(zip(modifiers.keys(), p)) for p in product(*modifiers.values())]
    for vars_list in mods_product:
        # Use `reduce` to loop over the keyword several times and replace all variables
        new_kw = reduce(lambda kw, var: kw.replace(var_char + var, vars_list[var].strip()), vars_list, seed)
        vars_list['keyword'] = new_kw.strip()

        yield vars_list


def matrix(seeds: list, modifiers: dict, var_char=r'%'):
    """Combine named modifier lists with a list of seed keywords containing variables."""
    for seed in seeds:
        # Subset modifiers so that we don't pass modifiers that aren't contained in the keyword
        mods_subset = _subset_modifiers(seed, modifiers, var_char)

        # Only run _combine function if there are variables to replace
        if len(mods_subset) > 0:
            for new_kw in _combine(seed, mods_subset, var_char):
                yield new_kw
        else:
            # Yield a dictionary to maintain consistency with combined keywords
            yield {'keyword': seed}
