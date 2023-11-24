# 🤯 Comparative Analysis of Solution Methods for System of Linear Equations.

## 📝 Overview

This project explores various methods for solving systems of linear equations using Python. Linear equations play a crucial role in modeling real-world scenarios, and different solution methods are employed based on the nature of the equations and the requirements of the problem.

This project is all about figuring out which method works best for different types of problems, **considering how many equations there are, what kind of numbers are in them, and how precise we need to be**, all with the help of Python.

## 🚗 Real-World Applications

Linear equations are fundamental in diverse fields:

- **👩‍🔬 Engineering and Physics:** Analysis and design of structures, circuits, and mechanical systems.
- **💵 Economics and Finance:** Modeling economic trends, financial decisions, and optimizing investments.
- **💻 Computer Science and Machine Learning:** Basis for algorithms, data analysis, and training machine learning models.
- **🤖 Control Systems and Robotics:** Essential for precise control of machines and automated systems.
- **📊 Statistics and Data Analysis:** Used to fit models to data, understand relationships, and solve optimization problems.

## 💪 Implemented Solution Methods

1. **Cramer's Rule:**

   - Utilizes determinants to solve the system by ratios of determinants.

2. **Gauss-Jordan Elimination:**

   - Further refines the augmented matrix to reduced row-echelon form for simplified solving.

3. **Matrix Inversion:**
   - Finds the inverse of the coefficient matrix (if it exists) to obtain the solution.

## 🔎 Comparative Analysis

The project includes a comparative analysis of the implemented methods, considering factors such as system size, coefficient complexity, and precision requirements. The user is prompted to input the size of the system, allowing for flexibility in exploring different scenarios.

## 🎮 How to use

The program generates random linear systems and provides three different methods to solve them: Cramer's Rule, Matrix Inversion, and Row Equivalent. Follow the instructions to input the size of the system and choose the solution method.

1. Run the `main.py` and input the number of unknowns when prompted.
2. The program will generate a random linear system of equations.
3. Choose a method to solve the system:
   - Enter `1` for Cramer's Rule.
   - Enter `2` for Matrix Inversion.
   - Enter `3` for Row Equivalent.
4. Depending on the method chosen, the program will display the solution.

#### Example:

```
Pick the number of unknowns: 3

The equations are:
7a + 9b + 6c  = 1
4a + 2b + 9c  = 8
2a + 3b + 3c  = 7


Choose the method to solve the linear system:
1 for Cramer's Rule
2 for Matrix Inversion
3 for Row Equivalent

Enter choice: 1

Using Cramers Rule, solutions are:
a = -26/3
b = 13/3
c = 34/9
```

## 📃 License

This project is licensed under the MIT License.
