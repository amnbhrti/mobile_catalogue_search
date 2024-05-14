indexMapping = {
    "properties":{
        "SL no":{
            "type":"long"
        },
        "Product Name":{
            "type":"text"
        },
        "Product Prices":{
            "type":"long"
        },
        "Product Descriptation":{
            "type":"text"
        },
        "Product_Review":{
            "type":"text"
        },
        "NumImages":{
            "type":"long"
        },
        "Prodesc":{
            "type":"text"
        },
        "DescVec":{
            "type":"dense_vector",
            "dims": 768,
            "index":True,
            "similarity": "l2_norm"
        }

    }
}