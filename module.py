def ilk_mesaj():
    print("Muhammed Ali Ulker, 211213007")
    print("donem projesi falan gittikce zor sanirsam yazilimla yeni tanisiyorum, rabbim bana irade versin")


def is_letter(char):
    if char.isalpha():
        return True
    else:
        return False


def kucuk_harf(char):
    return char.lower()


def harf_tekrari(text):
    toplam_char = len(text)
    freq_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    for char, count in freq_dict.items():
        freq_dict[char] = (count / toplam_char) * 100
    return freq_dict


def analyze_text(text):
    print("Metindeki harf sıklıkları:")
    freq_dict = harf_tekrari(text)
    for char, freq in freq_dict.items():
        print(f"{char}: %{freq:.2f}")


def transform_text(text):
    transformed_text = ""
    for char in text:
        if is_letter(char):
            transformed_text += kucuk_harf(char)
        else:
            transformed_text += char
    return transformed_text
