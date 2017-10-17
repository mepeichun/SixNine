
import pygame


def text2pixel(string, width=140, height=30):
    """
    :param string: The words that you want to display
    :param height: The height of the pixel matrix
    :param width: The width of the pixel matrix
    :return: <class 'numpy.ndarray'> with shape (width, height) and type bool
    """
    pygame.init()

    font = pygame.font.Font('msyh.ttc', 50)
    rtext = font.render(string, True, (0, 0, 0), (255, 255, 255))
    array = pygame.surfarray.array2d(pygame.transform.scale(rtext, (width, height))) > 200

    return array


def matrix2six_nine(array):
    """
    :param array: <class 'numpy.ndarray'> with shape (width, height) and type bool
    :return: string with html tag
    """
    string = ''
    shape = array.shape
    for i in range(shape[1]):
        for j in range(shape[0]):
            if array[j][i]:
                string += '6'
            else:
                string += '9'
        string += '<br />'
        string += '\n'

    return string


def generate_html(from_someone, to_someone, words, title="love"):
    """
    :param from_someone: your name as type string
    :param to_someone:  your girlfriend's/boyfriend's name
    :param words: what you want to say
    :param title: the html page title
    :return: None. But a html file will be generate
    """
    html = open('html/template.html', encoding='UTF-8').read()
    pixel_matrix = text2pixel(words, width=140, height=30)
    six_nine = matrix2six_nine(pixel_matrix)

    html = html.replace('Your_name', from_someone)
    html = html.replace('Somebody', to_someone)
    html = html.replace('Generate text and fill in here!', six_nine)
    html = html.replace('Replace title here', title)

    with open('html/main.html', 'w', encoding='utf-8') as f:
        f.write(html)
        f.close()


if __name__ == '__main__':

    # generate_html(from_someone, to_someone, words)
    generate_html("Peichun", "You", "Nice to meet you!", title="hello")
