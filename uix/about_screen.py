import webbrowser
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.utils import get_hex_from_color


class AboutScreen(Screen):
    Builder.load_file("uix/kv/about_screen.kv")

    def build(self, version, link_color):
        link_color = get_hex_from_color(link_color)
        author_site = 'https://github.com/phpusr'
        project_repo = 'https://github.com/phpusr/markdown-notebook'

        self.ids.label.text = f'''
        [size=20sp][b]Markdown Notebook[/b][/size]\n\n
        [b]Version:[/b] {version}\n
        [b]License:[/b] GNU General Public License v3.0\n\n
        [size=20sp][b]Developer[/b][/size]\n\n
        [ref={author_site}][color={link_color}]phpusr[/color][/ref]\n\n
        [b]Source code:[/b]
        [ref={project_repo}][color={link_color}]GitHub[/color][/ref]
        '''

    @staticmethod
    def open_url(instance, url):
        webbrowser.open(url)
