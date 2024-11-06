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
        print("Invalid choice. Please choose again.")
        first_choice()

# 森の中に入る
def enter_forest():
    print("\nYou bravely enter the forest, but it's eerily quiet.")
    time.sleep(1)
    print("Suddenly, a wild wolf appears!")
    print("1. Fight the wolf")
    print("2. Run away")
    
    choice = input("What will you do? (1/2): ")
    
    if choice == "1":
        fight_wolf()
    elif choice == "2":
        run_away()
    else:
        print("Invalid choice. Please choose again.")
        enter_forest()

# 森の端を歩く
def walk_along_edge():
    print("\nYou walk along the edge of the forest, avoiding any dangers inside.")
    time.sleep(1)
    print("After a while, you find a small village. You decide to rest there.")
    end_game()

# オオカミと戦う
def fight_wolf():
    print("\nYou decide to fight the wolf!")
    time.sleep(1)
    if player["strength"] >= 10:
        print("You swing your sword and defeat the wolf!")
        player["inventory"].append("Wolf Pelt")
        print("You have obtained a Wolf Pelt.")
    else:
        print("The wolf is too strong! You are injured.")
        player["health"] -= 20
    time.sleep(1)
    end_game()

# 逃げる
def run_away():
    print("\nYou run away from the wolf, escaping back to safety.")
    time.sleep(1)
    end_game()

# ゲーム終了
def end_game():
    print("\nYour adventure has come to an end.")
    print(f"Final stats for {player['name']}:")
    print(f"Health: {player['health']}")
    print(f"Strength: {player['strength']}")
    print(f"Inventory: {player['inventory']}")
    print("Thank you for playing!")

# ゲームを開始する
start_game()
