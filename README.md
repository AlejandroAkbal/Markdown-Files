# Markdown Files

Repository to keep track of various .MD files

## Requirements

You will need python and pip.

```sh
pip install -r requirements.txt
```

## Usage

```sh
# Build a file
markdown-pp <input> -o <output> -e latexrender, includeurl, youtubeembed

# Watch files
markdown-pp -w -e latexrender, includeurl, youtubeembed

# Copy processed file to clipboard (Powershell)
... | Set-Clipboard
```
