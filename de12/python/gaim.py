import time

# プレイヤーのステータス
player = {
    "name": "",
    "health": 100,
    "strength": 10,
    "inventory": []
}

# ゲームの開始
def start_game():
    print("ようこそ冒険者の皆さん！")
    player["name"] = input("あなたの名前は何ですか？")
    print(f"こんにちは、 {player['name']}! 冒険の始まりだ！")
    time.sleep(1)
    first_choice()

# 最初の選択肢
def first_choice():
    print("\nあなたは今暗い森の入り口に立っています")
    print("1. 堂々と突き進む")
    print("2. 道に沿って端を歩く")
    
    choice = input("どれを選ぶ？(1/2): ")
    
    if choice == "1":
        enter_forest()
    elif choice == "2":
        walk_along_edge()
    else:
        print("もう一度選んでね.")
        first_choice()

# 森の中に入る
def enter_forest():
    print("\nあなたは勇敢に森へ入りますが、そこは不気味で静かです.")
    time.sleep(1)
    print("あなたは暗い森の入り口にオオカミがいることに気が付きます!")
    print("1. オオカミと戦う")
    print("2. 逃げる")
    
    choice = input("どれを選ぶ？ (1/2): ")
    
    if choice == "1":
        fight_wolf()
    elif choice == "2":
        run_away()
    else:
        print("もう一度選んでね.")
        enter_forest()

# 森の端を歩く
def walk_along_edge():
    print("\n道の端を沿って歩い、危険から免れる.")
    time.sleep(1)
    print("しばらくすると、そこに小さな村があることに気が付く.")
    end_game()

# オオカミと戦う
def fight_wolf():
    print("\nオオカミと戦うことに決めた!")
    time.sleep(1)
    if player["strength"] >= 10:
        print("券を振り、オオカミを倒せ!")
        player["inventory"].append("オオカミの毛皮")
        print("あなたはオオカミの毛皮を手に入れた.")
    else:
        print("オオカミが強すぎる、あなたはけがをした.")
        player["health"] -= 20
    time.sleep(1)
    end_game()

# 逃げる
def run_away():
    print("\nオオカミから逃げ、あなたは安全たところにたどり着く.")
    time.sleep(1)
    end_game()

# ゲーム終了
def end_game():
    print("\nあなたの冒険はこれでおわり.")
    print(f"Final stats for {player['name']}:")
    print(f"Health: {player['health']}")
    print(f"Strength: {player['strength']}")
    print(f"Inventory: {player['inventory']}")
    print("プレイしてくれてありがとう!")

# ゲームを開始する
start_game()