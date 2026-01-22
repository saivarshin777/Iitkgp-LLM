import pandas as pd
from tqdm import tqdm

# ---------------- CONFIG ----------------
TRAIN_PATH = "train.csv"
TEST_PATH = "test.csv"
OUTPUT_PATH = "results.csv"

# ---------------- HELPERS ----------------
def find_column(possible_names, columns):
    for name in possible_names:
        if name in columns:
            return name
    raise ValueError(f"Missing column from {possible_names}")

def chunk_text(text, chunk_size=800):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def retrieve_chunks(sentence, chunks, k=3):
    sentence_words = set(sentence.lower().split())
    scored = []

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(sentence_words & chunk_words)
        if score > 0:
            scored.append((score, chunk))

    scored.sort(reverse=True)
    return [c for _, c in scored[:k]]

# ---------------- MAIN ----------------
def main():
    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    print("✔ train.csv columns:", list(train_df.columns))
    print("✔ test.csv columns:", list(test_df.columns))

    id_col = find_column(["id", "story_id"], test_df.columns)
    novel_col = find_column(["content"], test_df.columns)
    backstory_col = find_column(["caption"], test_df.columns)

    results = []

    for _, row in tqdm(test_df.iterrows(), total=len(test_df)):
        story_id = row[id_col]
        novel = str(row[novel_col])
        backstory = str(row[backstory_col])

        contradiction_sentences = []
        chunks = chunk_text(novel)

        for sentence in backstory.split("."):
            sentence = sentence.strip()
            if len(sentence) < 5:
                continue

            evidence = retrieve_chunks(sentence, chunks)
            if not evidence:
                contradiction_sentences.append(sentence)

        # -------- FINAL DECISION --------
        if contradiction_sentences:
            prediction = 0
            rationale = "; ".join(contradiction_sentences[:2])
        else:
            prediction = 1
            rationale = "Backstory is consistent with the story narrative"

        results.append({
            "story_id": story_id,
            "prediction": prediction,
            "rationale": rationale
        })

    pd.DataFrame(results).to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Done! {OUTPUT_PATH} created successfully.")

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()
