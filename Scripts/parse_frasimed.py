import os
import re


def parse_frasimed(input_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.ann'):
                    ann_path = os.path.join(root, file)
                    txt_path = ann_path.replace('.ann', '.txt')

                    if os.path.exists(txt_path):
                        with open(txt_path, 'r', encoding='utf-8') as txt_file:
                            text = txt_file.read()

                        entities = parse_annotations(ann_path)
                        tokens = text.split()
                        current_entity = None
                        previous_label = "O"
                        previous_end = 0

                        for i, token in enumerate(tokens):
                            token_start = text.find(token, previous_end)
                            token_end = token_start + len(token)
                            label = 'O'

                            for entity in entities:
                                if entity['start'] <= token_start < entity['end'] or (current_entity and current_entity['label'] == entity['label'] and current_entity['end'] == token_start):
                                    if current_entity and current_entity['label'] == entity['label']:
                                        # Continue l'entité multi-token
                                        current_entity['end'] = token_end
                                        label = "I-" + entity['label']
                                    else:
                                        # Nouvelle entité ou début d'une entité multi-token
                                        current_entity = {'label': entity['label'], 'start': token_start, 'end': token_end}
                                        label = "B-" + entity['label']
                                    break

                            # Si le label est différent, réinitialiser l'entité courante
                            if current_entity and current_entity['end'] < token_start:
                                current_entity = None
                            if label == "O":
                                current_entity = None

                            outfile.write(f"{token} {label}\n")
                            previous_end = token_end + 1  # Avancer pour le prochain token

                        outfile.write("\n")


def parse_annotations(ann_path):
    entities = []
    with open(ann_path, 'r', encoding='utf-8') as ann_file:
        for line in ann_file:
            parts = line.strip().split('\t')
            if len(parts) >= 3 and parts[0].startswith('T'):
                tag_info = parts[1].split()
                label = tag_info[0]
                start = int(tag_info[1])
                end = int(tag_info[-1])
                entities.append({"label": label, "start": start, "end": end})
    return entities


if __name__ == "__main__":
    input_dir = "../Corpus/FRASIMED/"
    output_file = "../Outputs/frasimed_bio.txt"
    parse_frasimed(input_dir, output_file)
    print("FRASIMED parsing completed.")
