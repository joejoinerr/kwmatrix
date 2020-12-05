# 🔠 kwmatrix: Combine keywords with several modifiers for SEO

Keyword 'matrixing' is the process of taking one or more seed keywords and combining it with every combination of modifier keywords. 

For example, the following seed keywords contain replacement variables:

* %color shoes
* %color %type shoes

Given the following modifiers:

* __color__: red, blue
* __type__: walking, leather

These would be combined with the seed keywords to give the following result:

* red shoes
* blue shoes
* red walking shoes
* blue walking shoes
* red leather shoes
* blue leather shoes

This process makes it very quick and easy to create large lists of potential keywords for SEO. The kwmatrix package for Python makes this process very straightforward.

## Installation

kwmatrix can be installed using the pip package manager:

    pip install kwmatrix

Alternatively, using pipenv:

    pipenv install kwmatrix

It can then be imported in the usual way:

    import kwmatrix

## Usage

kwmatrix has a single function: `matrix()`. This has 2 required arguments and a third optional argument:

<dl>
    <dt><strong>seeds</strong>: list</dt>
    <dd>A list of seed keywords with variables to replace. Each variable name is preceded by a `%` character e.g. "%color %type shoes".</dd>
    <dt><strong>modifiers</strong>: dict</dt>
    <dd>A dictionary of modifier keywords to replace the variables in the seed keywords. Each key should match the name of a %variable, and the value should be a list of values insert in its place.</dd>
    <dt><strong>var_char</strong>: str (optional)</dt>
    <dd>A single character to use for variables instead of the default `%`. Provide this argument if the default choice is causing issues with your keyword set.</dd>
</dl>

The `matrix()` function will return a generator. When iterated upon, it will produce a dictionary for each result containing the final keyword and the %variables used, e.g.:

    {'color': 'red', 'type': 'walking', 'keyword': 'blue walking shoes'}

### Example

    from kwmatrix import matrix

    SEEDS = [
        '%color shoes',
        '%color %type shoes'
    ]
    MODIFIERS = {
        'color': ['red', 'blue'],
        'type': ['walking', 'leather']
    }

    results = matrix(SEEDS, MODIFIERS)

