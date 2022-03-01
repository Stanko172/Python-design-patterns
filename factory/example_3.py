"""

Here we implemented object factory so thst we can add defferent formats
with no problems or confusion

"""
import json
import xml.etree.ElementTree as et


class Song:
    """ Stores information about song id, title and artist and runs given serializer """
    def __init__(self, id, title, artist):
        self.id = id
        self.title = title
        self.artist = artist

    def serialize(self, serializer):
        serializer.start_object("id", self.id)
        serializer.add_property("title", self.title)
        serializer.add_property("artist", self.artist)

class JsonSerializer:
    def __init__(self):
        self.current_object = None

    def start_object(self, name, id):
        self.current_object[name] = id

    def add_property(self, name, property):
        self.current_object[name] = property

    def to_str(self):
        return json.dumps(self.current_object)


class XmlSerializer:
    def __init__(self):
        self.current_element = None

    def start_object(self, name, id):
        self.current_element = et.Element(name, attrib={"id": id})

    def add_property(self, name, property):
        prop = et.SubElement(self.current_element, name)
        prop.text = property

    def to_str(self):
        return et.tostring(self.current_element, encoding="unicode")

class SerializerFactory:
    def __init__(self):
        self.creators = {}

    def register_format(self, format, creator):
        self.creators[format] = creator

    def get_serializer(self, format):
        creator = self.creators[format]
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)


class ObjectSerializer:
    def serialize(self, serializable, file_format):
        """ From return serializer convert the data """
        serializer = factory.get_serializer(file_format)
        serializable.serialize(serializer)
        return serializer.to_str()


factory.register_format('XML', XmlSerializer)

song = Song("1", "Smells like teen spirit", "Nirvana")
object_serializer = ObjectSerializer()
serialized_object = object_serializer.serialize(song, "XML",)
print(serialized_object)