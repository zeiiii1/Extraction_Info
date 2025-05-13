import spacy
from spacy.scorer import Scorer
from spacy.tokens import DocBin
import os


def evaluate_model(model_path, test_file):
    nlp = spacy.load(model_path)
    doc_bin = DocBin().from_disk(test_file)
    docs = list(doc_bin.get_docs(nlp.vocab))

    scorer = Scorer()
    for doc in docs:
        predicted = nlp(doc.text)
        scorer.score(predicted, doc)

    scores = scorer.score
    print(f"Precision: {scores['ents_p']}")
    print(f"Recall: {scores['ents_r']}")
    print(f"F1 Score: {scores['ents_f']}")


if __name__ == "__main__":
    model_path = "./output/model-best"
    test_file = "../Outputs/test.spacy"
    evaluate_model(model_path, test_file)
    print("Evaluation completed.")
