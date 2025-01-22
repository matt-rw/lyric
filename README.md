## Lyrics

## Installation

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

Run from the command line with the artist name and song title.

### Example

```bash
$ python3 find.py "Creedence Clearwater Revival" "Green River" | less
```

```bash
$ python3 find.py -t -f "Townes Van Zandt" "Pancho and Lefty"
Saved lyrics to 'townesvanzandt-panchoandlefty.txt'
$ head townesvanzandt-panchoandlefty.txt
Pancho and Lefty - Townes Van Zandt

Living on the road my friend
Is gonna keep you free and clean
Now you wear your skin like iron
And your breath as hard as kerosene
You weren't your mama's only boy
But her favorite one it seems
She began to cry when you said goodbye
```
