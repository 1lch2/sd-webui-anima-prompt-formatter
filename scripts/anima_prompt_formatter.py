import gradio as gr

from modules import scripts, shared
from modules.ui_components import InputAccordion


def format_prompt(prompt: str, semicolon_newlines: bool = False) -> str:
    if not prompt:
        return ""
    # Remove original newlines before inserting any requested line breaks.
    text = prompt.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ')
    parts = text.split(';') if semicolon_newlines else [text]
    formatted_parts = []
    for part in parts:
        tags = [tag.strip() for tag in part.split(',')]
        formatted_parts.append(', '.join(tag for tag in tags if tag))
    return '\n'.join(formatted_parts)


class AnimaPromptFormatterScript(scripts.Script):
    sorting_priority = 530

    def title(self):
        return "Anima Prompt Formatter"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with InputAccordion(value=False, label=self.title()) as enable:
            semicolon_newlines = gr.Checkbox(
                value=False,
                label="Convert semicolons (;) to line breaks",
            )
        return [enable, semicolon_newlines]

    def process(self, p, enable: bool, semicolon_newlines: bool = False):
        if not enable or shared.opts.forge_preset != "anima":
            p._anima_formatter_enabled = False
            return
        p._anima_formatter_enabled = True
        p._anima_formatter_semicolon_newlines = semicolon_newlines

    def process_batch(self, p, *args, **kwargs):
        if not getattr(p, '_anima_formatter_enabled', False):
            return
        semicolon_newlines = p._anima_formatter_semicolon_newlines
        p.prompts = [format_prompt(prompt, semicolon_newlines) for prompt in p.prompts]
        p.negative_prompts = [format_prompt(prompt, semicolon_newlines) for prompt in p.negative_prompts]
