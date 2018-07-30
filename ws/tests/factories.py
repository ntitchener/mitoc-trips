from factory import SubFactory, Sequence
from factory.django import DjangoModelFactory

from ws import models


class EmergencyContactFactory(DjangoModelFactory):
    class Meta:
        model = models.EmergencyContact

    name = "My Mother"
    cell_phone = "781-555-0342"
    relationship = "Mother"
    email = "mum@example.com"


class EmergencyInfoFactory(DjangoModelFactory):
    class Meta:
        model = models.EmergencyInfo

    emergency_contact = SubFactory(EmergencyContactFactory)
    allergies = "None"
    medications = "None"
    medical_history = "None"


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    username = Sequence(lambda n: f"participant{n + 1}")
    email = Sequence(lambda n: f"participant{n + 1}@example.com")


class ParticipantFactory(DjangoModelFactory):
    class Meta:
        model = models.Participant

    user_id = Sequence(lambda n: n + 1)
    email = Sequence(lambda n: f"participant{n + 1}@example.com")
    name = "Test Participant"
    emergency_info = SubFactory(EmergencyInfoFactory)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """ Create a corresponding user whenever we make a Participant.

        Each Participant stores the ID of its user, but it's not truly a
        foreign key, since the row resides in another database. Accordingly,
        we cannot use a SubFactory for the User object.
        """
        UserFactory.create(id=kwargs['user_id'], email=kwargs['email'])
        return super()._create(model_class, *args, **kwargs)


class TripFactory(DjangoModelFactory):
    class Meta:
        model = models.Trip

    name = Sequence(lambda n: f"Test Trip #{n + 1}")
    description = "An awesome trip into the Whites"
    difficulty_rating = "Intermediate"
    level = "B"
    activity = "winter_school"
    creator = SubFactory(ParticipantFactory)


class FeedbackFactory(DjangoModelFactory):
    class Meta:
        model = models.Feedback

    participant = SubFactory(ParticipantFactory)
    leader = SubFactory(ParticipantFactory)
    trip = SubFactory(TripFactory)
    comments = "Participant did a great job."