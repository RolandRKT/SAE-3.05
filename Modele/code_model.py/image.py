class Image:
    def __init__(self, id, name, img_filename, img_data):
        self.id_photo = id
        self.name = name
        self.img_filename = img_filename
        self.img_data = img_data

    # Getter pour id_photo
    def get_id_photo(self):
        return self.id_photo

    # Getter pour name
    def get_name(self):
        return self.name

    # Getter pour img_filename
    def get_img_filename(self):
        return self.img_filename

    # Getter pour img_data
    def get_img_data(self):
        return self.img_data
