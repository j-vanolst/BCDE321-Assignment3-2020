from graphviz import Digraph, render

class Grapher:
    def __init__(self, classes):
        self.graph = Digraph()
        self.classes = classes
        self.labels = []

        self.graph_config()
        self.configure_labels()
        self.add_nodes()

    def graph_config(self):
        self.graph.attr('node', shape='record', fontsize='8')
        self.graph.attr('edge', dir='back', arrowtail='empty')

    def configure_labels(self):
        for aClass in self.classes:
            label_text = '{'
            label_text += f'{aClass.get_name()}|'
            for aAttribute in aClass.get_attributes():
                label_text += f'{aAttribute}\\l'
            label_text += '|'
            for aMethod in aClass.get_methods():
                label_text += f'{aMethod.get_name()}\\l'
            label_text += '}'
            self.labels.append(label_text)

    def add_nodes(self):
        for i in range(0, len(self.labels)):
            self.graph.node(f'{i}', label=self.labels[i])

    def render(self, view=True):
        if (len(self.labels) != 0):
            self.graph.render('output/output', view=view)
            render('dot', 'pdf', 'output/output')
        else:
            print('Nothing to render...')
