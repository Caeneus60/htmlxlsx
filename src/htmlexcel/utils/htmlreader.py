from htmlexcel.utils.molecule.interaction import Interaction


class HTMLReader:
    def __init__(self, file):
        self.parse_html(file)

        self.file = open(file, "r")
        self.get_interaction_lines()
        self.file.close()

    def parse_html(self, html):
        with open(html, "r") as f:
            html_content = f.read()

        html_content = html_content.replace("&lt;", "<").replace("&gt;", ">")

        with open(html, "w") as f:
            f.write(html_content)

    def read(self, restriction):
        for line in self.file:
            if line.startswith(restriction):
                break
            if "<-->" in line:
                yield line

    def get_interaction_lines(self):
        restrictions = {
            "Hydrogen": "Non-bonded contacts",
            "Non-interacting": "Salt",
            "Salt Bridges": "Number of salt bridges",
        }

        self.hbond_lines = list(self.read(restrictions["Hydrogen"]))
        self.non_interacting_lines = list(self.read(restrictions["Non-interacting"]))
        self.salt_bridges_lines = list(self.read(restrictions["Salt Bridges"]))

    def get_interactions(self):
        hbonds = [
            Interaction().get(interaction_line) for interaction_line in self.hbond_lines
        ]
        salt_bridges = [
            Interaction().get(interaction_line, salt=True)
            for interaction_line in self.salt_bridges_lines
        ]

        return [*hbonds, *salt_bridges]
