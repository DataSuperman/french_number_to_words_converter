# French Number to Words Converter

This project is a Python application that converts numeric values into their French word equivalents.

## Getting the code

```bash
git clone https://github.com/DataSuperman/french_number_to_words_converter
cd french_number_to_words_converter
make
```

## Running using cli

On linux/macos you can run locally using: 
```bash
make .venv
./.venv/bin/python3 main.py 10 20 30
```

### Sample output

```
10 -> dix
20 -> vingt
30 -> trente
```

## Running using API server

Create your virtual environment and start the server:
```bash
make start_server # this will start the uvicorn server on port 8000
```

Output will be like this:
```
INFO:     Will watch for changes in these directories: ['**your_local_path**/french_number_to_words_converter']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1022200] using WatchFiles
INFO:     Started server process [1022202]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Send the request to the server using curl:
```bash
curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"numbers": [17, 21, 100, 2000, 999999]}' \
    "http://127.0.0.1:8000/convert/"
```

Or you can send the request to the server using a sample script:
```bash
./.venv/bin/python3 get_from_api.py
```

### Sample output

```
{'numbers': [17, 21, 100, 2000, 999999], 'french_numbers': ['dix-sept', 'vingt-et-un', 'cent', 'deux-mille', 'neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf']}
```
