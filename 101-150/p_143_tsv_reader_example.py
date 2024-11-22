# 日本語:
# `csv.reader()`はCSVファイルを読み込むための関数です。
# デリミタと引用符をカスタマイズできます。
# TSVファイルや特殊な引用符を含むファイルを読み込む。

# English:
# `csv.reader()` is a function to read CSV files.
# It allows customization of delimiter and quote character.
# Read TSV files or files with special quote characters.

import csv


# Function to read and display the contents of a TSV file with custom quote character
def read_tsv(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter="\t", quotechar="#")
        for row in csv_reader:
            print("\t".join(row))  # Print each row as a tab-separated string


# Application scenario: Library management system
# Suppose 'books.tsv' contains book information with columns: Title, Author, Year

tsv_file_path = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-05-16-2335_Python 3 Certified Practical Engineer\\新建 Microsoft Excel 工作表.tsv"  # Path to the TSV file
read_tsv(tsv_file_path)

# Example output format:
# Title  Author  Year
# 1984   George Orwell  1949
# To Kill a Mockingbird  Harper Lee  1960
# The Great Gatsby  F. Scott Fitzgerald  1925
