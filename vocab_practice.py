#!/usr/bin/env python3
import json
import random
import os

WORDS_FILE = os.path.join(os.path.dirname(__file__), "words.json")

def load_words():
    if not os.path.exists(WORDS_FILE):
        return []
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_words(words):
    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

def add_word(words):
    word = input("英文單字: ").strip()
    if not word:
        print("單字不可為空。")
        return
    meaning = input("中文或英文解釋: ").strip()
    if not meaning:
        print("解釋不可為空。")
        return
    words.append({"word": word, "meaning": meaning})
    save_words(words)
    print("已新增。")

def practice(words):
    if not words:
        print("沒有單字，請先新增。")
        return
    n = input("題目數（預設10）: ").strip()
    try:
        n = int(n) if n else 10
    except:
        n = 10
    correct = 0
    for i in range(n):
        correct_item = random.choice(words)
        others = [w for w in words if w != correct_item]
        if len(others) >= 3:
            distractors = random.sample(others, 3)
            options = [correct_item["meaning"]] + [d["meaning"] for d in distractors]
            random.shuffle(options)
            print(f"\n題目 {i+1}: {correct_item['word']}")
            for idx,opt in enumerate(options,1):
                print(f"  {idx}. {opt}")
            ans = input("答案數字: ").strip()
            if ans.isdigit() and 1 <= int(ans) <= len(options):
                if options[int(ans)-1] == correct_item["meaning"]:
                    print("正確")
                    correct += 1
                else:
                    print("錯誤，正確答案:", correct_item["meaning"])
            else:
                print("跳過，正確答案:", correct_item["meaning"])
        else:
            print(f"\n題目 {i+1}: {correct_item['word']}")
            ans = input("請輸入解釋（輸入空白以顯示答案）: ").strip()
            if ans and ans.strip().lower() == correct_item["meaning"].strip().lower():
                print("正確")
                correct += 1
            else:
                print("答案:", correct_item["meaning"])
    print(f"\n完成：{correct}/{n} 正確")

def list_words(words):
    if not words:
        print("無單字。")
        return
    for i,w in enumerate(words,1):
        print(f"{i}. {w['word']} — {w['meaning']}")

def main():
    words = load_words()
    while True:
        print("\n選單：")
        print("1. 練習")
        print("2. 新增單字")
        print("3. 列出單字")
        print("4. 結束")
        choice = input("請選擇: ").strip()
        if choice == "1":
            practice(words)
        elif choice == "2":
            add_word(words)
        elif choice == "3":
            list_words(words)
        elif choice == "4" or choice.lower() in ("q","exit"):
            break
        else:
            print("無效選項")

if __name__ == "__main__":
    main()
