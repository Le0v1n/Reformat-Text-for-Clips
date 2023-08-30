import re
import tkinter as tk
import pyperclip


def format_text(input_text):
    # 添加中英文之间空格、标点符号空格、数字与中文之间空格
    formatted_text = re.sub(r'(?<=[\u4e00-\u9fa5])(?=[a-zA-Z0-9])|(?<=[a-zA-Z0-9])(?=[\u4e00-\u9fa5])|(?<=[\u4e00-\u9fa5])(?=[.,;!?])|(?<=[.,;!?])(?=[\u4e00-\u9fa5])|(?<=[0-9])(?=[\u4e00-\u9fa5])|(?<=[\u4e00-\u9fa5])(?=[0-9])', ' ', input_text)

    # 删除中文与中文之间多余的空格
    formatted_text = re.sub(r'(?<=[\u4e00-\u9fa5])\s+(?=[\u4e00-\u9fa5])', '', formatted_text)
    
    # 删除中文标点后面的空格
    formatted_text = re.sub(r'([，。、（）【】])\s+', r'\1', formatted_text)
    
    # 在英文标点后添加一个空格，删除多余的空格
    formatted_text = re.sub(r'([.,;!?]+)(?=[a-zA-Z0-9])', r'\1 ', formatted_text)
    
    # 删除英文标点后多余的空格，只保留一个空格
    formatted_text = re.sub(r'([.,;!?]+)\s*', r'\1 ', formatted_text)
    
    return formatted_text

def convert_text():
    input_text = text_input.get("1.0", "end-1c")  # 获取文本框中的文本
    output_text = format_text(input_text)
    text_output.delete("1.0", "end")  # 清空输出文本框
    text_output.insert("1.0", output_text)  # 将格式化后的文本插入输出文本框

def convert_text():
    input_text = text_input.get("1.0", "end-1c")  # 获取文本框中的文本
    output_text = format_text(input_text)
    text_output.delete("1.0", "end")  # 清空输出文本框
    text_output.insert("1.0", output_text)  # 将格式化后的文本插入输出文本框

def convert_and_copy():
    input_text = text_input.get("1.0", "end-1c")  # 获取文本框中的文本
    output_text = format_text(input_text)
    pyperclip.copy(output_text)  # 复制格式化后的文本到剪贴板
    text_output.delete("1.0", "end")  # 清空输出文本框
    text_output.insert("1.0", output_text)  # 将格式化后的文本插入输出文本框

# 创建GUI窗口
window = tk.Tk()
window.title("Text Format Tool ver1.0")

# 创建作者信息标签
author_label = tk.Label(window, text="Author：Le0v1n\nContact me：zjkljd@163.com", justify="left")
author_label.pack()

# 创建文本输入框
text_input = tk.Text(window, height=20, width=80)
text_input.pack()

# 创建转换按钮
convert_button = tk.Button(window, text="    Format   ", command=convert_text)
convert_button.pack()

# 创建转换并复制按钮
copy_button = tk.Button(window, text="Format & Copy", command=convert_and_copy)
copy_button.pack()

# 创建文本输出框并插入README
text_output = tk.Text(window, height=20, width=80)
text_output.pack()

readme = "这个程序是一个文本格式化工具，它的主要功能是将输入的文本按照一定的规则进行格式化。以下是程序的主要规则总结：\n"\
         "    1. 中英文之间空格：程序会在中文字符与英文字符之间自动添加一个空格，以提高文本的可读性；\n"\
         "    2. 标点符号与中文之间空格：程序会在中文字符与标点符号之间自动添加一个空格，以提高文本排版的规范性；\n"\
         "    3. 数字与中文之间空格：程序会在数字与中文字符之间自动添加一个空格，以提高数字与中文的排版效果；\n"\
         "    4. 中文与中文之间多余的空格：程序会删除中文字符之间多余的空格，确保文本排版整洁；\n"\
         "    5. 英文标点后的空格：程序会删除英文标点符号后面的多余空格，只保留一个空格；\n"\
         "    6. 中文标点后的空格：程序会删除中文标点符号后面的空格；\n"\
         "程序将根据上述规则格式化文本并在输出框中显示结果"
text_output.insert("1.0", readme)

window.mainloop()