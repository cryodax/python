import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv


    def test_init(self):
        #tv initial values
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        #tv on
        self.tv.power()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

        #tv off
        self.tv.power()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        #tv on, volume up 1, mute
        self.tv.power()
        self.tv.volume_up() #volume = 1
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

        #tv on, unmute
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #tv off, mute
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'

        #tv off, unmute
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        #tv off, channel up
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #tv on, channel up 1
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 1, Volume = 0'

        #tv on, channel up past max value 3
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        #tv off, channel down
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #tv on, channel down past min value
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        #tv off, volume up 1
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #tv on, volume up 1
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #tv on, mute, volume up 1
        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'

        #tv on, volume up past max 2
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        #tv off, volume down 1
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #tv on, volume up to max, volume down 1
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #tv on, mute, volume down 1
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

        #tv on, volume down past min 0
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_str(self):
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'


