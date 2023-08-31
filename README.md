# :rocket:Updated
- [x] 已加入新字体 [ver 1.0 -> ver 1.1]☘️
- [x] 窗口初始化时实现自适应分辨率 [ver 1.0 -> ver 1.1]☘️
- [x] 修复 `阿拉伯数字.阿拉伯数字` 会添加空格的 bug [ver 1.0 -> ver 1.1]☘️
- [x] 修复正则表达式会删除换行符的行为 [ver 1.0 -> ver 1.1]☘️
- [x] 删除转换按钮，仅保留转换并复制到粘贴板 [ver 1.0 -> ver 1.1]☘️
- [x] 补充中文标点符号 [ver 1.0 -> ver 1.1]☘️
- [x] `README.md` 文件增加规则说明 [ver 1.0 -> ver 1.1]☘️
- [x] 新增 `create_icon.py`，可以使用该脚本生成自己的 `.icon` 文件 [ver 1.0 -> ver 1.1]☘️
- [x] 新增 `create_exe_file.sh`，可以使用该脚本生成快速生成 `.ext` 文件 [ver 1.0 -> ver 1.1]☘️
- [x] 新增 `requirements.txt`，可以快速安装所需第三方库 -> `pip install -r requirements.txt` [ver 1.0 -> ver 1.1]☘️
- [x] 新增 Apache License [ver 1.0 -> ver 1.1]☘️
- [x] 发布 `reformat-text-for-clips-ver-1.1.exe`版本

# 😒TODO
- [x] 修改字体，为中文和英文应用不同的字体
- [ ] 尝试加入 Markdown 插件，使其可以显示 Markdown 语法

# :b:Bugs
- [x] `数字.数字`的形式会在 `.` 后面加空格，如：`4.1 -> 4. 1` [ver 1.0 -> ver 1.1]
- [x] 如果有两行，会把换行符删除 [ver 1.0 -> ver 1.1]
- [ ] 使用 \`\` 包围的代码中如果出现 `.字母`，会在 `.` 后添加空格

# 🥰Introduction

"This program is designed to assist you in reformatting raw text. Alternatively, you can review the original code and generate a new `.exe` file on your own using the following Bash command:

```bash
pyinstaller --onefile --noconsole --icon file_icon.ico --name reformat-text-for-clips-ver-1.1 reformat-text-for-clips.py
```

---

这个程序旨在帮助您重新格式化原始文本。你也可以查看原始代码并使用以下 Bash 命令自行生成一个新的`. exe`文件：

```bash
pyinstaller --onefile --noconsole --icon file_icon.ico --name reformat-text-for-clips-ver-1.1 reformat-text-for-clips.py
```

# :abc:Rules

Here are explanations for the text formatting rules:

1. **Space Between Chinese and English Characters**:
   - Automatically add a space between Chinese characters and English characters to improve text readability. For example, format "你好world" as "你好 world".
2. **Space Between Punctuation and Chinese Characters**:
   - Automatically add a space between Chinese characters and punctuation marks to improve text layout consistency. For example, format "你好，世界！" as "你好， 世界！".
3. **Space Between Numbers and Chinese Characters**:
   - Automatically add a space between numbers and Chinese characters to enhance the formatting of numbers with Chinese text. For example, format "100元" as "100 元".
4. **Remove Extra Spaces Between Chinese Characters**:
   - Remove extra spaces between Chinese characters to maintain text compactness. For example, format "你  好" as "你好".
5. **Remove Spaces After Chinese Punctuation**:
   - Remove spaces after Chinese punctuation marks while preserving spaces after English punctuation marks. For example, format "你好 ， 世界！" as "你好， 世界！".
6. **Add a Space After English Punctuation**:
   - Add a space after English punctuation marks to improve text layout. However, exclude periods before and after Arabic numerals. For example, format "Hello,world!" as "Hello, world!", but leave "3.14" unchanged.
7. **Remove Extra Spaces After English Punctuation**:
   - Remove extra spaces after English punctuation marks, leaving only one space. For example, format "Hello ,  world ! " as "Hello, world!".
8. **Remove Extra Spaces**:
   - Remove extra spaces, for example, change "1.   1" to "1.1".
9. **Fix Periods After Arabic Numerals**:
   - Fix periods after Arabic numerals to ensure there is a space between numbers and periods. For example, format "1 . 2" as "1.2".

---

以下是文本格式化规则的说明：

1. **中英文之间空格**：
   - 在中文字符和英文字符之间自动添加一个空格，以提高文本的可读性。例如，将"你好world"格式化为"你好 world"。
2. **标点符号与中文之间空格**：
   - 在中文字符与标点符号之间自动添加一个空格，以提高文本排版的规范性。例如，将"你好，世界！"格式化为"你好， 世界！"。
3. **数字与中文之间空格**：
   - 在数字与中文字符之间自动添加一个空格，以提高数字与中文的排版效果。例如，将"100元"格式化为"100 元"。
4. **删除中文与中文之间多余的空格**：
   - 删除中文字符与中文字符之间多余的空格，以保持文本的紧凑性。例如，将"你  好"格式化为"你好"。
5. **删除中文标点后面的空格**：
   - 删除中文标点符号后面的空格，但保留英文标点符号后的空格。例如，将"你好 ， 世界！"格式化为"你好， 世界！"。
6. **在英文标点后添加一个空格**：
   - 在英文标点符号后添加一个空格，以改善文本排版。但会排除阿拉伯数字前后的句点。例如，将"Hello,world!"格式化为"Hello, world!"，但不会改变"3.14"。
7. **删除英文标点后多余的空格**：
   - 删除英文标点符号后多余的空格，只保留一个空格。例如，将"Hello ,  world ! "格式化为"Hello, world!"。
8. **去除多余的空格**：
   - 去除多余的空格，例如将"1.   1"改为"1.1"。
9. **修复阿拉伯数字后的句点**：
   - 修复阿拉伯数字后的句点，确保数字和句点之间有一个空格。例如，将"1 . 2"修复为"1.2"。

# :warning:Note

+ If your screen resolution is greater than 1920x1080, you may encounter low text resolution issues when using this software. In such cases, you need to right-click the `reformat-text-for-clips.exe` file -> Properties -> Compatibility -> Change high DPI settings -> Check 'Override high DPI scaling behavior (Application)'.
+ 360 Security Guard may trigger a false positive. You can add it to the trusted list. If you're still concerned, you can inspect the code or generate the `.exe` program yourself.

---

+ 如果你的屏幕大于 1920×1080，那么在使用本软件时可能会出现文字分辨率低的问题。此时你需要右键 `.exe` 文件 -> 属性 -> 兼容性 -> 更改高 DPI 设置 -> 勾选替代高 DPI 缩放行为（应用程序）；
+ 360 安全卫士可能会报毒，添加信任即可。如果不放心，可自行检查代码或自行生成 `.exe` 程序。


# :e-mail:Contact me

Welcome to contact me if there are any bugs.

+ [联系我](mailto:zjkljd@163.com)
+ [Contact me](mailto:zjkljd@163.com)
