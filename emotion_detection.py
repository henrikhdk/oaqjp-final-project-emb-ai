import requests
import json

def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using Watson NLP Emotion Predict function.
    """
    # Watson NLP Emotion Predict API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Required headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    try:
        # Send POST request to Watson NLP API
        response = requests.post(url, json=input_json, headers=headers)
        
        # Convert response text to dictionary
        response_dict = json.loads(response.text)
        
        # Extract emotion predictions from the response
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        # Extract required emotions with their scores
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Create emotion scores dictionary
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        # Find the dominant emotion (emotion with highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return formatted output
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
    except requests.exceptions.RequestException as e:
        # Handle connection errors gracefully
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    except (json.JSONDecodeError, KeyError) as e:
        # Handle JSON parsing or key errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
