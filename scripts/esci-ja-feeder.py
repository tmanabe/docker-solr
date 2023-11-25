#!/usr/bin/env python

from argparse import ArgumentParser
from pandas import read_parquet
from requests import post

argument_parser = ArgumentParser()
argument_parser.add_argument("--parquet",
                             default="/Users/owner/working/amazon-science/esci-data/shopping_queries_dataset/shopping_queries_dataset_examples.parquet")
argument_parser.add_argument("--endpoint", default="http://localhost:8983/solr/esci-ja-examples/update")
name_space = argument_parser.parse_args()

parquet = read_parquet(name_space.parquet, filters=[("product_locale", "==", "jp")])

N, buffer = parquet.shape[0] ** 0.5, []
for named_tuple in parquet.itertuples(index=False):
    d = named_tuple._asdict()
    buffer.append(d)
    if (N < len(buffer)):
        post(name_space.endpoint, json=buffer)
        buffer = []
if (0 < len(buffer)):
    post(name_space.endpoint, json=buffer)
