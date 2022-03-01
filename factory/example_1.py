"""

This is an example of data serialization for song object.
Problem with this implementation could be if we wanna serialize defferent objects
like Album or Music. In this case we'd need to refactor our code to support
different serializable or serialize classes.

"""
import json
import xml.etree.ElementTree as et


class Song:
    """ Stores information about song id, title and artist """
    def __init__(self, id, title, artist):
        self.id = id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, file_format):
        """ From return serializer convert the data """
        serializer = self.get_serializer(file_format)
        return serializer(song)

    def get_serializer(self, file_format):  # CREATOR
        """ Return serializer  based on file format """
        if file_format == "JSON":
            return self.serialize_to_json
        elif file_format == "XML":
            return self.serialize_to_xml
        else:
            raise ValueError(file_format)

    # todo Implement as static method or separate function
    def serialize_to_json(self, song):  # PRODUCT
        """ Converts python object to JSON object """
        payload = {
            'id': song.id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    # todo Implement as static method or separate function
    def serialize_to_xml(self, song):  # PRODUCT
        """ Converts python object to XML object """
        element = et.Element("song", attrib={"id": song.id})
        title = et.SubElement(element, "title")
        title.text = song.title
        artist = et.SubElement(element, "artist")
        artist.text = song.artist
        return et.tostring(element, encoding="unicode")


song = Song("1", "Lithium", "Nirvana")
song_serializer = SongSerializer()
serialized_song = song_serializer.serialize(song, 'JSON')
print(serialized_song)
