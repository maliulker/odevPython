import module

if __name__ == '__main__':

    module.ilk_mesaj()
    text = "Konyaspor bir gun sampiyon olacak"

    module.analyze_text(text)
    transformed_text = module.transform_text(text)

    print("Dönüştürülmüş metin:")
    print(transformed_text)

    print(module.buyuk_harf("Mecnun olup yürürüm, Ol yâri düşte görürüm, Uyanıp melûl olurum, Gel gör beni aşk neyledi"))
