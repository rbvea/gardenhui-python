from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from neighborhood.models import Neighborhood


class NeighborhoodTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')

    def tearDown(self):
        self.user.delete()

    def test_list(self):
        response = self.client.get(reverse('neighborhood-list'))
        self.failUnlessEqual(response.status_code, 200)

    def test_crud(self):
        # Create new instance
        response = self.client.post(reverse('neighborhood-list'), {})
        self.assertContains(response, '"success": true')

        # Read instance
        items = Neighborhood.objects.all()
        self.failUnlessEqual(items.count(), 1)
        item = items[0]
        response = self.client.get(reverse('neighborhood-details', kwargs={'id': item.id}))
        self.failUnlessEqual(response.status_code, 200)

        # Update instance
        response = self.client.post(reverse('neighborhood-details', kwargs={'id': item.id}), {})
        self.assertContains(response, '"success": true')

        # Delete instance
        response = self.client.post(reverse('neighborhood-delete', kwargs={'id': item.id}), {})
        self.assertContains(response, '"success": true')
        items = Neighborhood.objects.all()
        self.failUnlessEqual(items.count(), 0)

