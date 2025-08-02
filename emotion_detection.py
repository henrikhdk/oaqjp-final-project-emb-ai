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
        
        # Return the text attribute of the response object
        return response.text
    except requests.exceptions.RequestException as e:
        # Handle connection errors gracefully
        return f"Error connecting to Watson NLP service: {str(e)}"
