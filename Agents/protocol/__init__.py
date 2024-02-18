from typing import List
from uagents import Context, Model, Protocol
from .yt_proto import *
from .grader_proto import *
from .home_proto import *
# from .summarizer_proto import *
# from protocol.models import *

summary_proto = Protocol(name="summmary", version="0.1.0")
quiz_proto = Protocol(name="quiz", version="0.1.0")