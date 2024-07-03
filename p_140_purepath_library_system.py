# 日本語:
# PurePathは複数のパスを連結するために使用されます。
# 例えば、図書管理システムで複数のパスを連結してファイルの保存先を決定する場合に使用します。

# 英語:
# PurePath is used to concatenate multiple paths.
# For example, in a library management system, you can use PurePath to concatenate multiple paths to determine the file storage location.

from pathlib import Path, PurePath

# Define base directory path for the library system
base_dir = Path("/library_system")

# Define subdirectories for different sections
fiction_dir = "fiction"
non_fiction_dir = "non_fiction"
science_dir = "science"

# Create full paths using PurePath
fiction_path = PurePath(base_dir, fiction_dir)
non_fiction_path = PurePath(base_dir, non_fiction_dir)
science_path = PurePath(base_dir, science_dir)

# Print the concatenated paths
print("Fiction section path:", fiction_path)
print("Non-fiction section path:", non_fiction_path)
print("Science section path:", science_path)
