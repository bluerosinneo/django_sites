from django.test import TestCase
from django.urls import reverse

from .models import Site


class SiteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.site = Site.objects.create(
            title="A Title",
            description="A description",
            link="h",
        )

    def test_site_model(self):
        self.assertEqual(self.site.title, "A Title")
        self.assertEqual(self.site.description, "A description")
        self.assertEqual(self.site.link, "h")
        self.assertEqual(str(self.site), "A Title")
        self.assertEqual(self.site.get_absolute_url(), "/site/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/site/1/")
        self.assertEqual(response.status_code, 200)

    def test_site_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A description")
        self.assertTemplateUsed(response, "home.html")

    def test_site_detailview(self):
        response = self.client.get(
            reverse("site_detail", kwargs={"pk": self.site.pk})
        )
        no_response = self.client.get("/site/1999/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A Title")
        self.assertTemplateUsed(response, "site_detail.html")

    def test_site_createview(self):
        response = self.client.post(
            reverse("site_new"),
            {
                "title": "New Title",
                "description": "New description",
                "link": "h",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Site.objects.last().title, "New Title")
        self.assertEqual(Site.objects.last().description, "New description")
        self.assertEqual(Site.objects.last().link, "h")

    def test_site_updateview(self):
        response = self.client.post(
            reverse("site_edit", args="1"),
            {
                "title": "Updated Title",
                "description": "Updated description",
                "link": "h updated",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Site.objects.last().title, "Updated Title")
        self.assertEqual(Site.objects.last().description,
                         "Updated description")
        self.assertEqual(Site.objects.last().link, "h updated")

    def test_site_deleteview(self):
        response = self.client.post(
            reverse("site_delete", args="1")
        )
        self.assertEqual(response.status_code, 302)
