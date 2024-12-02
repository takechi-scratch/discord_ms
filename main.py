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

bot = commands.Bot(
    command_prefix="t!",
    case_insensitive=True,
    help_command=None,
    intents=discord.Intents.all()
)
tree = bot.tree


@tree.command(name="ping", description="Botの状況を確認します。")
async def send_ping(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Pong!",
        color=discord.Color.green()
    )
    embed.add_field(name="応答速度", value=f"{round(bot.latency * 1000)}ms")
    embed.add_field(name="導入サーバー数", value=f"{len(bot.guilds)} サーバー")
    embed.add_field(name="利用可ユーザー数", value=f"{len(bot.users)} 人")
    embed.set_footer(text="開発: takechi", icon_url="https://api.takechi.cloud/src/icon/takechi_v2.1.png")

    await interaction.response.send_message(embed=embed)
    logger.info(f"Pong 応答速度: {round(bot.latency * 1000)}ms")


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
    logger.info("マインスイーパーを作成しました。")


@bot.event
async def on_ready():
    await tree.sync()
    logger.info("Botの準備ができました！")


bot.run(os.environ["DISCORD_TOKEN"])
