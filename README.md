# MLOps lab 1

`/predict` route test

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 0,
  "sepal_width": 0,
  "petal_length": 0,
  "petal_width": 0
}'
```

## Screenshots

![Docker](<assets/Screenshot 2026-10-12 at 23.34.08.png>)

![Docker_compose](<assets/Screenshot 2026-10-12 at 23.43.51.png>)
