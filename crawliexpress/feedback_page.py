from crawliexpress.exception import CrawliexpressException
from crawliexpress.feedback import Feedback

from bs4 import BeautifulSoup


class FeedbackPage:
    page = None
    feedbacks = None
    has_next_page = None
    known_pages = None

    def from_html(self, html):
        soup = BeautifulSoup(html, "lxml")

        # extract feedbacks
        feedbacks = self.feedbacks = list()
        for node in soup.find_all("", class_="buyer-review"):
            feedback = Feedback()
            feedback.from_node(node)
            feedbacks.append(feedback)

        # TODO: pages
