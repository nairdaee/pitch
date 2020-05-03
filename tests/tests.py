import unittest
from app import db
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='james55')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('james55'))

        import unittest


class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.user = User(username='james', password='james55',
                         email='jamesgathuru001@gmail.com')
        self.new_comment = Comment(
            comment='comment', pitch_id=1, user_id=self.user)
        self.new_pitch = Pitch(id=1, title="Pitch", body='pitches',
                               category='Interview', writer=self.user, comment=self.new_comment)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_variables(self):
        self.assertEquals(self.new_pitch.id, 1)
        self.assertEquals(self.new_pitch.title, 'Pitch')
        self.assertEquals(self.new_pitch.body, 'pitches')
        self.assertEquals(self.new_pitch.category, "Interview")
        self.assertEquals(self.new_pitch.writer, self.user)
        self.assertEquals(self.new_pitch.comment, self.new_comment)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch(self):

        self.new_pitch.save_pitch()
        get_pitches = Pitch.get_pitch(1)
        self.assertTrue(len(get_pitches) == 1)
