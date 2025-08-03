# 🔍 Code Snippet Generation using Fine-Tuned T5

This project is a code snippet generation system built using a fine-tuned [T5-small](https://huggingface.co/t5-small) model. It takes natural language programming queries and returns relevant code snippets. A simple web interface is built using Streamlit.

---

## 📌 Features

- Fine-tuned T5 on natural language → code mapping
- Streamlit-based frontend for live query testing
- Easily extendable to other languages or domains

---

## 📂 Directory Structure

├── app/
│ └── streamlit_app.py # Streamlit frontend
├── src/
│ └── train_t5.py # Model training script
├── data/
│ └── extended_programming_code_snippets.csv # Dataset
├── t5_finetuned_model/ # Fine-tuned model (excluded from Git)
├── requirements.txt
├── .gitignore
└── README.md


---

## 📊 Dataset

File: `data/extended_programming_code_snippets.csv`  
The dataset consists of three columns:

| Column        | Description                             |
|---------------|-----------------------------------------|
| `Query`       | Natural language programming query      |
| `Code_Snippet`| Expected output code                    |
| `Tags`        | (Optional) Tags like language/domain    |

---

## 🏋️‍♂️ Training the Model

1. Prepare your dataset at `./data/extended_programming_code_snippets.csv`
2. Run the training script:

```bash
python src/train_t5.py


This will save the fine-tuned model and tokenizer to:
./t5_finetuned_model/

🌐 Running the Streamlit App
After training, you can run the frontend locally:

1. Install dependencies

pip install -r requirements.txt

 Start the app

streamlit run app/streamlit_app.py

Sample Output
Query: how to sort a list in python

my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()
print(my_list)


🧰Tech Stack
Hugging Face Transformers

PyTorch

Streamlit

Google Colab (for training)

📌 Notes
The model (t5_finetuned_model/) is excluded from the repo to avoid large file uploads. You should train or manually place it locally.

You can upload the trained model to Hugging Face Hub or Google Drive for deployment.


📄 License
MIT License © 2025 Vishal Meena

👨‍💻 Author
Vishal Meena
IIT Kharagpur
🔗 [LinkedIn](https://linkedin.com/in/vishalmeenaiit)



