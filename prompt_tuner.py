from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

def tune_prompt(scene, style="cartoon"):
    try:
        result = emotion_classifier(scene)
        if isinstance(result, list) and isinstance(result[0], dict):
            emotion = result[0].get("label", "neutral").lower()
        elif isinstance(result, dict) and "label" in result:
            emotion = result["label"].lower()
        else:
            raise TypeError("Unexpected structure returned by emotion classifier")
    except Exception as e:
        print("⚠️ Emotion detection failed:", e)
        emotion = "neutral"

    prompt = f"{style} style, {emotion} mood, scene: {scene[:120]}"
    print(f"🧠 Emotion: {emotion} | Prompt: {prompt}")
    return emotion, prompt
