import requests  # Import the requests library to handle HTTP requests
import json
import numpy

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the status code is 200, extract emotion scores from the response
    if response.status_code == 200:      
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
        # Find the dominant emotion
        emotion_list = ['anger','disgust','fear','joy','sadness']
        score_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        dominant_emotion = emotion_list[numpy.argmax(score_list)]
    # If the status code is 400, set the values to None
    elif response.status_code == 400: 
        anger_score = disgust_score = fear_score = joy_score = sadness_score = dominant_emotion = None
        
    # Returning a dictionary containing emotion detection results
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            } 

