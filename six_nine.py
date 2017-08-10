import pygame

pygame.init()

text = "xx, I love you!"
font = pygame.font.Font('msyh.ttc', 50)
rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))
array = pygame.surfarray.array2d(pygame.transform.scale(rtext, (140, 20)))

red = array > 200

content = ''
shape = red.shape
print(shape)
for i in range(shape[1]):
    for j in range(shape[0]):
        if red[j][i]:
            content += '6'
        else:
            content += '9'
    content += '<br />'
    content += '\n'

content += u'\n \n <font size="5">请按下Ctrl + F键，输入数字：6，然后按下回车键！</font>'

with open('test.html', 'w', encoding='utf-8') as f:
    html_tag_begin = '''
    <!doctype html><html>
    <head>
    <meta charset="utf-8">
    <title>test</title>
    </head>
    <body>
    '''
    html_tag_end = '</body>\n</html>'
    f.write(html_tag_begin + content + html_tag_end)
    f.close()
