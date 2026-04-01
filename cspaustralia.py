import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Variables
states = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

# Domains
colors = ['Red', 'Green', 'Blue']

# Neighbours for constraints 
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# To check if assigning a color to the neighbour is valid
def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(states):
        return assignment

    unassigned = [s for s in states if s not in assignment]
    current = unassigned[0]

    for color in colors:
        if is_valid(current, color, assignment):
            assignment[current] = color

            result = backtrack(assignment)
            if result:
                return result

            del assignment[current]  #Invalid

    return None

solution = backtrack({})

print("CSP Solution:", solution)


color_map = {
    'Red': 'red',
    'Green': 'green',
    'Blue': 'blue'
}

states_shapes = {
    'WA': [(0,2), (1,1), (2,1), (2.5,2), (2.5,5), (1.5,6), (0.5,5)],
    'NT': [(2.5,4), (4.5,4), (4.5,6), (2.5,6)],
    'SA': [(2.5,2), (4.5,2), (4.5,4), (2.5,4)],
    'Q': [(4.5,3), (7,3.5), (7.5,5), (6.5,6), (4.5,6)],
    'NSW': [(4.5,2), (7,2), (7,3.5), (4.5,3)],
    'V': [(4.5,1), (6.5,1), (6,2), (4.5,2)],
    'T': [(5.5,-1), (6,-0.8), (6.2,-0.4), (5.8,0.1), (5.3,-0.3)]
}

plt.figure()

for state, shape in states_shapes.items():
    polygon = Polygon(
        shape,
        closed=True,
        facecolor=color_map[solution[state]],
        edgecolor='black'
    )
    plt.gca().add_patch(polygon)

    x = sum(p[0] for p in shape) / len(shape)
    y = sum(p[1] for p in shape) / len(shape)
    plt.text(x, y, state, ha='center', va='center', color='white')

plt.title("Australia Map Coloring")
plt.xlim(-1, 9)
plt.ylim(-2, 7)
plt.axis('off')

plt.show()