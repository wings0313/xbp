# 音楽データベースを用意
music_recommendations = {
    "ポップ": ["Taylor Swift - Shake It Off", "Bruno Mars - Uptown Funk", "Dua Lipa - Levitating"],
    "ロック": ["Queen - Bohemian Rhapsody", "AC/DC - Back In Black", "Nirvana - Smells Like Teen Spirit"],
    "ジャズ": ["Miles Davis - So What", "John Coltrane - Giant Steps", "Billie Holiday - All of Me"],
    "クラシック": ["Ludwig van Beethoven - Symphony No.5", "Wolfgang Amadeus Mozart - Eine kleine Nachtmusik", "Frédéric Chopin - Nocturne op.9 No.2"],
    "リラックス": ["Yiruma - River Flows in You", "Joe Hisaishi - Summer", "Enya - Only Time"],
    "エネルギッシュ": ["Survivor - Eye of the Tiger", "Daft Punk - Harder, Better, Faster, Stronger", "Eminem - Lose Yourself"],
    "ラテン": ["Luis Fonsi - Despacito", "Shakira - Hips Don't Lie", "Daddy Yankee - Gasolina"],
    "ヒップホップ": ["Kendrick Lamar - HUMBLE.", "Drake - God's Plan", "Travis Scott - Sicko Mode"]
}

# おすすめの音楽を教えてくれる関数
def recommend_music():
    print("おすすめの音楽ジャンルを入力してください（例: ポップ, ロック, ジャズ, クラシック, リラックス, エネルギッシュ, ラテン, ヒップホップ）:")
    genre = input("ジャンル: ")

    # 入力されたジャンルに応じておすすめの曲を表示
    if genre in music_recommendations:
        print(f"\nジャンル '{genre}' のおすすめ音楽:")
        for song in music_recommendations[genre]:
            print(f"- {song}")
    else:
        print("\n申し訳ありません、そのジャンルは見つかりませんでした。")
        print("利用可能なジャンル: ", ", ".join(music_recommendations.keys()))

# プログラムの実行
if __name__ == "__main__":
    recommend_music()
