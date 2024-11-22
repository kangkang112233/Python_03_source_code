def align_abap_comments(input_file, output_file):
    def find_max_code_length(lines):
        """Find the length of the longest line excluding comments."""
        max_length = 0
        for line in lines:
            if '"' in line:
                code_part = line.split('"')[
                    0
                ].rstrip()  # Extract the code part and strip trailing whitespace
                max_length = max(max_length, len(code_part))
        return max_length

    def align_comments(lines, max_length):
        """Align comments in the lines based on the maximum code length."""
        aligned_lines = []
        for line in lines:
            if '"' in line:
                code_part, comment_part = line.split('"', 1)
                code_part = code_part.rstrip()
                aligned_line = (
                    f'{code_part.ljust(max_length + 4)}"{comment_part.lstrip()}'
                )
                aligned_lines.append(aligned_line)
            else:
                aligned_lines.append(line.rstrip())  # Add lines without comments as is
        return aligned_lines

    form_flag = 0  # Initial flag value
    output_lines = []  # List to store output lines
    temp_lines = []  # Temporary list to store lines for processing

    # Read ABAP code from the input file
    with open(input_file, "r", encoding="utf-8") as file:
        abap_code_lines = file.readlines()

    # Process each line
    for line in abap_code_lines:
        stripped_line = line.strip()
        if stripped_line.lower().startswith("form"):
            if form_flag == 0:
                # Process lines before the form block
                if temp_lines:
                    max_length = find_max_code_length(temp_lines)
                    output_lines.extend(align_comments(temp_lines, max_length))
                    temp_lines = []
            form_flag = 1  # Entering a form block

        if form_flag == 1:
            temp_lines.append(line)  # Add line to temporary list
            if stripped_line.lower().startswith("endform"):
                form_flag = 0  # Exiting the form block
                if temp_lines:
                    max_length = find_max_code_length(temp_lines)
                    output_lines.extend(align_comments(temp_lines, max_length))
                    temp_lines = []
        else:
            temp_lines.append(line)  # Add line to temporary list if not in a form block

    # Process the last part if any
    if temp_lines:
        max_length = find_max_code_length(temp_lines)
        output_lines.extend(align_comments(temp_lines, max_length))

    # Write the aligned code to the output file without adding extra newlines
    with open(output_file, "w", encoding="utf-8") as file:
        for line in output_lines:
            if not line.endswith("\n"):
                line += "\n"
            file.write(line)


# Specify input and output files
input_file = (
    "D:\\2024-01-29-0008_sort_by_creation_date\\240628-175630_comment_test\\01.txt"
)
output_file = (
    "D:\\2024-01-29-0008_sort_by_creation_date\\240628-175630_comment_test\\02.txt"
)

# Call the function to align comments
align_abap_comments(input_file, output_file)
