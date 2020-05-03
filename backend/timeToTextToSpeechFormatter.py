#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.libs.internals.profileformatter import ProfileFormatter
from raspiot.profiles.soundtexttospeechprofile import SoundTextToSpeechProfile

class TimeToTextToSpeechFormatter(ProfileFormatter):
    """
    Current time data to TextToSpeechProfile
    """
    def __init__(self, events_broker):
        """
        Constructor

        Args:
            events_broker (EventsBroker): events broker instance
        """
        ProfileFormatter.__init__(self, events_broker, u'parameters.time.now', SoundTextToSpeechProfile())

    def _fill_profile(self, event_values, profile):
        """
        Fill profile with event data

        Args:
            event_values (dict): event values
            profile (Profile): profile instance

        Note:
            http://www.anglaisfacile.com/exercices/exercice-anglais-2/exercice-anglais-3196.php
        """
        if event_values[u'hour']==0 and event_values[u'minute']==0:
            profile.text = u'It\'s midnight'
        if event_values[u'hour']==12 and event_values[u'minute']==0:
            profile.text = u'It\'s noon'
        elif event_values[u'minute']==0:
            profile.text = u'It\'s %d o\'clock' % event_values[u'hour']
        elif event_values['minute']==15:
            profile.text = u'It\'s quarter past %d' % event_values[u'hour']
        elif event_values[u'minute']==45:
            profile.text = u'It\'s quarter to %d' % (event_values[u'hour']+1)
        elif event_values[u'minute']==30:
            profile.text = u'It\'s half past %d' % event_values[u'hour']
        elif event_values[u'minute']<30:
            profile.text = u'It\'s %d past %d' % (event_values[u'minute'], event_values[u'hour'])
        elif event_values[u'minute']>30:
            profile.text = u'It\'s %d to %d' % (60-event_values[u'minute'], event_values[u'hour']+1)

        return profile


