# Advanced NLP Project: DistilBERT Sentiment Analysis

## Overview

This project explores sentiment analysis using a pretrained DistilBERT language model. It investigates how a transformer-based model classifies text and how its predictions behave when presented with different linguistic patterns.

The project was developed as part of the ShadowFox Machine Learning Engineer Internship.

## Objectives

- Implement a pretrained sentiment analysis model.
- Evaluate predictions on different types of text inputs.
- Examine confidence scores and unexpected predictions.
- Investigate the limitations of binary sentiment classification.
- Discuss ethical considerations, practical applications, and future improvements.

## Model

- **Model:** DistilBERT fine-tuned for sentiment analysis
- **Model identifier:** `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
- **Framework:** PyTorch
- **Model library:** Hugging Face Transformers
- **Environment:** Python and Jupyter Notebook

The selected model predicts either `POSITIVE` or `NEGATIVE` sentiment.

## Experiments

The notebook evaluates examples covering:

- Clearly positive and negative sentences
- Negation
- Mixed sentiment
- Sarcasm
- Neutral or factual statements
- Short and ambiguous inputs

The results demonstrate that the model can classify straightforward examples while struggling to represent neutral, ambiguous, or mixed sentiment using only two output labels.

## Key Findings

In an exploratory test of 10 manually selected examples, 7 predictions matched their manually assigned expected labels. The model also produced confident predictions for some neutral or ambiguous inputs that did not adequately represent the intended meaning.

This small test set is illustrative and does not establish the model's general accuracy.

## Limitations

- Only positive and negative sentiment labels are available.
- Sarcasm and context-dependent language may be misinterpreted.
- Confidence scores do not guarantee correctness.
- The manually selected test set is too small to establish general performance.

## Ethical Considerations

Sentiment predictions can be biased or misleading. Real-world use should account for privacy, fairness, contextual interpretation, and human oversight.

## Future Improvements

- Evaluate a model that supports neutral sentiment.
- Test on a larger labeled dataset.
- Compare multiple sentiment analysis models.
- Investigate confidence calibration and domain-specific performance.

## How to Run

1. Install Python 3.11 or a compatible Python version.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

4. Open `DistilBERT_Sentiment_Analysis.ipynb` and run the cells from top to bottom.

The pretrained model may need to download its files from Hugging Face on the first run, so an internet connection is required.

## Project Structure

```text
NLP-Language-Model/
├── DistilBERT_Sentiment_Analysis.ipynb
├── README.md
└── requirements.txt
```

## Conclusion

This project demonstrates practical use of a pretrained transformer model for sentiment analysis and explores its behavior across different text inputs. The findings highlight the importance of evaluating predictions critically rather than relying solely on confidence scores.