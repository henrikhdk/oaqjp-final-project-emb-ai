# Emotion Detection Python Module

This project demonstrates how to use the `emotion_detection` module to analyze the emotions expressed in text using Python.

## 📦 Requirements

- Python 3.6+
- `requests` library
- `emotion_detection` module (must be installed or available in your environment)

## 🚀 Getting Started

Follow the steps below to set up and run the emotion detection example.

### 1. Clone or download this repository

If applicable, clone this repo or make sure the `emotion_detection` module is available in your project directory.

### 2. Install dependencies

Make sure you have `requests` installed. You can install it via pip:

```bash
python3 -m pip install requests
```

### 3. Run the Emotion Detector
Here is a simple usage example:

```python
from emotion_detection import emotion_detector

result = emotion_detector("I love this new technology.")
print(result)
```

Expected output:
```python
{
  'dominant_emotion': 'joy',
  'anger': 0.01,
  'disgust': 0.0,
  'fear': 0.0,
  'joy': 0.98,
  'sadness': 0.01
}
```
