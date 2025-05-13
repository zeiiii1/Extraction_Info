import spacy


def predict_entities(model_path, text):
    nlp = spacy.load(model_path)
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities


if __name__ == "__main__":
    model_path = "./output/model-best"
    sample_text = input("Enter a medical text to analyze: ")
    predictions = predict_entities(model_path, sample_text)
    if predictions:
        for entity, label in predictions:
            print(f"Entity: {entity} | Label: {label}")
    else:
        print("No entities detected.")
