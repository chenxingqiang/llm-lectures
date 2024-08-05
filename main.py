import os
from ppt_gen import MarkdownReader
from ppt_gen import PPTTemplateReader
from ppt_gen import DetailedPPTGenerator

template_path = "template.pptx"

# markdown_paths = [
#     "PPT1.md",
#     "PPT2.md",
#     "PPT3.md",
#     "PPT4.md",
#     "PPT5.md",
#     "PPT6.md",
#     "PPT7.md",
#     "PPT8.md",
#     "PPT9.md",
#     "PPT10.md",
# ]
markdown_paths = ["llm-leture/" + str(i) + ".md" for i in range(1,326)]

output_dir = "llm-PPT"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

for markdown_path in markdown_paths:
    template_reader = PPTTemplateReader(template_path)
    markdown_reader = MarkdownReader(markdown_path)
    ppt_generator = DetailedPPTGenerator(template_reader, markdown_reader, output_dir)
    ppt_generator.generate_ppt()