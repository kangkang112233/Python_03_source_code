# 日本語:
# `csv.reader()`はCSVファイルを読み込むための関数です。
# イテラブルなReaderオブジェクトを返します。
# CSVファイルの内容を行ごとにリストとして扱います。

# English:
# `csv.reader()` is a function to read CSV files.
# It returns an iterable Reader object.
# It treats the contents of a CSV file as lists, line by line.

import csv


# Function to read and display the contents of a CSV file
def read_csv(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(", ".join(row))  # Print each row as a comma-separated string


# Application scenario: Library management system
# Suppose 'books.csv' contains book information with columns: Title, Author, Year

csv_file_path = "/mnt/data/sample.csv"  # Path to the CSV file
read_csv(csv_file_path)

# Example output format:
# Title, Author, Year
# 1984, George Orwell, 1949
# To Kill a Mockingbird, Harper Lee, 1960
# The Great Gatsby, F. Scott Fitzgerald, 1925
