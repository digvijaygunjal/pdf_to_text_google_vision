# PDF to text using Google Vision

#Clone the code?
    1.`git clone https://github.com/digvijaygunjal/pdf_to_text_google_vision.git`
    1.`cd pdf_to_text_google_vision`

#Setup
    2.Make sure you have install python and pip
    2.Install dependencies
        3.`pip install -r requirements.txt`
        3.Install poppler eg: mac -> `brew install poppler` (https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows)
    2.Create a project on google cloud and activate api for google-vision. https://cloud.google.com/vision/docs/libraries
    2.Run
        4.`python -m src.main --pdf="{path_of_pdf_file}"`
