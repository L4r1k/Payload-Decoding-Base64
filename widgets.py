import ipywidgets as widgets
from ipywidgets import interactive, Layout
from IPython.display import display
import base64

class base64_decoder(object):
    def __init__(self, encoded_string):
        self.encoded_string = encoded_string
        self.decoded_string = self.decode_string()

    def decode_string(self):
        xorBytes = bytearray()
        base64String = base64.b64decode(self.encoded_string)
        stringBytes = bytearray(base64String)
        for byte in stringBytes:
            xorBytes.append(byte ^ 35)
        return xorBytes

class NotebookWidgets(object):
    def __init__(self):
        self.encoded_string = None
        self.dc = None

    def initialize_decoder(self):
        self.dc = base64_decoder(self.encoded_string)

    def decode_args(self, encoded_string):
        self.encoded_string = encoded_string

nbw = NotebookWidgets()
layout = Layout(width='80%')
style = {'description_width': 'initial'}

string_panel = interactive(
    nbw.decode_args,
    encoded_string=widgets.Text(
        value=nbw.encoded_string,
        description='Encoded String',
        disabled=False,
        layout=layout,
        style=style))

decode_button = widgets.Button(
        description='Decode',
        disabled=False,
        button_style='',
        style=style,
        layout=layout)

def decode_string(click):
    decode_button.description = 'Decoded'
    decode_button.button_style = 'success'
    decode_button.disabled = True

    nbw.initialize_decoder()
    display(nbw.dc.decoded_string)

decode_button.on_click(decode_string)

display(string_panel)
display(decode_button)
