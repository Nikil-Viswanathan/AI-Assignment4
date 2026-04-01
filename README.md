# CSP Assignment 
---
# 1. Australia Map Coloring

To run, we need matplotlib so we install it first:
pip install matplotlib

This program colors the Australian states such that no two neighboring states have the same color.
* Variables -> States (WA, NT, Q, SA, NSW, V, T)
* Domain -> {Red, Green, Blue}
* Constraint -> Neighboring states cannot have the same color



* Prints the color assigned to each state
* Displays a map-like visualization using polygons

---

# 2. Telangana Map Coloring

pip install geopandas matplotlib

This program performs map coloring on real Telangana districts using geographic data.
* Variables -> Districts
* Domain -> Colors
* Constraint -> Adjacent districts must have different colors
* Neighbors are detected using geometric intersection

To run, we need matplotlib and geopandas so we install it first:

* Automatically finds neighboring districts
* Colors the real map
* Displays labeled Telangana map

---

# 3. Sudoku Solver

Solves a 9×9 Sudoku puzzle using CSP and backtracking.
* Variables -> Empty cells
* Domain -> {1–9}
* Constraints:

  * No repetition in rows
  * No repetition in columns
  * No repetition in 3×3 grids
  * 
* Displays the original Sudoku
* Prints the solved Sudoku in a clean grid format

---

# 4. Cryptarithmetic Puzzle (TWO + TWO = FOUR)

Solves the cryptarithmetic puzzle where each letter represents a unique digit.

* Variables -> Letters (T, W, O, F, U, R) + carry variables
* Domain -> Digits (0–9), carries {0,1}
* Constraints:

  * All letters must have different digits
  * Column-wise addition must be correct
  * No leading zeros

* Displays the digit assigned to each letter
* Shows the final arithmetic verification

