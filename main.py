from pathlib import Path
from pdfminer import high_level
from gtts import gTTS

def process_file(file_name, language):

    path = Path(file_name)

    if (not path.is_file()) | (path.suffix != '.pdf'):
        print(f"Can't process {file_name}")
        return
    
    print('Start reading file...')

    with open(file_name, 'rb') as fpdf:
        text = high_level.extract_text(fpdf)

    text = text.replace('\n', '')
    tts = gTTS(text, lang = language)

    print('Generating mp3...')
    fname = path.name.replace(path.suffix, '') + '.mp3'
    with open(fname, 'wb') as fmp3:
        tts.write_to_fp(fmp3)

    print(f'File {fname} was generated!')

    # sklfdjlksdjfl
    

def main():
    process_file('F:\\python-projects\\vscode-test\\PDF_Converter_Pro_Quick_Reference_Guide.RU.pdf', 'ru')

if __name__ == '__main__':
    main()