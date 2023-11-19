# docker-solr

```shell
docker compose up -d

cp -r ./configsets/esci-ja-examples ./data
```

Create core from [Core Admin UI](http://localhost:8983/solr/#/~cores/).

- name: `esci-ja-examples`
- instanceDir: `esci-ja-examples`

```shell
./scripts/esci-ja-feeder.py \
    --parquet /Users/owner/working/amazon-science/esci-data/shopping_queries_dataset/shopping_queries_dataset_examples.parquet \
    --endpoint "http://localhost:8983/solr/esci-ja-examples/update"
curl "http://localhost:8983/solr/esci-ja-examples/update?commit=true"
```
