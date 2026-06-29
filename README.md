
---

## Project 4: eliza-vs-llm-chatbot

```markdown
# ELIZA vs LLM Chatbot Comparison

> Interactive desktop application comparing the rule-based ELIZA chatbot (1960s) with a modern simulated LLM, side-by-side in real-time.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green.svg)
![NLP](https://img.shields.io/badge/NLP-Chatbot-red.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

---

## Table of Contents

- [Overview](#overview)
- [The Problem It Solves](#the-problem-it-solves)
- [Key Features](#key-features)
- [ELIZA vs LLM: The Difference](#eliza-vs-llm-the-difference)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Author](#author)

---

## Overview

This project implements an **interactive desktop application** that compares two generations of AI chatbots side-by-side:

1. **ELIZA (1960s)** – A rule-based chatbot using pattern matching and keyword detection
2. **Simulated LLM (Present)** – A modern context-aware chatbot with more natural responses

The application features a clean dual-panel GUI built with Python Tkinter, allowing users to send messages to both chatbots simultaneously and compare their responses in real-time.

---

## The Problem It Solves

The evolution of AI chatbots represents a significant milestone in AI history:

- **Understanding AI Progress:** How has conversational AI evolved from the 1960s to today?
- **Comparing Approaches:** What are the strengths and weaknesses of rule-based vs. learning-based systems?
- **Educational Tool:** How can students visualise the difference between old and new AI?

**The Challenge:** Most people don't understand the difference between a simple pattern-matching chatbot and a modern AI. This tool makes the comparison visual, interactive, and intuitive.

---

## ✨ Key Features

### ELIZA Features
- ✅ **Rule-based pattern matching** using regular expressions
- ✅ **10+ conversation rules** covering greetings, introductions, emotions, and exams
- ✅ **Random response variation** for natural conversation flow
- ✅ **Dynamic response generation** with captured groups

### LLM Features
- ✅ **Keyword-based response system** with context awareness
- ✅ **10+ conversation categories** including stress, exams, and tiredness
- ✅ **Random variation** for natural conversation feel

### GUI Features
- ✅ **Dual-panel display** showing both chatbots side-by-side
- ✅ **Real-time comparison** – send one message, see two responses
- ✅ **Multi-threading** to prevent UI freezing for LLM responses
- ✅ **Dark theme UI** with professional styling
- ✅ **Clear chat functionality**
- ✅ **Keyboard shortcut** (Enter to send)

---

## ELIZA vs LLM: The Difference

| **Aspect** | **ELIZA (1960s)** | **LLM (Present)** |
| :--- | :--- | :--- |
| **Approach** | Rule-based pattern matching | Machine learning / Deep learning |
| **Training** | Hand-coded rules by humans | Trained on billions of text examples |
| **Understanding** | Limited to pre-defined patterns | Understands context and nuance |
| **Flexibility** | Rigid – only responds to known patterns | Flexible – handles novel inputs |
| **Emotional Intelligence** | Simulated with generic responses | More empathetic and context-aware |
| **Memory** | No memory of previous conversation | Limited context memory |
| **Example Response** | "Why do you feel stressed?" | "I understand stress can be difficult. Would you like to talk about what's bothering you?"

## Installation
Prerequisites
Python 3.8 or higher

No external dependencies required (all libraries are built-in)

## Steps
1. Clone the repository:


git clone https://github.com/decodb/eliza-vs-llm-chatbot.git
cd eliza-vs-llm-chatbot
2. Run the application:

python main.py

## How to Use the Application
1. Type your message in the input box at the bottom
2. Press Enter or click the "Compare" button
3. Watch both chatbots respond simultaneously in their respective panels
4. Compare the responses side-by-side
5. Click "Clear" to reset both chat windows

## Author
Kulani Maphosa
GitHub: decodb
LinkedIn: Kulani Maphosa
Email: kulanimaphosa@gmail.com


