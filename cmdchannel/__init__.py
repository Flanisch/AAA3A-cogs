from .AAA3A_utils.cogsutils import CogsUtils  # isort:skip
import json
from pathlib import Path

from .cmdchannel import CmdChannel

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]

async def setup(bot):
    cog = CmdChannel(bot)
    await CogsUtils().add_cog(bot, cog)