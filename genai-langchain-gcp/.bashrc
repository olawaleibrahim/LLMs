gsutil -m cp -R ./data gs://langchain-book-test-bucket/

apt-get update && apt-get install libmagic-dev
pip install unstructured==0.15.9 unstructured[pdf]==0.15.9  opencv-python==4.9.0.80