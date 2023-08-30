from PIL import Image

# 输入图片文件名（包括文件扩展名）
input_image_file = "file_icon.png"

# 输出.ico图标文件名（包括文件扩展名）
output_ico_file = "file_icon.ico"

# 打开输入图片
image = Image.open(input_image_file)

# 将图片保存为.ico图标文件
image.save(output_ico_file, format="ICO")

print(f"已生成 {output_ico_file}")
