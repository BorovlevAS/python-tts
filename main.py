from cmath import inf
from pathlib import Path
from pdfminer import high_level

def process_file(file_name, lang):

    path = Path(file_name)

    if (not path.is_file()) | (path.suffix != '.pdf'):
        print(f"Can't process {file_name}")
        return
    
    
    

def main():
    process_file('F:\\python-projects\\vscode-test\\PDF_Converter_Pro_Quick_Reference_Guide.RU.pdf', 'en')

if __name__ == '__main__':
    main()