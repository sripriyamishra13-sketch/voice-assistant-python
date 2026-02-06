import wikipedia

def search(topic):
    try:
        return wikipedia.summary(topic, sentences=2)
    except:
        return "No information found"