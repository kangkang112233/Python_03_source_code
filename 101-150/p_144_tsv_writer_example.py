# 日本語:
# `csv.writerow()`はデータを書式化し、writerのファイルオブジェクトに書き込むメソッドです。
# 行ごとにデータをファイルに書き込む。
#
# `csv.writerows()`は複数行を書き込むために、上記のwriterow()メソッド同様に
# rowオブジェクトのイテラブルのすべての要素を指定するメソッドです。
# 複数のデータ行を一度にファイルに書き込む。

# English:
# `csv.writerow()` is a method to format data and write it to a writer file object.
# Write data to a file row by row.
#
# `csv.writerows()` is a method similar to writerow() for writing multiple rows.
# Write multiple rows of data to a file at once.

import csv


# Function to write data to a TSV file
def write_tsv(file_path, data):
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        tsv_writer = csv.writer(
            file, delimiter="\t", quotechar="#", quoting=csv.QUOTE_MINIMAL
        )

        # Writing header
        header = ["Title", "Author", "Year"]
        tsv_writer.writerow(header)  # Write a single row

        # Writing multiple rows
        tsv_writer.writerows(data)  # Write multiple rows


# Application scenario: Library management system
# Data to be written to 'books.tsv'
books_data = [
    ["1984", "George Orwell", "1949"],
    ["To Kill a Mockingbird", "Harper Lee", "1960"],
    ["The Great Gatsby", "F. Scott Fitzgerald", "1925"],
]

tsv_file_path = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-05-16-2335_Python 3 Certified Practical Engineer\\新建 Microsoft Excel 工作表.csv"  # Path to the TSV file
write_tsv(tsv_file_path, books_data)

# Example output file content:
# Title   Author  Year
# 1984    George Orwell  1949
# To Kill a Mockingbird  Harper Lee  1960
# The Great Gatsby  F. Scott Fitzgerald  1925
