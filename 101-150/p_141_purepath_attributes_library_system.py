# 日本語:
# PurePathの属性を使用して、パスの異なる部分にアクセスできます。
# 例えば、図書管理システムでファイルのパスからファイル名や拡張子を取得する場合に使用します。

# 英語:
# You can access different parts of a path using PurePath attributes.
# For example, in a library management system, you might use these attributes to retrieve the file name or extension from a file path.

from pathlib import PurePath

# Define a sample file path for a book in the library system
file_path = PurePath("/library_system/fiction/novel.txt")

# Access different parts of the path
parts = file_path.parts
drive = file_path.drive
root = file_path.root
anchor = file_path.anchor
parents = file_path.parents
parent = file_path.parent
name = file_path.name
suffix = file_path.suffix
suffixes = file_path.suffixes
stem = file_path.stem

# Print the results
print("Parts:", parts)
print("Drive:", drive)
print("Root:", root)
print("Anchor:", anchor)
print("Parents:", parents)
print("Parent:", parent)
print("Name:", name)
print("Suffix:", suffix)
print("Suffixes:", suffixes)
print("Stem:", stem)
