import os
import random


def split_dataset(input_file, train_file, dev_file, test_file, train_ratio=0.8, dev_ratio=0.1):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = infile.read().strip().split('\n\n')

    random.shuffle(data)
    total = len(data)
    train_count = int(total * train_ratio)
    dev_count = int(total * dev_ratio)

    train_data = data[:train_count]
    dev_data = data[train_count:train_count + dev_count]
    test_data = data[train_count + dev_count:]

    with open(train_file, 'w', encoding='utf-8') as train_out:
        train_out.write('\n\n'.join(train_data) + '\n')

    with open(dev_file, 'w', encoding='utf-8') as dev_out:
        dev_out.write('\n\n'.join(dev_data) + '\n')

    with open(test_file, 'w', encoding='utf-8') as test_out:
        test_out.write('\n\n'.join(test_data) + '\n')

    print(f"Data split into train: {len(train_data)}, dev: {len(dev_data)}, test: {len(test_data)}")


if __name__ == "__main__":
    input_file = "../Outputs/merged_bio.txt"
    train_file = "../Outputs/train.txt"
    dev_file = "../Outputs/dev.txt"
    test_file = "../Outputs/test.txt"
    split_dataset(input_file, train_file, dev_file, test_file)
    print("Dataset splitting completed.")