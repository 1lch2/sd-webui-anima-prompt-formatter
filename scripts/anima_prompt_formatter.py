import re

from modules import scripts, shared
from modules.ui_components import InputAccordion


def format_prompt(prompt: str) -> str:
    if not prompt:
        return ""
    # Step 1: Original formatting - remove newlines, clean comma spacing
    text = prompt.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ')
    tags = text.split(',')
    cleaned_tags = [tag.strip() for tag in tags]
    non_empty_tags = [tag for tag in cleaned_tags if tag]
    formatted = ', '.join(non_empty_tags)

    # Step 2: Handle BREAK - remove commas/newlines between BREAK and next tag, replace BREAK with newline
    parts = re.split(r'\s*\bBREAK\b\s*', formatted)
    result = parts[0]
    for part in parts[1:]:
        result += '\n' + part.lstrip(', ')
    return result


class AnimaPromptFormatterScript(scripts.Script):
    sorting_priority = 530

    def title(self):
        return "Anima Prompt Formatter"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with InputAccordion(value=False, label=self.title()) as enable:
            pass
        return [enable]

    def process(self, p, enable: bool):
        if not enable or shared.opts.forge_preset != "anima":
            return
        p.all_prompts = [format_prompt(prompt) for prompt in p.all_prompts]
        p.all_negative_prompts = [format_prompt(prompt) for prompt in p.all_negative_prompts]
