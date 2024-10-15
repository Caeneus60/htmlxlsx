from htmlexcel.utils.htmlreader import HTMLReader


class InteractionFile:
    def __init__(self, file_content: HTMLReader) -> None:
        self.filepath = file_content.filepath
        self.interactions = list(file_content.get_interactions())

        interaction_sample = self.interactions[0]
        self.atom1_chain = interaction_sample.atom1.chain
        self.atom2_chain = interaction_sample.atom2.chain

    def get_headings(self):
        return [
            "",
            self.atom1_chain,
            self.atom2_chain,
            "Interacting atoms",
            "Distance",
        ]
