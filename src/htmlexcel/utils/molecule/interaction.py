from .atom import Atom


class Interaction:
    """
    Describes an interaction between residues.
    """

    def get(self, interaction_line, salt=False) -> None:
        """Takes a line from the .html file and manipulates it to create a valid Atom object.

        Args:
            interaction_line (str): Follows the format of the .html file
            and contains both atom information from interaction.

        Returns:
            str: Identifier string
            obj: Interaction information
        """

        atom1, atom2 = map(lambda x: x.split(), interaction_line.split("<-->"))
        self.interaction_id = atom1.pop(0)[:-1]
        self.distance = atom2.pop()
        self.is_salt_bridge = salt

        if self.is_salt_bridge:
            self.distance += "*"

        number, name, res_name, res_num, chain = atom1
        self.atom1 = Atom(number, name, res_name, res_num, chain)
        number, name, res_name, res_num, chain = atom2
        self.atom2 = Atom(number, name, res_name, res_num, chain)

        return self

    def format(self):
        """
        Formats the interaction information for tabulation.
        """
        AMINO_ACIDS = {
            "ALA": "A",
            "ARG": "R",
            "ASN": "N",
            "ASP": "D",
            "CYS": "C",
            "GLU": "E",
            "GLN": "Q",
            "GLY": "G",
            "HIS": "H",
            "ILE": "I",
            "LEU": "L",
            "LYS": "K",
            "MET": "M",
            "PHE": "F",
            "PRO": "P",
            "SER": "S",
            "THR": "T",
            "TRP": "W",
            "TYR": "Y",
            "VAL": "V",
            "HSE": "H",
        }

        return [
            self.interaction_id,
            f"{AMINO_ACIDS[self.atom1.res_name]}{self.atom1.res_num}",
            f"{AMINO_ACIDS[self.atom2.res_name]}{self.atom2.res_num}",
            f"{self.atom1.number} {self.atom1.name}<--->{self.atom2.name} {self.atom2.number}",
            self.distance,
        ]

    def __repr__(self):
        return f"<Interaction{self.interaction_id} {self.atom1.res_name}{self.atom1.res_num}-{self.atom2.res_name}{self.atom2.res_num}>"
