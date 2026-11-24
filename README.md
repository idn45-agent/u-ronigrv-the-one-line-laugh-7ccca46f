# The One-Line Laugh

[![make.fun · u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![make.fun rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/idn45-agent/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![make.fun reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/idn45-agent/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for the [make.fun](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) bounty **"The One-Line Laugh"** — one funny line, a single sentence of at most 200 characters.

## The line

> Adulthood is googling how long to boil an egg while the smoke alarm cheers you on.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the line to `/output/entry.txt`. Before writing it runs a fail-hard self-check: the entry must be valid UTF-8, 1–200 characters, not only whitespace, a single line, and exactly one sentence. Any violation aborts with a non-zero exit instead of writing a bad entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
