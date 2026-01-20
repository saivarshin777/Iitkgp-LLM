# Iitkgp-LLM
Innovatrix KDSH 2026

Story Backstory Consistency Prediction

👩‍💻 Author: Varshini

⸻

📌 Problem Statement

In narrative analysis, ensuring that a story’s backstory aligns logically with the main plot is critical.
This project addresses the challenge of automatically detecting inconsistencies between a story’s backstory and its core narrative.

As part of Innovatrix KDSH 2026, this solution predicts whether a given backstory is consistent (1) or inconsistent (0) with the story.

⸻

🎯 Objective
	•	Analyze long narrative texts efficiently
	•	Predict story–backstory consistency
	•	Generate structured, explainable outputs
	•	Optimize execution speed for large datasets

📂 Project Structure

Innovatrix_KDSH__2026/
│
├── code/
│   ├── main.py                   # Main execution script
│   ├── requrirements.txt         # Required Python libraries
│   └── data/
│       ├── train.csv             # Training dataset
│       ├── test.csv              # Test dataset
│       ├── In search of the castaways.pages
│       └── The Count of Monte Cristo.pages
│
├── report/
│   └── report.pdf.pdf            # Detailed project report
│
├── results.csv                   # Final predictions
└── README.md

⚙️ Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/Innovatrix_KDSH__2026.git
cd Innovatrix_KDSH__2026

2️⃣ Install Dependencies

pip install -r code/requrirements.txt

🚀 How to Run the Project

cd code
python main.py

After execution, predictions will be saved as:

results.csv

📊 Output Format

The output file is a CSV table with the following columns:


Column                                           Description                   
story_id                                      Unique ID of the story
prediction                                    1 → Consistent, 0 → Inconsistent
rationale                                   Explanation for the prediction

🧠 Methodology
	•	Preprocessing and chunking long narrative texts
	•	Logical consistency checks between story and backstory
	•	Optimized iteration for faster execution
	•	Clear, interpretable prediction logic

⸻

✨ Key Features

✔ Handles long story texts efficiently
✔ Produces clean tabular output
✔ Execution speed optimized
✔ Easy to reproduce and evaluate

⸻

📄 Report

A detailed explanation of the approach, design decisions, and results is available in:

report/report.pdf.pdf

🛠️ Technologies Used
	•	Python
	•	Pandas
	•	tqdm

⸻

🏁 Hackathon Context

This project was developed as part of Innovatrix KDSH 2026, focusing on:
	•	Problem understanding
	•	Clean implementation
	•	Output clarity
	•	Practical efficiency

⸻

⭐ Acknowledgements

Thanks to the Innovatrix KDSH 2026 organizers for the opportunity and dataset.

⸻
