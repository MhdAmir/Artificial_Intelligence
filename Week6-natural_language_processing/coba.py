from svgling.core import draw_tree

# Define the tree structure
tree = ('S', [
    ('NP', [
        ('John', [])
    ]),
    ('VP', [
        ('saw', []),
        ('NP', [
            ('the', []),
            ('dog', [])
        ])
    ])
])

# Draw the tree
draw_tree(tree)
