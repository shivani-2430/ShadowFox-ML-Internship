# ShadowFox Autocorrect System

## Overview

The ShadowFox Autocorrect System is a Python application that identifies potentially misspelled English words and suggests spelling corrections using the `pyspellchecker` library.

## Objectives

- Identify common spelling mistakes.
- Automatically correct words in a sentence.
- Display alternative spelling suggestions.
- Preserve basic capitalization and punctuation.
- Evaluate the behavior of the spell checker through automated tests.

## Technologies Used

- Python 3.11
- pyspellchecker
- Regular expressions
- unittest

## Project Structure

```text
Autocorrect-System/
├── src/
│   ├── __init__.py
│   ├── autocorrect.py
│   └── main.py
├── tests/
│   └── test_autocorrect.py
├── requirements.txt
└── README.md
```

## Setup and Installation

1. Install Python 3.11.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Install the dependency.

```powershell
python -m pip install -r requirements.txt
```

## Running the Application

Run the following command from the project directory:

```powershell
python -m src.main
```

Enter a word or sentence to view the original text, corrected text, and available alternative suggestions. Enter `exit` to close the application.

## Running Tests

```powershell
python -m unittest discover -s tests -v
```

The initial automated test suite contains five tests covering word correction, sentence correction, empty input, punctuation, and alternative suggestions.

## Evaluation

The initial test suite completed successfully with five passing tests. This confirms that the tested functions behaved as expected for those cases.

Further evaluation should cover additional spelling mistakes, valid words, capitalization, punctuation, and sentences with ambiguous words.

## Limitations

- A dictionary-based spell checker may replace a valid word with another word.
- Alternative suggestions may include words that change the intended meaning.
- The current implementation is designed for English spelling correction, not grammar correction or semantic understanding.
- Test success does not establish real-world accuracy across all text inputs.

## Future Improvements

- Improve handling of words that are already correct.
- Add broader test cases and evaluate correction accuracy.
- Build a user-friendly interface.
- Explore deployment options for real-world use.

## Internship Task

This project addresses the Beginner-level autocorrect task described in the ShadowFox Machine Learning Engineer Internship task documents.
Objective: spelling correction and contextual next-word suggestions.


note:
Technologies: Python 3.11.9, pyspellchecker 0.9.1, and an n-gram model.
Methodology: tokenization, spelling correction, unigram/bigram/trigram counting, and prediction.
Testing: nine unit tests, with their actual results.
Limitations: small built-in corpus, limited vocabulary, and predictions based on observed word sequences.
Future improvements: larger text corpus, quantitative evaluation, and a graphical interface.
