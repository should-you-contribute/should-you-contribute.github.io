from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_get_information_from_github(self):
        # Tux is a newcomer to open source and github.  Zie wants to know whether
        # the github repository zie's found might be a good project to contribute
        # to, and has heard about this site.  So zie visits it.
        self.browser.get("http://127.0.0.1:8000/index.html")

        # Tux notices that the title page and header include the phrase "Should
        # I Contribute?"
        project_name = "Should I Contribute?"
        self.assertIn(project_name, self.browser.title)
        self.assertEquals(project_name.upper(),
            self.browser.find_element_by_id('project_name').text)

        # Tux also notices a checklist on the page.  The checklist is not yet filled
        # out - instead of #s, there are ? marks in each spot.
        self.assertEquals(self.browser.find_element_by_id('checklist_title').text,
            "CHECKLIST")
        self.assertEquals(6,
            len(self.browser.find_elements_by_class_name('fa-question-circle')))

        # Tux sees that the main page is prompting hir to enter the name of the
        # repository.
        self.assertTrue(self.browser.find_element_by_id('repo_name'))

        # The first time Tux tries, zie enters the name wrong and sees
        # a message asking hir to try again.
        repo_input_box = self.browser.find_element_by_id('repo_name')
        repo_input_box.send_keys('shaunagm/terrible-idea-for-a-repo-name')
        # self.browser.implicitly_wait(6)
        repo_input_box.send_keys(Keys.ENTER)
        time.sleep(2) # For some reason, webdriver's explicit waiting *or* implicit waiting not working
        self.assertIn("That is not a valid, public Github repository.",
            self.browser.find_element_by_id('repo_error').text)

        # The second time Tux enters the repository name correctly.  Zie sees a
        # message telling hir that the information was successfully obtained.
        repo_input_box.clear()
        working_repo = "shaunagm/WelcomeBot"
        repo_input_box.send_keys(working_repo)
        # self.browser.implicitly_wait(6)
        repo_input_box.send_keys(Keys.ENTER)
        time.sleep(2) # For some reason, webdriver's explicit waiting *or* implicit waiting not working
        self.assertIn("Success!",
            self.browser.find_element_by_id('repo_error').text)

        # Looking at the checklist, Tux sees that the checklist's header now contains
        # the name of the repository.
        self.assertIn(working_repo.upper(),
            self.browser.find_element_by_id('checklist_title').text)

        # Tux also sees that the ? marks have all been replaced by numbers.
        # In the first row, which has the prompt "How many commits have been
        # made in the last week?" now says something like "There have been X
        # commits in the last week".

        # The second row, which has the prompt "How many contributors are there
        # to this repository?" now says something like "There are X contributors
        # to this repository."
        self.assertIn("contributors to this repository",
            self.browser.find_element_by_id('checklist_contribs').text)

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

        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main()
