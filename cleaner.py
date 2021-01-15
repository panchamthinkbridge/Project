import os
import glob
import argparse

def text_cleaner(fileName):
    with open(fileName, encoding='utf8', errors='ignore') as reader:
        text = reader.read()
        text = " ".join(text.split())
        reader.close()

    return text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    args = parser.parse_args()

    folderName = 'Clean-JD'
    os.makedirs(folderName)
    fileGLOB = glob.glob(f'{args.path}\*.txt') #get path of all text files

    for file in fileGLOB:
        text = text_cleaner(file)
        fname = file.split('\\')[1]
        print(fname)
        with open(f'{folderName}\clean-{fname}', 'w',encoding='utf8', errors='ignore') as writer:
            writer.write(text)
        writer.close()
        

    print('DONE')
    print("SUCCESS")