class Button(object):
    html = ''

    def get_html(self):
        return self.html    # Why it will read the html ??


class Image(Button):
    html = '<img></img>'


class Input(Button):
    html = '<input></input>'


class Flash(Button):
    html = '<obj></obj>'


def Video():
    html = '<video></video>'


class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()


button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print(button_obj.create_button(b).get_html())
