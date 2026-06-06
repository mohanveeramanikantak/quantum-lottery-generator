# 🎰 Quantum Lottery Generator

A beginner-friendly Quantum Computing project built using **Qiskit** and **Streamlit** that generates lottery numbers using quantum randomness.

---

## 📌 Project Overview

Traditional lottery generators use classical pseudo-random algorithms.

This project uses **Quantum Computing principles** to generate lottery numbers through quantum measurement, providing randomness derived from quantum superposition.

---

## 🚀 Features

* Generate lottery numbers using quantum randomness
* Unique number generation (No Duplicates)
* Multiple lottery modes

  * Classic 6/49
  * Powerball Style
  * EuroMillions Style
* Interactive Streamlit UI
* Real-time lottery generation

---

## 🧠 Quantum Concepts Used

### Qubits

Basic units of quantum information.

### Superposition

Allows qubits to exist in multiple states simultaneously.

### Hadamard Gate

Creates superposition and quantum randomness.

### Quantum Measurement

Collapses qubits into random classical states.

---

## 🛠️ Tech Stack

* Python
* Qiskit
* Qiskit Aer
* Streamlit

---

## 📂 Project Structure

```text
quantum-lottery-generator/
│
├── app.py
├── qrng.py
├── lottery.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│
└── docs/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/mohanveeramanikantak/quantum-lottery-generator.git
cd quantum-lottery-generator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🎯 Supported Lottery Modes

| Mode               | Numbers | Range  |
| ------------------ | ------- | ------ |
| Classic 6/49       | 6       | 1 - 49 |
| Powerball Style    | 5       | 1 - 69 |
| EuroMillions Style | 5       | 1 - 50 |

---

## 📊 Sample Output

```text
Quantum Lottery Numbers

4  11  18  27  35  46
```

---

## 🎓 Learning Outcomes

* Quantum Computing Fundamentals
* Qubits and Superposition
* Quantum Measurement
* Quantum Random Number Generation
* Streamlit Development
* Qiskit Framework
* Modular Python Programming

---

## 📈 Future Improvements

* Lottery History Tracking
* Export Results to CSV
* Quantum Probability Visualization
* Lucky Number Prediction Dashboard
* Quantum-Powered Number Analytics

---

## 💼 Resume Point

Built a Quantum Lottery Generator using Qiskit and Streamlit, leveraging quantum superposition and measurement principles to generate unique lottery combinations through quantum randomness.

---

## 👨‍💻 Author

**Mohan Veera Manikanta**

AI Engineer | Full Stack Developer | Product Builder

GitHub:
https://github.com/mohanveeramanikantak

LinkedIn:
https://www.linkedin.com/in/kalepu-mohan-veera-manikanta

---

## ⭐ Support

If you found this project useful, please consider giving it a star and sharing it with fellow Quantum Computing enthusiasts.

Happy Quantum Coding! 🚀⚛️
