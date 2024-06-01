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

    # First, handle combined full-width Katakana
    for fullwidth, halfwidth in combined_katakana.items():
        content = content.replace(fullwidth, halfwidth)

    # Then, convert remaining full-width Katakana to half-width
    converted_content = content.translate(conversion_table)

    return converted_content


def test_convert_fullwidth_to_halfwidth_katakana():
    test_cases = [
        ("テーブルデータ", "ﾃｰﾌﾞﾙﾃﾞｰﾀ"),
        ("ガッコウ", "ｶﾞｯｺｳ"),
        ("ブタ", "ﾌﾞﾀ"),
        ("パーティー", "ﾊﾟｰﾃｨｰ"),
        ("", ""),
        ("ハンカクカタカナと全角カタカナ", "ﾊﾝｶｸｶﾀｶﾅと全角ｶﾀｶﾅ"),
        ("ガールズバンド", "ｶﾞｰﾙｽﾞﾊﾞﾝﾄﾞ"),
    ]

    for input_str, expected_output in test_cases:
        output_str = convert_fullwidth_to_halfwidth_katakana(input_str)
        assert (
            output_str == expected_output
        ), f"Test failed for input: {input_str}. Expected: {expected_output}, but got: {output_str}"

    print("All tests passed.")


# Run tests
test_convert_fullwidth_to_halfwidth_katakana()
