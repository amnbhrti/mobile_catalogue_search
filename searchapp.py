import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "all_phones"

try:
    es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic","OHepg_t_GvCiz3LGURxB"),
    )
except ConnectionError as e:
    print("Connection Error:", e)

#CHECK ELASTIC SEARCH IF ON

if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")

##DEFINING SEARCH

def search(input_kw):
    model = SentenceTransformer("C:/Users/amnbh/Downloads/all-mpnet-base-v2")
    vec_of_kw = model.encode(input_kw)

    query = {
        "field": "DescVec",
        "query_vector": vec_of_kw,
        "k": 2,
        "num_candidates": 400
    }
    res = es.knn_search(index="all_phones", knn=query , source=["Product_Name","Product Descriptation"])
    results = res["hits"]["hits"]

    return results

#DEFINITION OF MAIN FUNC

def main():
    st.title("Search Phone Catalogue")

    #input
    search_query = st.text_input("Enter search query")

    #buttons
    if st.button("Search"):
        if search_query:
            results = search(search_query)

            st.subheader("Results")
            for result in results:
                with st.container():
                    if "_source" in result:
                        try:
                            st.header(f"{result['_source']['Product_Name']}")
                        except Exception as e:
                            print(e)
                        
                        try:
                            st.write(f"Description: {result['_source']['Product Descriptation']}")
                        except Exception as e:
                            print(e)
                        st.divider()

                    
if __name__ == "__main__":
    main()
