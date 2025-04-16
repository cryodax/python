class Television:
    """
    A class representing a television object
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        function to create a tv object and set the default values
        """
        self.__status = False
        self.__muted = False
        self.__volume = 0
        self.__channel = 0

    def power(self) -> None:
        """
        function to turn the tv on and off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        function to mute and unmute the tv
        """
        if self.__status:
            self.__muted = not self.__muted
        # if self.__muted:
        #     self.__muted = False
        # else:
        #     self.__muted = True

    def channel_up(self) -> None:
        """
        function to increase tv channel value
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        function to decrease tv channel value
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        function to increase tv volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1
            else:
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1


    def volume_down(self) -> None:
        """
        function to decrease tv volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1
            else:
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1


    def __str__(self) -> str:
        """
        function to return the TV's power state, channel and volume
        :return: string in the form of 'Power = tv status, Channel = channel, Volume = volume'
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'






