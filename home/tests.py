import unittest
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Users, Listing
from .forms import SignUpForm


class FeaturesTests(TestCase):
    def testAllFeatures(self):
        features = {
            "gym": True,
            "parking": True,
            "wifi": True,
            "heating": True,
            "furnished": True,
            "lounge": True,
            "laundry": True,
            "pets": True,
            "AC": True,
            "business_center": True
        }
        temp = []
        if features["gym"]:
            temp.append(0)
        if features["parking"]:
            temp.append(1)
        if features["wifi"]:
            temp.append(2)
        if features["heating"]:
            temp.append(3)
        if features["furnished"]:
            temp.append(4)
        if features["lounge"]:
            temp.append(5)
        if features["laundry"]:
            temp.append(6)
        if features["pets"]:
            temp.append(7)
        if features["AC"]:
            temp.append(8)
        if features["business_center"]:
            temp.append(9)
        featureObject = Listing()
        featureObject.set_features(temp)
        self.assertEqual(featureObject.features,
                         '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')

    def testSomeFeatures(self):
        features = {
            "gym": False,
            "parking": True,
            "wifi": False,
            "heating": True,
            "furnished": False,
            "lounge": True,
            "laundry": False,
            "pets": True,
            "AC": False,
            "business_center": True
        }
        temp = []
        if features["gym"]:
            temp.append(0)
        if features["parking"]:
            temp.append(1)
        if features["wifi"]:
            temp.append(2)
        if features["heating"]:
            temp.append(3)
        if features["furnished"]:
            temp.append(4)
        if features["lounge"]:
            temp.append(5)
        if features["laundry"]:
            temp.append(6)
        if features["pets"]:
            temp.append(7)
        if features["AC"]:
            temp.append(8)
        if features["business_center"]:
            temp.append(9)
        featureObject = Listing()
        featureObject.set_features(temp)
        self.assertEqual(featureObject.features, '[1, 3, 5, 7, 9]')

    def testNoFeatures(self):
        features = {
            "gym": False,
            "parking": False,
            "wifi": False,
            "heating": False,
            "furnished": False,
            "lounge": False,
            "laundry": False,
            "pets": False,
            "AC": False,
            "business_center": False
        }
        temp = []
        if features["gym"]:
            temp.append(0)
        if features["parking"]:
            temp.append(1)
        if features["wifi"]:
            temp.append(2)
        if features["heating"]:
            temp.append(3)
        if features["furnished"]:
            temp.append(4)
        if features["lounge"]:
            temp.append(5)
        if features["laundry"]:
            temp.append(6)
        if features["pets"]:
            temp.append(7)
        if features["AC"]:
            temp.append(8)
        if features["business_center"]:
            temp.append(9)
        featureObject = Listing()
        featureObject.set_features(temp)
        self.assertEqual(featureObject.features, '[]')

    def testDefaultFeatures(self):
        featureObject = Listing()
        self.assertEqual(featureObject.features, '[]')


class SignUpFormTests(TestCase):
    def testValidSignupForm(self):
        form = SignUpForm(data={'first_name': 904158957,
                                'last_name': 'Jeffrey', 'email': 'jsg@gmail.com'})
        self.assertFalse(form.is_valid())


class ListingInfoTests(TestCase):
    def testToString(self):
        listing = Listing(address="1819 JPA", price=650, description="Yes")
        self.assertEqual(str(listing), str(listing.address) + str(" for ") +
                         str(listing.price) + str("\nDescription: ") + str(listing.description))

    def testFutureListing(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_listing = Listing(pub_date=time)
        self.assertIs(future_listing.published_recently(), False)

    def testOldListing(self):
        time = timezone.now() - datetime.timedelta(days=51)
        old_listing = Listing(pub_date=time)
        self.assertIs(old_listing.published_recently(), False)

    def testRecentListing(self):
        time = timezone.now() - datetime.timedelta(hours=49)
        recent_listing = Listing(pub_date=time)
        self.assertIs(recent_listing.published_recently(), True)

    def testAddressTrue(self):
        temp = Listing(address="123 Conch Lane")
        self.assertEqual(temp.address, "123 Conch Lane")

    def testAddressFalse(self):
        temp = Listing(address="123 Bonch Bane")
        self.assertNotEqual(temp.address, "123 Conch Lane")

    def testDescTrue(self):
        temp = Listing(description="This place is so cool bro I'd live here")
        self.assertEqual(temp.description,
                         "This place is so cool bro I'd live here")

    def testDescFalse(self):
        temp = Listing(description="This place is so cool bro I'd live here")
        self.assertNotEqual(
            temp.description, "This place is not so cool bro I'd rather die than live here")

    def testBedsTrue(self):
        temp = Listing(beds=2)
        self.assertEqual(temp.beds, 2)

    def testBedsFalse(self):
        temp = Listing(beds=3)
        self.assertNotEqual(temp.beds, 2)

    def testPriceTrue(self):
        temp = Listing(price=69)
        self.assertEqual(temp.price, 69)

    def testPriceFalse(self):
        temp = Listing(price=420)
        self.assertNotEqual(temp.price, 69)


class ListingReviewTests(TestCase):
    def testRatingsDefault(self):
        temp = Listing()
        self.assertEqual(temp.ratings, 0)

    def testRatingsTrue(self):
        temp = Listing(ratings=5)
        self.assertEqual(temp.ratings, 5)

    def testRatingsFalse(self):
        temp = Listing(ratings=3)
        self.assertNotEqual(temp.ratings, 5)

    def testNumRatingsDefault(self):
        temp = Listing()
        self.assertEqual(temp.number_of_ratings, 0)

    def testNumRatingsTrue(self):
        temp = Listing(number_of_ratings=20)
        self.assertEqual(temp.number_of_ratings, 20)

    def testNumRatingsFalse(self):
        temp = Listing(number_of_ratings=60)
        self.assertNotEqual(temp.number_of_ratings, 20)
