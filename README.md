# Anima Prompt Formatter

A Stable Diffusion WebUI Forge extension that formats and cleans prompts before model inference.

## Features

- **Normalize comma spacing** — strips extra whitespace around tags and ensures consistent `tag, tag` formatting
- **Remove line breaks** — collapses multi-line prompts into a single line
- **Filter empty tags** — removes stray commas that produce empty entries
- **BREAK handling** — converts the `BREAK` keyword into a proper newline separator (as expected by the model for attention block boundaries)

## Usage

1. Enable the **Anima Prompt Formatter** accordion in the generation UI
2. Set the Forge preset to **`anima`** (the formatter is inactive for other presets)
3. Write your prompt as usual — the extension reformats it automatically before inference

### Example

```
// Input
1girl, long hair,
BREAK
red dress,   boots,

// Formatted output
1girl, long hair
red dress, boots
```

## Requirements

- [Stable Diffusion WebUI Forge Classic](https://github.com/lllyasviel/stable-diffusion-webui-forge)
- Forge preset set to `anima`

## License

MIT
