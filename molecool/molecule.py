import numpy as np


def calculate_distance(rA, rB):

    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)

    return distance


def build_bond_list(coordinates,
                    max_bond: float | np.ndarray[float] = 1.5,  # Make the type checkers happy
                    min_bond: float | np.ndarray[float] = 0):
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if min_bond < distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds
