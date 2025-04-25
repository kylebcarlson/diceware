## Diceware Passphrase Generator

Creates strong, memorable passphrases using Python's `SystemRandom` and a word list.

## Usage

To generate a passphrase,  run:

```bash
python diceware.py
```

The script will output a 7-word passphrase, with words separated by spaces.

## How It Works

1. The script generates 7 sets of 5-digit numbers
2. Each 5-digit number corresponds to a word in the word list
3. The words are combined to create a final passphrase
