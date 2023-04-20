# chunk the files into simple chunks of x characters with a sliding window of y characters
# usage: python chunk_simple.py --input <input_folder> --output <output_folder> --chunk_size <chunk_size> --window_size <window_size>
# example: python chunk_simple.py --input data/2-processed --output data/3-chunked --chunk_size 1000 --window_size 100

import argparse
import os
import re
import pathlib

def get_chunk(lines, start, chunk_size, window_size):
    chunk = []
    chunk_length = 0

    # walk backwards from the start line until we have enough characters
    for line in reversed(lines[:start]):
        if line.strip() == "```": # don't cross code
            break
        chunk.append(line)
        chunk_length += len(line)
        if chunk_length >= window_size:
            break
    chunk.reverse()

    # walk forwards from the start line until we have enough characters
    # make sure we take at least one line or else the algortithm might not terminate
    lines_moved = 0
    in_code = False
    for line in lines[start:]:
        if line.strip() == "```": 
            # leaving code section
            in_code = False
        elif line.strip().startswith("```"):
            # entering code section
            in_code = True
        chunk.append(line)
        lines_moved += 1
        chunk_length += len(line)
        if chunk_length >= chunk_size and not in_code:
            break
    
    return chunk, start + lines_moved


def chunk_file(input_file, output_folder, chunk_size, window_size):
    # for input file, separate folder, file and extension
    output_file_extension = pathlib.Path(input_file).suffix
    # get file name without the path and extension
    output_file_base = pathlib.Path(input_file).stem


    with open(input_file, 'r') as input_file:
        # read the file
        text = input_file.readlines()
        start = 0
        while True:
            # get the chunk
            chunk_file = f"{output_folder}/{output_file_base}-{start}{output_file_extension}"            
            chunk, start = get_chunk(text, start, chunk_size, window_size)

            # write the chunk
            with open(chunk_file, 'w') as output_file:
                output_file.writelines(chunk)
            
            # stop if we have reached the end of the file
            if start >= len(text):
                break


def chunk_files(input_folder, output_folder, chunk_size, window_size):
    # fail if the output folder does not exist
    if not os.path.exists(output_folder):
        raise Exception(f"Output folder {output_folder} does not exist")

    # delete all files in the output folder
    for filename in os.listdir(output_folder):
        os.remove(os.path.join(output_folder, filename))

    # process each file in the input folder
    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        chunk_file(input_file, output_folder, chunk_size, window_size)

if __name__ == "__main__":
    # parse the command line arguments
    parser = argparse.ArgumentParser(description='Chunk the files into simple chunks of x characters with a sliding window of y characters')
    parser.add_argument('--input', help='input folder', default='data/2-processed')
    parser.add_argument('--output', help='output folder', default='data/3-chunked/simple-4000-100/')
    parser.add_argument('--chunk_size', help='chunk size', default=4000, type=int)
    parser.add_argument('--window_size', help='window size', default=100, type=int)
    args = parser.parse_args()

    # chunk the files
    chunk_files(args.input, args.output, args.chunk_size, args.window_size)