from googletrans import Translator

# 翻訳する関数
def translate_lyrics(lyrics, target_language='ja'):
    # Translatorのインスタンスを作成
    translator = Translator()
    
    # 翻訳を実行
    translated = translator.translate(lyrics, dest=target_language)
    
    # 翻訳結果を返す
    return translated.text

# プログラムの実行
if __name__ == "__main__":
    print("翻訳したい歌詞を入力してください（英語などの歌詞を日本語に翻訳する場合など）:")
    original_lyrics = input("歌詞: ")
    
    print("\n翻訳したい言語を入力してください（例: ja = 日本語, en = 英語, es = スペイン語,ko = 韓国語）:")
    target_language = input("言語コード: ").strip()
    
    # 歌詞を翻訳
    translated_lyrics = translate_lyrics(original_lyrics, target_language)
    
    # 結果を表示
    print("\n翻訳された歌詞:")
    print(translated_lyrics)
