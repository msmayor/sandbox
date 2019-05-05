import boto3

if __name__ == "__main__":

    bucket='miguelmayorbucket'
    photo='WholesomeMeme.jpg'

    #This calls the needed AWS Service
    clientRek=boto3.client('rekognition')
    clientTran=boto3.client('translate')
    
    #This calls a specific function of the AWS Service
    responseRek=clientRek.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    textDetections=responseRek['TextDetections']
    testlist =[]

    for text in textDetections:
        testlist.append(text['DetectedText'])
    toSentence=' '.join(testlist)

    responseTran=clientTran.translate_text(Text=toSentence, SourceLanguageCode="en", TargetLanguageCode="fr")
    
    print('Original Text: ' + toSentence)
    print('Translated Text: ' + responseTran.get('TranslatedText'))

    
