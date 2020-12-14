# Markdown Files

Repository to keep track of various .MD files

## Requirements

You will need python and pip.

```sh
pip install -r requirements.txt
```

## Usage

### Specific

Process a single file

```sh
# Build a specific file
markdown-pp <input> -o <output>

# Copy processed file to clipboard (Powershell)
markdown-pp <input> | Set-Clipboard
```

### Everything

Processes all files to the `dist` directory.

```sh
python ./process_all.py
```

> This is the recommended way since it bypasses OS encoding and uses `UTF8`.
