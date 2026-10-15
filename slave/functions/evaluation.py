import sys
import io
import traceback
from discord.ext import commands
from discord import File, Embed
from slave import slave as Yuri
from slave.decorator.filter_user import filter_user

def p(code):
    print(code)

@filter_user('gPunisher', 1515042523016593499)
async def evall(ctx, *args, **kwargs):
    if len(ctx.message.content.split()) < 2:
        return await ctx.send("Please enter code to run it!")
    stats = await ctx.send("Loading...")
    
    cmd = ctx.message.content.split(None, 1)[1]
    replied_message = ctx.message.reference.resolved
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    redirected_output = io.StringIO()
    redirected_error = io.StringIO()
    sys.stdout = redirected_output
    sys.stderr = redirected_error
    exc = None

    try:
        exec(f"async def __aexec(ctx, replied_message):\n" + "".join(f"    {line}\n" for line in cmd.splitlines()))
        await locals()["__aexec"](ctx, replied_message)
    except Exception:
        exc = traceback.format_exc()
    stdout, stderr = redirected_output.getvalue(), redirected_error.getvalue()
    sys.stdout, sys.stderr = old_stdout, old_stderr
    evaluation = exc if exc else stderr if stderr else stdout if stdout else "Success"
    output_code = f"{evaluation.strip()}"
    if len(output_code) > 3500:
        with io.BytesIO(evaluation.encode()) as out_file:
            out_file.name = "eval_output.txt"
            await ctx.send("Output too big, sending as file:", file=File(out_file))
    else:
        embed = Embed(title="Output", description=f"```python\n{output_code}```", color=0x1E90FF)
        await ctx.send(embed=embed)
    await stats.delete()      

async def setup(Yuri):
    Yuri.add_command(commands.Command(evall, name="eval"))
