import pandas as pd


def convert_fullwidth_to_halfwidth_katakana(content):
    fullwidth_katakana = "ヲァィゥェォャュョッーアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワン゛゜"
    halfwidth_katakana = "ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝﾞﾟ"
    conversion_table = str.maketrans(fullwidth_katakana, halfwidth_katakana)

    combined_katakana = {
        "ガ": "ｶﾞ",
        "ギ": "ｷﾞ",
        "グ": "ｸﾞ",
        "ゲ": "ｹﾞ",
        "ゴ": "ｺﾞ",
        "ザ": "ｻﾞ",
        "ジ": "ｼﾞ",
        "ズ": "ｽﾞ",
        "ゼ": "ｾﾞ",
        "ゾ": "ｿﾞ",
        "ダ": "ﾀﾞ",
        "ヂ": "ﾁﾞ",
        "ヅ": "ﾂﾞ",
        "デ": "ﾃﾞ",
        "ド": "ﾄﾞ",
        "バ": "ﾊﾞ",
        "ビ": "ﾋﾞ",
        "ブ": "ﾌﾞ",
        "ベ": "ﾍﾞ",
        "ボ": "ﾎﾞ",
        "パ": "ﾊﾟ",
        "ピ": "ﾋﾟ",
        "プ": "ﾌﾟ",
        "ペ": "ﾍﾟ",
        "ポ": "ﾎﾟ",
    }

    for fullwidth, halfwidth in combined_katakana.items():
        content = content.replace(fullwidth, halfwidth)

    converted_content = content.translate(conversion_table)

    return converted_content


def convert_excel_file(input_file_path, output_file_path):
    # Read the Excel file
    df = pd.read_excel(input_file_path)

    # Apply the conversion to each cell in the DataFrame
    for col in df.columns:
        df[col] = df[col].astype(str).apply(convert_fullwidth_to_halfwidth_katakana)

    # Write the converted DataFrame to a new Excel file
    df.to_excel(output_file_path, index=False)
    print(f"Converted Excel file has been saved to {output_file_path}")


# Example usage
input_excel_file = "/mnt/data/input.xlsx"  # Replace with your input Excel file path
output_excel_file = (
    "/mnt/data/output.xlsx"  # Replace with your desired output Excel file path
)

convert_excel_file(input_excel_file, output_excel_file)
