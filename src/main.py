import argparse
import io

from google.cloud import vision
from pdf2image import convert_from_path


def pic_to_text(infile):
    """Detects text in an image file

    ARGS
    infile: path to image file

    RETURNS
    String of text detected in image
    """

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Opens the input image file
    with io.open(infile, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # For dense text, use document_text_detection
    # For less dense text, use text_detection
    response = client.document_text_detection(image=image)
    text = response.full_text_annotation.text
    print("Detected text: {}".format(text))

    return text


def arg_parser():
    parser = argparse.ArgumentParser(description='Google vision pdf to text')
    parser.add_argument('--pdf', help='File path of pdf')
    parser.add_argument('--dpi', help='DPI for pdf to jpeg', default=500, type=int)
    parser.add_argument('--output_file', help='output text file', default="./data/output.txt")
    return parser.parse_args()


def write_text(file_name, data=''):
    file = open(file_name, "a")
    file.write(data)
    file.close()


def create_temporary_text_file(number):
    return './data/text/' + str(number) + '_out.txt'


def create_temporary_jpeg_file(number):
    return './data/images/' + str(number) + '.jpg'


def create_page_end_line(number):
    return '\n----------- Page End : ' + str(number) + '-----------\n'


if __name__ == '__main__':
    pdf = arg_parser().pdf
    dpi = arg_parser().dpi
    output_file = arg_parser().output_file

    pages = convert_from_path(pdf, dpi)

    for page_number in range(0, len(pages)):
        f = open(create_temporary_jpeg_file(page_number + 1), 'a')
        f.close()
        pages[page_number].save(create_temporary_jpeg_file(page_number + 1), 'JPEG')

    data = []
    for page_number in range(0, len(pages)):
        text = pic_to_text(create_temporary_jpeg_file(page_number + 1))
        data.append(text)
        write_text(create_temporary_text_file(page_number + 1), text)

    all_out = open(output_file, 'a')
    for page_number in range(0, len(pages)):
        f = open(create_temporary_text_file(page_number + 1), 'r')
        all_out.write(f.read())
        all_out.write(create_page_end_line(page_number + 1))
        f.close()
    all_out.close()
