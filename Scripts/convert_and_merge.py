import os


def merge_files(frasimed_file, quaero_file, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Merge FRASIMED
        with open(frasimed_file, 'r', encoding='utf-8') as f_file:
            for line in f_file:
                outfile.write(line)

        # Merge QUAERO
        with open(quaero_file, 'r', encoding='utf-8') as q_file:
            for line in q_file:
                outfile.write(line)

    print(f"Merged files into {output_file}")


if __name__ == "__main__":
    frasimed_file = "../Outputs/frasimed_bio.txt"
    quaero_file = "../Outputs/quaero_bio.txt"
    output_file = "../Outputs/merged_bio.txt"
    merge_files(frasimed_file, quaero_file, output_file)
    print("Conversion and merging completed.")