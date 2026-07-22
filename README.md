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

## Day 6
Task: Filter rows, select columns and sort the dataset using Pandas.
What I Did: Selected specific columns from the dataset, filtered rows based on conditions (e.g., rating above 4.5, discount above 50%), combined multiple filter conditions using &, and sorted the dataset using sort_values() to identify top-rated and highly discounted products.

## Day 7 – Basic Business Insights
Task: Calculate total, average, minimum, maximum and count values from the dataset.
What I Did: Used Pandas aggregate functions (sum, mean, min, max, count) on key numeric columns of the dataset, and used describe() to generate an overall statistical summary.
Expected Outcome: Basic business insights generated successfully.
## Day 8 – Data Visualization

Task: Create bar charts, line charts and pie charts using Matplotlib.

What I Did: Created a bar chart comparing product counts across top categories, a line chart showing average rating by category, a pie chart showing category share among the top 5 categories, and a bar chart comparing ratings across the top 10 highest-rated products.
## Day 9 – Mini Dashboard
Task: Combine charts and analysis into a single Jupyter Notebook dashboard.

What I Did: Combined the bar chart, line chart, pie chart, and an additional bar chart into a single 2x2 grid using Matplotlib's subplots(). Added a written analysis summarizing key takeaways from the visualizations, bringing together insights and charts from previous days into one consolidated dashboard.
## Day 10 – Export Data

Task: Export the cleaned dataset to a new CSV file.
## Day 11 – Business Insights

Task: Write at least five observations from the dataset based on your analysis.

What I Did: Analyzed the cleaned dataset to generate business insights, including highest/lowest buying categories, discount percentage range, rating range, average rating, average discount, and the correlation between discount percentage and rating (found to be very weak, -0.16), showing that discount level does not reliably predict a product's rating.

What I Did: Used df.to_csv() to export the cleaned Amazon Sales dataset to a new CSV file (cleaned_amazon_sales.csv), with index=False to avoid adding an extra unnecessary index column. Verified the export by reloading the file and checking its structure.
## Conclusion
I successfully completed all 12 days of this internship task, gaining hands-on experience 
in the complete data analysis workflow — from loading and cleaning raw data to generating 
visualizations and business insights using Python, Pandas, and Matplotlib.
