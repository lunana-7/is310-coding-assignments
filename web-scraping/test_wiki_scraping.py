"""Offline regression checks; these tests make no network requests."""
import unittest
from unittest.mock import Mock, patch

from bs4 import BeautifulSoup
from wiki_scraping import WikiClient, discover_works, measure_work


class ScraperTests(unittest.TestCase):
    def test_two_galleries_and_filtering(self):
        soup = BeautifulSoup('''
        <p><span id="Miyazaki"></span></p><ul class="gallery">
        <li class="gallerytext"><a href="/wiki/Test">Test</a><a href="/wiki/Test">Duplicate</a>
        <a href="/w/index.php?action=edit">Missing</a><a href="https://other.test/wiki/X">External</a></li></ul>
        <p><span id="Takahata"></span></p><ul class="gallery">
        <li class="gallerytext"><a href="/wiki/Second">Second</a></li></ul>
        ''', 'html.parser')
        records = discover_works(soup)
        self.assertEqual([r['title'] for r in records], ['Test', 'Second'])
        self.assertEqual(records[1]['director_group'], 'Isao Takahata')

    def test_article_counts_and_subpages(self):
        soup = BeautifulSoup('''<div id="mw-content-text"><div class="mw-parser-output">
        <table><tr><td><b>Feature Film</b></td></tr></table>
        <p>A film <a href="/wiki/Test_(story)">Story</a>
        <a href="/wiki/Test_(story)">Again</a><a href="/wiki/Other">Other</a>
        <a href="/wiki/X#section">Fragment</a><a href="/w/index.php">Edit</a></p>
        <script>do not count this script</script></div></div>''', 'html.parser')
        record = measure_work({'page_url': 'https://nausicaa.net/wiki/Test'}, soup)
        self.assertEqual(record['work_type'], 'Feature Film')
        self.assertEqual(record['internal_link_count'], 3)
        self.assertEqual(record['unique_internal_link_count'], 2)
        self.assertEqual(record['linked_subpage_count'], 1)
        self.assertNotIn('script', soup.get_text())
        self.assertGreater(record['word_count'], 0)

    def test_failures_are_missing_not_zero(self):
        record = measure_work({'page_url': 'https://nausicaa.net/wiki/Test'}, None)
        self.assertEqual(record['measurement_status'], 'download_failed')
        self.assertEqual(record['word_count'], '')
        soup = BeautifulSoup('<h1>No article container</h1>', 'html.parser')
        self.assertEqual(measure_work({}, soup)['measurement_status'], 'missing_article_content')

    @patch('wiki_scraping.time.sleep')
    def test_non_200_is_not_parsed_and_request_is_delayed(self, sleep):
        client = WikiClient()
        client.robots.parse(['User-agent: *', 'Disallow: /w/'])
        client.session.get = Mock(return_value=Mock(status_code=403))
        self.assertIsNone(client.soup('https://nausicaa.net/wiki/Test'))
        self.assertEqual(client.request_log[0]['http_status'], 403)
        sleep.assert_called_once_with(2)
        with self.assertRaises(RuntimeError):
            client.download('https://nausicaa.net/w/index.php')
        self.assertEqual(client.session.get.call_count, 1)
        client.session.close()


if __name__ == '__main__':
    unittest.main()
