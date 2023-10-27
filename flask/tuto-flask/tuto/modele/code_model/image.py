class Image:
    def __init__(self, id, name, img_filename, img_data):
        self.__id_photo = id
        self.__name = name
        self.__img_filename = img_filename
        self.__img_data = img_data

    # Getter pour id_photo
    def get_id_photo(self):
        return self.__id_photo

    # Getter pour name
    def get_name(self):
        return self.__name

    # Getter pour img_filename
    def get_img_filename(self):
        return self.__img_filename

    # Getter pour img_data
    def get_img_data(self):
        return self.__img_data
