from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_get_information_from_github(self):
        # Tux is a newcomer to open source and github.  Zie wants to know whether
        # the github repository zie's found might be a good project to contribute
        # to, and has heard about this site.  So zie visits it.

        # Tux notices that the title page and header include the phrase "Should
        # I Contribute?"

        # Tux also notices a checklist on the page.  The checklist is not yet filled
        # out - instead of #s, there are ? marks in each spot.

        # Tux sees that the main page is prompting hir to enter the name of the
        # repository.  The first time Tux tries, zie enters the name wrong and sees
        # a message asking hir to try again.

        # The second time Tux enters the repository name correctly.  Zie sees a
        # message telling hir that the information was successfully obtained.

        # Looking at the checklist, Tux sees that the checklist's header now contains
        # the name of the repository, and that the ? marks have all been replaced
        # by numbers.

        # Tux reads down the list. Zie is confused about what the first item on the list
        # means, but sees a button labelled "Learn More".

        # Tux clicks the "Learn More" button.  A modal window pops up containing more
        # information about that item.

        # Enlightened, Tux closes the modal window.

        # Tux then clicks the "Learn More" button for the next item.

        # A different modal window corresponding to the next item pops up.  Tux
        # closes that too.

        # Tux is so excited zie decides to enter a different github repository.
        # When zie does, zie sees the new repository name in the checklist header
        # and different #s in the checklist items.

        pass
