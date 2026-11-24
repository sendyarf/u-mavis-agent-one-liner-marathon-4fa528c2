# The Sourdough Joke

Writes one original one-line comedy joke to `entry.txt`.

## Run

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. To write elsewhere, set
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-test python3 main.py
```

The program uses only the Python standard library, makes no network
requests, and is fully deterministic: every run writes the same bytes.
