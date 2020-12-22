# PDF to text using Google Vision

###How to use?

    1.`git clone https://github.com/digvijaygunjal/pdf_to_text_google_vision.git`
    1.`cd pdf_to_text_google_vision`

1.Make sure you have install python and pip
1.Install dependencies
    1.`pip install -r requirements.txt`
    1.Install poppler eg: mac -> `brew install poppler` (https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows)
1.Create a project on google cloud and activate api for google-vision. https://cloud.google.com/vision/docs/libraries
1.Run
    - `python -m src.main --pdf="{path_of_pdf_file}"`
