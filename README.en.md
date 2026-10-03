# Anima Prompt Formatter

[简体中文](README.md)

This is a [Stable Diffusion Web UI Forge](https://github.com/Haoming02/sd-webui-forge-classic) extension that formats and cleans prompts before model inference for best performance.

Unlike SDXL models like IllustrousXL or NoobAI XL, [Anima is sensitive to whitespaces, commas and line breaks](https://huggingface.co/circlestone-labs/Anima/discussions/57#6997ae1d9ab163d4a7a5121e). I create this custom node so I can keep my prompting habits on NoobAI models.

I also write a ComfyUI custom nodes for this feature: [ComfyUI-AnimaPromptFormatter](https://github.com/1lch2/ComfyUI-AnimaPromptFormatter)。

## Features

- **Normalize comma spacing** — strips extra whitespace around tags and ensures consistent `tag, tag` formatting
- **Remove line breaks** — collapses multi-line prompts into a single line
- **Filter empty tags** — removes stray commas that produce empty entries
- **Optional semicolon line breaks** — converts each `;` into one newline when enabled. Consecutive semicolons produce the same number of newlines, including at the start or end of a prompt. Semicolons are preserved when disabled.

## Usage

1. Enable the **Anima Prompt Formatter** accordion in the generation UI
2. Set the Forge preset to **`anima`** (the formatter is inactive for other presets)
3. To insert line breaks with semicolons, check **Convert semicolons (;) to line breaks** inside the panel (off by default; applies to both positive and negative prompts)
4. Write your prompt as usual — the extension reformats it automatically before inference

### Example (semicolon line breaks enabled)

```
// Input
1girl, long hair,
;;
red dress,   boots,

// Formatted output
1girl, long hair

red dress, boots
```

## Note

This extension does not save the formatted prompt into the generated images. This is for better readability when loading prompts from previous generations.

## License

MIT
