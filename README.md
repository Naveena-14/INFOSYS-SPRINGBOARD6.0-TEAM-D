# AI Cover Letter Generator

## Overview

This project generates personalized cover letters using AI by analyzing a user's resume and job description.

The system uses Large Language Models (LLMs) to tailor the cover letter according to the role requirements, helping job seekers quickly create professional applications.

## Features

* Upload resume for analysis
* Input job description
* AI-generated personalized cover letters
* Modular architecture for prompt routing and LLM interaction
* Easy to extend with other LLM APIs

## Project Structure

app.py — Main application entry point
file_reader.py — Handles resume/document parsing
llm_handler.py — Manages LLM interactions
prompt_router.py — Builds prompts for cover letter generation

## Installation

1. Clone the repository

git clone https://github.com/Naveena-14/Cover-Letter-Generator.git

2. Navigate to the project folder

cd Cover-Letter-Generator

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python app.py

## Future Improvements

* Add web interface
* Support multiple LLM providers
* Improve prompt engineering
* Export generated cover letters as PDF

## License

This project is licensed under the MIT License.
