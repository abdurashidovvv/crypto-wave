from datasets import load_dataset
from collections import Counter
import re

print("Dataset yuklanmoqda...")

dataset = load_dataset("murodbek/uz-text-classification", split="train")
print(f"✅ Yuklandi! Jami maqolalar: {len(dataset)}")

# O'zbek apostrofining barcha variantlari → oddiy apostrof
APOSTROPHS = [
    "\u0060",  # ` backtick (96)
    "\u02BB",  # ʻ modifier letter (699)
    "\u2018",  # ' left quote (8216)
    "\u2019",  # ' right quote (8217)
]

word_counter = Counter()

for i in range(len(dataset)):
    text = dataset[i]["text"].lower()

    # Barcha apostrof variantlarini birlashtirамiz
    for apos in APOSTROPHS:
        text = text.replace(apos, "'")

    # So'zlarni ajratamiz
    words = re.findall(r"[a-z']+", text)

    for word in words:
        word = word.strip("'")
        if len(word) >= 3:
            word_counter[word] += 1

    if i % 50000 == 0:
        print(f"  {i:,} / {len(dataset):,} qayta ishlandi...")

top_words = [word for word, _ in word_counter.most_common(10000)]

print(f"\nTop 10 so'z: {top_words[:10]}")

with open("app/words.txt", "w", encoding="utf-8") as f:
    for word in top_words:
        f.write(word + "\n")

print(f"✅ app/words.txt yangilandi — {len(top_words):,} so'z!")