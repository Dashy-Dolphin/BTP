Following packages are dependencies: Grobid,lxml,selenium, beautifulsoup

The Directory Structure is as follows:
        DataExtraction
            ResearchPapers
            WikiArticles
        RAG


The DataExtraction contains the code used to download and clean the relevant Datasets.

    ResearchPapers

        pdfdownloader.ipynb 
        contains the selenium code to launch a controlled chromium engine. Then, using the GUI for the browser we can authorize
        the sesion to access the papers.
        Then , the latter part of the script contains the code to download all the recent research papers.

        XMLtotext.ipynb
        Using the grobid , we can convert the PDF files into XML format. Then this script parses the XML files to chunk them paragraph wise.


    WikiArticles
        CategroyTreeparser.ipynb
        The CategroyTreeparser recursively parses the links tree for a particular category and emits all the links.

        HTMLtoChunks.ipynb
        This scripts downloads the relevant HTML files and chunks them paragraph wise.



RAG

ChunkingpipelineDisk.ipynb
This contains the chunking and retrieval parts of the RAG and writes the retieved context for each query in a file.

Replicate.py
Due to lack of compute capacity of local system, we have used Replicate API for LLama based chatbot for generation purpose.


