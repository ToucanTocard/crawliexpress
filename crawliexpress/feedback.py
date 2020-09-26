from crawliexpress.exception import CrawliexpressException

from bs4 import BeautifulSoup


class Feedback:
    datetime = None
    comment = None
    images = None

    def from_node(self, node):

        node_comment = node.find("", class_="buyer-feedback")
        if node_comment is None:
            raise CrawliexpressException("could not find feedback comment node")

        # datetime
        node_datetime = node_comment.find("", class_="r-time-new")
        if node_datetime is None:
            raise CrawliexpressException("could not find feedback datetime")
        self.datetime = node_datetime.text

        # comment
        node_comment_span = node_comment.find("span")
        if node_comment_span is None:
            raise CrawliexpressException("could not find feedback comment")
        self.comment = node_comment_span.text

        # images
        images = self.images = list()
        node_images = node.find("", class_="r-photo-list")
        if node_images is not None:
            for node_image in node_images.find_all("img"):
                images.append(node_image["src"])

    def __iter__(self):
        yield "datetime", self.datetime
        yield "comment", self.comment
        yield "images", self.images
