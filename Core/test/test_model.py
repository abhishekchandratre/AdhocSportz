from django.test import TestCase
from Core.models import Location, Sports, UserInfo, SportsType


class LocationTest(TestCase):
    def createLocation(self, country="India", state="MH", region="Pune"):
        return Location.objects.create(country=country, state=state, region=region)

    def test_location_creation(self):
        location = self.createLocation()
        self.assertTrue(isinstance(location, Location))
        self.assertEqual(location.__str__(), location.country + ', ' + location.state + ', ' + location.region)


class SportsTest(TestCase):
    def createSport(self):
        sportType = SportsType.objects.create(categoryName="outdoor")
        return Sports.objects.create(sportName="football",sportType=sportType)

    def test_sport_creation(self):
        sport = self.createSport()
        self.assertTrue(isinstance(sport, Sports))
        self.assertEqual(sport.__str__(), "football")


class SportsTypeTest(TestCase):
    def createSportType(self):
        return SportsType.objects.create(categoryName="outdoor")

    def test_sporttype_creation(self):
        sportsType = self.createSportType()
        self.assertTrue(isinstance(sportsType, SportsType))
        self.assertEqual(sportsType.__str__(), "outdoor")