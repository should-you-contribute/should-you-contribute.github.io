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
        # made in the last month?" now says something like "There have been X
        # commits in the last month".
        self.assertIn("commits in the last month.",
            self.browser.find_element_by_id('checklist_commits').text)

        # The second row, which has the prompt "How many contributors are there
        # to this repository?" now says something like "There are X contributors
        # to this repository."
        self.assertIn("contributors to this repository",
            self.browser.find_element_by_id('checklist_contribs').text)

        # The third row, which has the prompt "What percentage of issues have replies?"
        # now says something like "X% of issues have replies."
        self.assertIn("issues get replies. The median number of replies ",
            self.browser.find_element_by_id('checklist_issues').text)

        # The fourth row, which has the prompt "What percentage of pull requests
        # are merged?" now says something like "X% of pull requests have been merged."
        self.assertIn("pull requests have been merged.",
            self.browser.find_element_by_id('checklist_mergedprs').text)

        # The fifth row, which has the prompt "Does the repository have a README?"
        # now says something like "The repository has a README."
        self.assertIn("The repository has a readme",
            self.browser.find_element_by_id('checklist_files').text)

        # The sixth row, which has the prompt "Does the issue tracker label issues
        # as good for newcomers?" now says something like "The tracker has issues labeled
        # X"
        self.assertIn("The tracker has issues labeled ",
            self.browser.find_element_by_id('checklist_labels').text)

        # Tux reads down the list. Zie is confused about what the first item on the list
        # means, but sees a button labelled "Learn More".
        self.assertIn("Learn More",
            self.browser.find_element_by_id('checklist_commits_prompt').text)

        # Tux clicks the "Learn More" button.  A modal window pops up containing more
        # information about that item.
        self.assertEqual(False,
            self.browser.find_element_by_id('commits-info').is_displayed())

        self.browser.find_element_by_css_selector('#padder-row > div > div:nth-child(3) > div.col-lg-6.checklist-item.checklist-description > p > button').click()
        time.sleep(1) # For some reason, we need to sleep here to get the following test to work
        self.assertEqual('false',
            self.browser.find_element_by_id('commits-info').get_attribute("aria-hidden"))

        # Enlightened, Tux closes the modal window.
        self.browser.find_element_by_css_selector('#commits-info > div > div > div.modal-header > button > span').click()
        time.sleep(1) # For some reason, we need to sleep here to get the following test to work
        self.assertEqual(False,
            self.browser.find_element_by_id('commits-info').is_displayed())

        # Tux then clicks the "Learn More" button for the next item.

        # A different modal window corresponding to the next item pops up.  Tux
        # closes that too.

        # Tux clicks on a few of the links to places in the repository on github.
        # They open in a separate window.

        # Tux clicks on the "Find one!" link.

        # Tux is so excited zie decides to enter a different github repository.
        # When zie does, zie sees the new repository name in the checklist header
        # and different #s in the checklist items.

        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main()
