def test_convert_halfwidth_to_fullwidth_katakana():
    test_cases = [
        ("ﾃｰﾌﾞﾙﾃﾞｰﾀ", "テーブルデータ"),
        ("ｶﾞｯｺｳ", "ガッコウ"),
        ("ﾌﾞﾀ", "ブタ"),
        ("ﾊﾟｰﾃｨｰ", "パーティー"),
        ("", ""),
        ("ﾊﾝｶｸｶﾀｶﾅと全角カタカナ", "ハンカクカタカナと全角カタカナ"),
        ("ｶﾞｰﾙｽﾞﾊﾞﾝﾄﾞ", "ガールズバンド"),
    ]

    for input_str, expected_output in test_cases:
        output_str = convert_halfwidth_to_fullwidth_katakana_text(input_str)
        assert (
            output_str == expected_output
        ), f"Test failed for input: {input_str}. Expected: {expected_output}, but got: {output_str}"

    print("All tests passed.")


def convert_halfwidth_to_fullwidth_katakana_text(content):
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

    # First, handle combined half-width Katakana
    for halfwidth, fullwidth in combined_katakana.items():
        content = content.replace(halfwidth, fullwidth)

    # Then, convert remaining half-width Katakana to full-width
    converted_content = content.translate(conversion_table)

    return converted_content


# Run tests
test_convert_halfwidth_to_fullwidth_katakana()
