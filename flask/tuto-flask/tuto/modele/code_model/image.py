class Image:
    def __init__(self, id, name, img_filename, img_data):
        """
        Initialise un objet Image avec les informations de l'image.

        Args:
            id (int): L'ID de l'image.
            name (str): Le nom de l'image.
            img_filename (str): Le nom de fichier de l'image.
            img_data (bytes): Les données de l'image au format binaire.
        """
        self.__id_photo = id
        self.__name = name
        self.__img_filename = img_filename
        self.__img_data = img_data

    def get_id_photo(self):
        """
        Getter pour l'ID de l'image.

        Returns:
            int: L'ID de l'image.
        """
        return self.__id_photo

    def get_name(self):
        """
        Getter pour le nom de l'image.

        Returns:
            str: Le nom de l'image.
        """
        return self.__name

    def get_img_filename(self):
        """
        Getter pour le nom de fichier de l'image.

        Returns:
            str: Le nom de fichier de l'image.
        """
        return self.__img_filename

    def get_img_data(self):
        """
        Getter pour les données de l'image au format binaire.

        Returns:
            bytes: Les données de l'image.
        """
        return self.__img_data
