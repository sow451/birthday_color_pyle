# Birthday Color

A tiny Streamlit app that turns a birth date into a deterministic 6-digit hex color and displays it as a swatch.

## How It Works

1. Accepts a date input (minimum 1900-01-01).
2. Formats the date as `DDmYYYY` when the month is a single digit, otherwise `DDMMYYYY`.
3. Converts the string to an integer.
4. If the value exceeds `0xFFFFFF` (16,777,215), it applies a modulo to fit the 6-digit hex range.
5. Converts the result to a 6-character hex code and renders the color.

## Run Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Project Files

- `app.py` — Streamlit app.
- `requirements.txt` — Dependencies.
- `notes_about_birthday_color` — Background notes on hex and the idea.

## Ideas / Next Steps

- Add a friendly color name lookup (currently commented out in `app.py`).
- Consider using `DDMMYYYY` for all dates for a consistent 8-digit input.
- Add tests for the date-to-hex conversion.
