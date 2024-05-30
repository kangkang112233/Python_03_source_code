def convert_halfwidth_to_fullwidth_katakana(file_path, output_path):
    # Define the conversion tables for half-width Katakana and combined characters
    halfwidth_katakana = "ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ"
    fullwidth_katakana = "ヲァィゥェォャュョッーアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワン"
    conversion_table = str.maketrans(halfwidth_katakana, fullwidth_katakana)

    combined_katakana = {
        "ｶﾞ": "ガ",
        "ｷﾞ": "ギ",
        "ｸﾞ": "グ",
        "ｹﾞ": "ゲ",
        "ｺﾞ": "ゴ",
        "ｻﾞ": "ザ",
        "ｼﾞ": "ジ",
        "ｽﾞ": "ズ",
        "ｾﾞ": "ゼ",
        "ｿﾞ": "ゾ",
        "ﾀﾞ": "ダ",
        "ﾁﾞ": "ヂ",
        "ﾂﾞ": "ヅ",
        "ﾃﾞ": "デ",
        "ﾄﾞ": "ド",
        "ﾊﾞ": "バ",
        "ﾋﾞ": "ビ",
        "ﾌﾞ": "ブ",
        "ﾍﾞ": "ベ",
        "ﾎﾞ": "ボ",
        "ﾊﾟ": "パ",
        "ﾋﾟ": "ピ",
        "ﾌﾟ": "プ",
        "ﾍﾟ": "ペ",
        "ﾎﾟ": "ポ",
    }

    # Read the content of the file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # First, handle combined half-width Katakana
    for halfwidth, fullwidth in combined_katakana.items():
        content = content.replace(halfwidth, fullwidth)

    # Then, convert remaining half-width Katakana to full-width
    converted_content = content.translate(conversion_table)

    # Write the converted content to the output file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(converted_content)

    print("-----------okokok!!!!+++++")


# Example usage
input_file_path = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-00-20-1516_archive\\2024-01-29-0011_desktop\\tansTest\\test01.txt"  # Replace with your input file path
output_file_path = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-00-20-1516_archive\\2024-01-29-0011_desktop\\tansTest\\test02.txt"  # Replace with your desired output file path

convert_halfwidth_to_fullwidth_katakana(input_file_path, output_file_path)
