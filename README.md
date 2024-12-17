# AI-Powered Data Transformation Framework

## Overview

This project implements an intelligent data transformation system that leverages Large Language Models (LLMs) to generate and apply data transformations based on natural language queries.

## Key Features

- 🤖 AI-Driven Transformation Generation
- 🔬 Modular Transform Architecture
- 🧩 Extensible Design
- 💡 Natural Language to Data Transformation

## Project Structure

data_transformer/
│
├── transforms/         # Data transformation implementations
│   ├── base_transform.py
│   ├── column_selector.py
│   ├── filter_transform.py
│   └── aggregation_transform.py
│
├── llm_generator/      # LLM-powered transformation generation
│   ├── prompt_builder.py
│   ├── transform_generator.py
│   └── validator.py
│
└── main.py             # Main execution script

## Installation

```bash
git clone https://github.com/yourusername/ai-powered-data-transformation.git
cd ai-powered-data-transformation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

Quick Start

Set your OpenAI API key:

bashCopyexport OPENAI_API_KEY='your_openai_api_key_here'

Prepare your input CSV file
Run the transformation:

bashCopypython main.py
How It Works
1. Transform Layer

Abstract base class for data transformations
Supports multiple transformation types:

Column Selection
Filtering
Aggregation



2. LLM Generation Layer

Converts natural language queries to structured transforms
Uses OpenAI's GPT models
Generates validated transformation sequences
