# Anima 提示词格式化器

[English README](README.en.md)

这是一个 [Stable Diffusion Web UI Forge](https://github.com/Haoming02/sd-webui-forge-classic) 扩展，用于在模型推理前格式化提示词以保证最佳效果。

和之前的IllustriousXL，NoobAI XL这些SDXL模型不同，[Anima 模型对空格、逗号和换行符特别敏感](https://huggingface.co/circlestone-labs/Anima/discussions/57#6997ae1d9ab163d4a7a5121e)。我是为了在 NoobAI 模型上保留自己习惯的提示词写法才弄了这么个插件。

我同样做了一个 ComfyUI 上的插件：[ComfyUI-AnimaPromptFormatter](https://github.com/1lch2/ComfyUI-AnimaPromptFormatter)。

## 功能

- **标准化逗号间距** — 去除标签周围的额外空白，并确保一致的 `tag, tag` 格式
- **移除换行符** — 将多行提示词合并为单行
- **过滤空标签** — 删除会产生空条目的多余逗号
- **可选的分号换行** — 开启后，每个英文分号 `;` 转换为一个换行符；连续多个分号产生相同数量的换行，首尾分号也会保留对应换行。关闭时保留分号。
- **保留 BREAK** — 插件不再将 `BREAK` 关键字转换为换行符。

## 使用方法

1. 在生成界面中启用 **Anima Prompt Formatter** 折叠面板
2. 将 Forge 预设设置为 **`anima`**（其他预设下格式化器不生效）
3. 如需通过分号插入换行，勾选面板内的 **Convert semicolons (;) to line breaks**（默认关闭，对正向和负向提示词均生效）
4. 像往常一样编写提示词 — 扩展会在推理前自动重新格式化

### 示例（开启分号换行）

```
// 输入
1girl, long hair,
;;
red dress,   boots,

// 格式化后输出
1girl, long hair

red dress, boots
```

## 注意事项

这个插件不会把格式化后的提示词保存到生成的图片中。这是为了在从以前的图中读提示词时候保证可读性。

## 许可证

MIT
