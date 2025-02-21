import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_community import DocAIParser
from langchain_core.document_loaders.blob_loaders import Blob


def get_langchain_docs(user_resume_path):

    GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
    DOC_PROCESSOR_NAME = os.getenv("DOC_PROCESSOR_NAME")

    parser = DocAIParser(location="us",
                     processor_name=DOC_PROCESSOR_NAME,
                     gcs_output_path="gs://{}/resume-assistant/data/output/dev/pdfs".format(GCS_BUCKET_NAME))
    inp_path = f"gs://{GCS_BUCKET_NAME}/resume-assistant/data/input/dev/pdfs/{user_resume_path}"
    blob = Blob(path=inp_path)
    docs = list(parser.lazy_parse(blob))

    return docs

