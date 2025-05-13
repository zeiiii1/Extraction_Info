import spacy
from spacy.tokens import DocBin
import os


def convert_to_spacy(input_file, output_file):
    nlp = spacy.blank("fr")  # Blank French model
    doc_bin = DocBin()

    with open(input_file, 'r', encoding='utf-8') as infile:
        data = infile.read().strip().split('\n\n')

    for entry in data:
        words = []
        entities = []
        offset = 0
        for line in entry.split('\n'):
            if line.strip():
                token, label = line.split()
                words.append(token)
                if label != "O":
                    entity_label = label.split('-')[-1]
                    start = offset
                    end = start + len(token)
                    entities.append((start, end, entity_label))
                offset += len(token) + 1

        doc = nlp.make_doc(" ".join(words))
        spans = [doc.char_span(start, end, label=label) for start, end, label in entities if doc.char_span(start, end, label=label)]
        doc.ents = spans
        doc_bin.add(doc)

    doc_bin.to_disk(output_file)
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    convert_to_spacy("../Outputs/train.txt", "../Outputs/train.spacy")
    convert_to_spacy("../Outputs/dev.txt", "../Outputs/dev.spacy")
    convert_to_spacy("../Outputs/test.txt", "../Outputs/test.spacy")
    print("Conversion to SpaCy format completed.")
