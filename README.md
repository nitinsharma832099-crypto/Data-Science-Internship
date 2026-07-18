# Data Science Internship

## Day 1
- Installed Python
- Installed VS Code
- Installed Jupyter Notebook
- Created GitHub Repository
- Ran my first Python program

Thank you Codomax Digital Solution for this internship opportunity.

## Day 2
# Day 2 - Python Basics

## Objective
Learn the fundamentals of Python programming.

## Topics Covered
- Variables
- Data Types
- Operators
- Conditional Statements (if-else)
- Loops (for, while)
- Functions

## Tasks Completed
- Learned Python variables and different data types.
- Practiced arithmetic, comparison, and logical operators.
- Implemented conditional statements using if-else.
- Created loop-based programs using for and while loops.
- Wrote and called user-defined functions.
- Solved basic star pattern programs.

## Programs Created
- Variable and Data Type Examples
- Operator Examples
- If-Else Programs
- For Loop Examples
- While Loop Examples
- Function Examples
- Star Pattern Programs

## Outcome
Developed a strong foundation in Python programming by understanding basic concepts and implementing simple programs.

# Day 3 – NumPy

## Objective
Learn the fundamentals of NumPy, including array creation, mathematical operations, and array calculations.

## Topics Covered
- Introduction to NumPy
- Creating NumPy Arrays
- Array Indexing and Slicing
- Mathematical Operations
- Array Statistics (Sum, Mean, Max, Min)
- Reshaping Arrays

## Tasks Completed
- Installed and imported the NumPy library.
- Created one-dimensional and two-dimensional arrays.
- Performed arithmetic operations on arrays.
- Calculated sum, mean, maximum, and minimum values.
- Practiced array reshaping and indexing.

## Programs Created
- Creating Arrays
- Mathematical Operations
- Array Statistics
- Reshaping Arrays

## Outcome
Understood NumPy fundamentals and learned how to perform efficient numerical computations using arrays.
## Day4
What I Did

Imported the Pandas library to enable data manipulation and analysis.

python   import pandas as pd

Loaded the dataset into a DataFrame using read_csv().

python   df = pd.read_csv("amazon.csv")

Viewed the rows of the dataset using head() and tail() to inspect the first and last few records.
Viewed the columns and shape of the dataset to understand its structure. The dataset contains 16 columns:
product_id, product_name, category, discounted_price, actual_price, discount_percentage, rating, rating_count, about_product, user_id, user_name, review_id, review_title, review_content, img_link, product_link.
Checked dataset information using df.info() and df.describe() to understand data types, non-null counts, and summary statistics.
Checked for missing values using df.isnull().sum().

Key Observations

The dataset is largely clean, with missing values found only in the rating_count column (2 missing entries).
Columns such as discounted_price, actual_price, discount_percentage, and rating_count are stored as object (text) type instead of numeric, due to currency symbols (₹), percentage signs (%), and comma separators in large numbers.
These formatting issues will need to be addressed in Day 5 – Data Cleaning.

Expected Outcome
✅ Dataset successfully loaded and explored using Pandas.

## Day 5
Cleaned the Amazon Sales dataset: identified 2 missing values in rating_count and filled them with the median. Checked for duplicate records based on product_id and found none. Corrected data types for discounted_price, actual_price, discount_percentage, rating, and rating_count — converting them from text to numeric by removing currency symbols (₹), percentage signs (%), and commas. Final dataset is fully clean with zero missing values and correct data types, ready for analysis.
