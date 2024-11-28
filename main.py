import os
from logging import getLogger, StreamHandler, DEBUG

from dotenv import load_dotenv
from discord.ext import commands
import discord

from mylib.mine_sweeper import MSBoard


load_dotenv(verbose=True)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(
    command_prefix="t!",
    case_insensitive=True,
    help_command=None,
    intents=discord.Intents.all()
)
tree = bot.tree


@tree.command(name="make_ms", description="マインスイーパーを作成します。")
@discord.app_commands.describe(
    size="盤面のサイズ",
    mines="爆弾の数",
    ephemeral="非公開で生成するか (Trueで非公開)"
)
async def send_ms(interaction: discord.Interaction, size: int = 10, mines: int = 12, ephemeral: bool = False):
    ms = MSBoard(min(size, 10), mines)
    res_text = f"爆弾数: {ms.mines}\n" + "\n".join(["".join(row) for row in ms.board])

    await interaction.response.send_message(res_text, ephemeral=ephemeral)


@bot.event
async def on_ready():
    await tree.sync()
    logger.info("Botの準備ができました！")


bot.run(os.environ["DISCORD_TOKEN"])
