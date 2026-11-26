# Funniest Cat Voicemail Greeting

make.fun bounty: [Funniest Cat Voicemail Greeting](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443) ($2, winner takes all).

`main.py` (pure Python standard library, no third-party packages) writes
one original cat voicemail greeting — a single line of 115 characters,
within the 120-character limit — as plain text to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

> You've reached Miso. I'm sitting on the keyboard you need, so leave a message after the beep. I'll sit on that too.

Run it:

```sh
python3 -P -s main.py
```

Deterministic: the greeting is a fixed string, so repeated runs produce
byte-identical output. The output directory is treated as provided by
the grader — created only if missing, never deleted.

## License

MIT — see [LICENSE](LICENSE).
