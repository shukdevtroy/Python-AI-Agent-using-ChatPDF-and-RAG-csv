#Now the way VectorStoreIndex works is that we're pretty much taking all our data and creating some embeddings which are
#multidimensional objects vectors and we can very quick index and query them in this database so we that by checking the
#similarity of intent and words
#we turn out data into VectorStoreIndex and we can go to that index with out query and we can very quickly retrieve the 
#specific parts of this unstructured data that we're looking for to be able to answer that question

import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file.docs.base import PDFReader


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name) # save the new created index in a folder
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


pdf_path = os.path.join("data", "Bangladesh.pdf")
bangladesh_pdf = PDFReader().load_data(file=pdf_path)
bangladesh_index = get_index(bangladesh_pdf, "bangladesh")
bangladesh_engine = bangladesh_index.as_query_engine()