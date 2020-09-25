from crawliexpress.exception import CrawliexpressException

from bs4 import BeautifulSoup


class Feedback:
    comment = None
    datetime = None
    images = None

    def from_node(self, node):

        # comment
        node_comment = node.find("", class_="buyer-feedback")
        if node_comment is None:
            raise CrawliexpressException("could not find feedback comment node")

        node_datetime = node_comment.find("", class_="r-time-new")
        if node_datetime is None:
            raise CrawliexpressException("could not find feedback datetime")
        self.datetime = node_datetime.text

        node_comment_span = node_comment.find("span")
        if node_comment_span is None:
            raise CrawliexpressException("could not find feedback comment")
        self.comment = node_comment_span.text

        print(f"{self.datetime}: {self.comment}\n")
